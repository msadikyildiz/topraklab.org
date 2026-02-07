#!/usr/bin/env python3
"""
Asset sanitization pipeline for Toprak Lab science figures.

Processes all images in src/assets/images/science/:
  1. Backup originals
  2. Trim whitespace borders + add uniform 16px margin (unless skip_trim)
  3. Normalize color profile to sRGB
  4. LANCZOS upscale (if width < 1800px)
  5. Apply subtle brush texture overlay on white areas (figures only)
  6. Save (PNG for transparency/line-art, JPEG 95 for photos)

Also generates public/textures/paper-grain.png (512x512 tileable).
"""

import shutil
import subprocess
from pathlib import Path

import numpy as np
from PIL import Image

# ── Paths ──
ROOT = Path(__file__).resolve().parent.parent
SCIENCE_DIR = ROOT / "src" / "assets" / "images" / "science"
ORIGINALS_DIR = SCIENCE_DIR / ".originals"
TEXTURES_DIR = ROOT / "public" / "textures"

TARGET_WIDTH = 1800  # 2.5x the 720px CSS max-width
LOGO_TARGET = 1024   # 2x the 512px original for retina at 48px CSS
MARGIN_PX = 16
TEXTURE_OPACITY = 0.035  # ~3.5%
NOISE_AMPLITUDE = 10     # 0-255 scale

# Images and their properties
IMAGES = {
    "palmer-2015-delayed-commitment.jpg":       {"is_logo": False, "skip_trim": False, "format": "jpg"},
    "palmer-2015-fitness-landscape.jpg":        {"is_logo": False, "skip_trim": False, "format": "jpg"},
    "chevereau-2015-evolutionary-dynamics.jpg": {"is_logo": False, "skip_trim": False, "format": "jpg"},
    "lyon-2025-fig1.jpg":                       {"is_logo": False, "skip_trim": False, "format": "jpg"},
    "lyon-2025-fig3.jpg":                       {"is_logo": False, "skip_trim": False, "format": "jpg"},
    "gaszek-2025-fig1.jpg":                     {"is_logo": False, "skip_trim": False, "format": "jpg"},
    "gaszek-2025-fig2.jpg":                     {"is_logo": False, "skip_trim": False, "format": "jpg"},
    "biomarker-pipeline-schematic.png":         {"is_logo": False, "skip_trim": False, "format": "png"},
    "coskun-2025-fig1.png":                     {"is_logo": False, "skip_trim": False, "format": "png"},
    "earlymarker-logo.png":                     {"is_logo": True,  "skip_trim": True,  "format": "png"},
}


def run_cmd(cmd: list[str], desc: str = "") -> subprocess.CompletedProcess:
    """Run a shell command, raise on failure."""
    print(f"  {desc}: {' '.join(str(c) for c in cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ERROR: {result.stderr.strip()}")
        raise RuntimeError(f"Command failed: {' '.join(str(c) for c in cmd)}")
    return result


def backup(src: Path):
    """Copy original to .originals/ if not already backed up."""
    ORIGINALS_DIR.mkdir(parents=True, exist_ok=True)
    dest = ORIGINALS_DIR / src.name
    if not dest.exists():
        shutil.copy2(src, dest)
        print(f"  Backed up → {dest.name}")
    else:
        print(f"  Backup exists: {dest.name}")


def trim_whitespace(img_path: Path, tmp_dir: Path) -> Path:
    """Trim whitespace borders with ImageMagick, then add 16px uniform margin."""
    trimmed = tmp_dir / f"trimmed_{img_path.name}"

    # ImageMagick trim: flatten alpha onto white, add 1px white border so
    # -trim always references pure white, then trim with 5% fuzz to catch
    # near-white backgrounds (~249-252 per channel).
    run_cmd(
        [
            "magick", str(img_path),
            "-background", "white", "-flatten",
            "-bordercolor", "white", "-border", "1",
            "-fuzz", "5%", "-trim", "+repage",
            str(trimmed),
        ],
        desc="Trim",
    )

    # Add uniform margin with Pillow
    img = Image.open(trimmed)
    new_w = img.width + 2 * MARGIN_PX
    new_h = img.height + 2 * MARGIN_PX

    # Detect background color from corners for margin fill
    bg_color = _detect_bg_color(img)
    padded = Image.new(img.mode, (new_w, new_h), bg_color)
    padded.paste(img, (MARGIN_PX, MARGIN_PX))
    padded.save(trimmed)
    print(f"  Added {MARGIN_PX}px margin → {new_w}×{new_h}")

    return trimmed


def _detect_bg_color(img: Image.Image):
    """Sample corner pixels to detect background color."""
    pixels = []
    w, h = img.size
    for x, y in [(0, 0), (w-1, 0), (0, h-1), (w-1, h-1)]:
        pixels.append(img.getpixel((x, y)))

    if img.mode == "RGBA":
        return tuple(int(np.mean([p[i] for p in pixels])) for i in range(4))
    elif img.mode == "RGB":
        return tuple(int(np.mean([p[i] for p in pixels])) for i in range(3))
    else:
        return int(np.mean(pixels))


def normalize_color_profile(img_path: Path, tmp_dir: Path) -> Path:
    """Strip embedded profiles, normalize to sRGB 8-bit."""
    output = tmp_dir / f"srgb_{img_path.name}"
    run_cmd(
        ["magick", str(img_path), "-strip", "-colorspace", "sRGB", "-depth", "8", str(output)],
        desc="Color profile"
    )
    return output


def pil_upscale(img_path: Path, tmp_dir: Path, target_w: int) -> Path:
    """LANCZOS upscale to target width — clean and sharp for scientific figures."""
    img = Image.open(img_path)
    if img.width >= target_w:
        print(f"  Skip upscale: {img.width}px >= {target_w}px target")
        return img_path
    ratio = target_w / img.width
    new_h = int(img.height * ratio)
    resized = img.resize((target_w, new_h), Image.LANCZOS)
    output = tmp_dir / f"upscaled_{img_path.name}"
    resized.save(output, "PNG")
    print(f"  LANCZOS resize {img.width}x{img.height} -> {target_w}x{new_h}")
    return output


def logo_upscale(img_path: Path, tmp_dir: Path) -> Path:
    """Simple LANCZOS upscale for the logo. No AI upscaling, no trim, no texture."""
    img = Image.open(img_path)
    if img.width >= LOGO_TARGET:
        print(f"  Skip logo upscale: {img.width}px ≥ {LOGO_TARGET}px target")
        return img_path

    ratio = LOGO_TARGET / img.width
    new_h = int(img.height * ratio)
    resized = img.resize((LOGO_TARGET, new_h), Image.LANCZOS)
    output = tmp_dir / f"upscaled_{img_path.name}"
    resized.save(output, "PNG")
    print(f"  Logo LANCZOS {img.width}×{img.height} → {LOGO_TARGET}×{new_h}")
    return output


def apply_brush_texture(img_path: Path) -> Image.Image:
    """Apply subtle warm grain texture to white/light areas only."""
    img = Image.open(img_path).convert("RGB")
    arr = np.array(img, dtype=np.float64)

    # Generate noise layer
    rng = np.random.default_rng(42)
    noise = rng.normal(0, NOISE_AMPLITUDE, arr.shape)

    # Warm tint: shift noise slightly warm (more red, less blue)
    noise[:, :, 0] += 2   # red slightly warmer
    noise[:, :, 1] += 1   # green slightly warmer
    noise[:, :, 2] -= 1   # blue slightly cooler

    # Luminance mask: only apply texture to light areas (L > 200)
    luminance = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]
    # Smooth transition from L=180 to L=220
    mask = np.clip((luminance - 180) / 40, 0, 1)
    mask = np.stack([mask] * 3, axis=-1)

    # Apply with opacity
    textured = arr + noise * mask * TEXTURE_OPACITY
    textured = np.clip(textured, 0, 255).astype(np.uint8)

    return Image.fromarray(textured)


def generate_paper_grain():
    """Generate a 512×512 tileable paper grain texture."""
    TEXTURES_DIR.mkdir(parents=True, exist_ok=True)
    output = TEXTURES_DIR / "paper-grain.png"

    size = 512
    rng = np.random.default_rng(7)

    # Base: warm off-white
    base = np.full((size, size, 4), [252, 250, 247, 0], dtype=np.uint8)

    # Add noise
    noise = rng.normal(0, 6, (size, size))
    # Make tileable by mirroring edges
    blend = 32
    for i in range(blend):
        t = i / blend
        noise[i, :] = noise[i, :] * t + noise[size - 1 - i, :] * (1 - t)
        noise[:, i] = noise[:, i] * t + noise[:, size - 1 - i] * (1 - t)

    # Slight warm bias
    warm_noise_r = np.clip(noise + 2, -20, 20)
    warm_noise_g = np.clip(noise + 1, -20, 20)
    warm_noise_b = np.clip(noise - 1, -20, 20)

    # Very low opacity — alpha ~6-8 (out of 255)
    alpha = np.clip(np.abs(noise) * 1.2, 0, 12).astype(np.uint8)

    base[:, :, 0] = np.clip(128 + warm_noise_r, 0, 255).astype(np.uint8)
    base[:, :, 1] = np.clip(128 + warm_noise_g, 0, 255).astype(np.uint8)
    base[:, :, 2] = np.clip(128 + warm_noise_b, 0, 255).astype(np.uint8)
    base[:, :, 3] = alpha

    img = Image.fromarray(base, "RGBA")
    img.save(output, "PNG", optimize=True)
    size_kb = output.stat().st_size / 1024
    print(f"Generated paper-grain.png: {size}×{size}, {size_kb:.1f} KB")


def process_image(name: str, props: dict):
    """Full processing pipeline for a single image."""
    src = SCIENCE_DIR / name
    if not src.exists():
        print(f"SKIP: {name} not found")
        return

    print(f"\n{'='*60}")
    print(f"Processing: {name}")
    print(f"{'='*60}")

    # Create temp working dir
    tmp_dir = SCIENCE_DIR / ".tmp"
    tmp_dir.mkdir(exist_ok=True)

    try:
        # 1. Backup
        backup(src)

        current = src

        if props["is_logo"]:
            # Logo: simple LANCZOS upscale, skip trim and texture
            current = logo_upscale(current, tmp_dir)
            result = Image.open(current)
        else:
            # 2. Trim whitespace (unless skip_trim)
            if not props.get("skip_trim", False):
                current = trim_whitespace(current, tmp_dir)

            # 3. Normalize color profile
            current = normalize_color_profile(current, tmp_dir)

            # 4. Upscale
            current = pil_upscale(current, tmp_dir, TARGET_WIDTH)

            # 5. Brush texture overlay
            result = apply_brush_texture(current)

        # 6. Save
        output = SCIENCE_DIR / name
        if props["format"] == "jpg":
            result.save(output, "JPEG", quality=95)
        else:
            result.save(output, "PNG", optimize=True)

        size_kb = output.stat().st_size / 1024
        print(f"  Saved: {output.name} ({result.width}×{result.height}, {size_kb:.1f} KB)")

    finally:
        # Clean up temp files
        shutil.rmtree(tmp_dir, ignore_errors=True)


def main():
    print("Toprak Lab Figure Sanitization Pipeline")
    print("=" * 60)

    # Generate tileable paper grain texture
    generate_paper_grain()

    # Process all images
    for name, props in IMAGES.items():
        process_image(name, props)

    print(f"\n{'='*60}")
    print("Done! Originals saved in .originals/")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
