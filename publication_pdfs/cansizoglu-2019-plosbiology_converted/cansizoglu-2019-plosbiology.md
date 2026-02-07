

## METHODS AND RESOURCES

# Rapid ultrasensitive detection platform for antimicrobial susceptibility testing

Mehmet F. Cansizoglu<sup>1</sup>, Yusuf Talha Tamer<sup>1</sup>, Michael Farid<sup>2</sup>, Andrew Y. Koh<sup>3,4</sup>, Erdal Toprak<sup>1,5\*</sup>

**1** Green Center for Systems Biology, University of Texas Southwestern Medical Center, Dallas, Texas, United States of America, **2** Department of Biomedical Engineering, Johns Hopkins University, Baltimore, Maryland, United States of America, **3** Department of Pediatrics, University of Texas Southwestern Medical Center, Dallas, Texas, United States of America, **4** Department of Microbiology, University of Texas Southwestern Medical Center, Dallas, Texas, United States of America, **5** Department of Pharmacology, University of Texas Southwestern Medical Center, Dallas, Texas, United States of America

\* [erdal.toprak@utsouthwestern.edu](mailto:erdal.toprak@utsouthwestern.edu)

![Check for updates icon](0538daaa5583c23e17db3a12f2281a55_img.jpg)

Check for updates icon

###### OPEN ACCESS

**Citation:** Cansizoglu MF, Tamer YT, Farid M, Koh AY, Toprak E (2019) Rapid ultrasensitive detection platform for antimicrobial susceptibility testing. PLoS Biol 17(5): e3000291. <https://doi.org/10.1371/journal.pbio.3000291>

**Academic Editor:** Andrew Fraser Read, The Pennsylvania State University, UNITED STATES

**Received:** November 13, 2018

**Accepted:** May 10, 2019

**Published:** May 30, 2019

**Copyright:** © 2019 Cansizoglu et al. This is an open access article distributed under the terms of the [Creative Commons Attribution License](#), which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

**Data Availability Statement:** All relevant data are within the paper and its Supporting Information files.

**Funding:** This work was supported by the UTSW Endowed Scholars Program (ET), Human Frontiers Science Program Research Grant RGP0042/2013 (ET), National Institutes of Health grant R01GM125748 (ET), DOD PR172118 (ET), and National Institutes of Health grant R01AI123163 (AYK), as well as the Roberta I. and Norman L. Pollock Fund (AYK). The funders had no role in

## Abstract

Rapid detection and phenotyping of pathogenic microbes is critical for administration of effective antibiotic therapies and for impeding the spread of antibiotic resistance. Here, we present a novel platform, rapid ultrasensitive detector (RUSD), that utilizes the high reflectance coefficient at high incidence angles when light travels from low- to high-refractive-index media. RUSD leverages a principle that does not require complex manufacturing, labeling, or processing steps. Utilizing RUSD, we can detect extremely low cell densities (optical density [OD]  $\ge 5 \times 10^{-7}$ ) that correspond to approximately 20 bacterial cells or a single fungal cell in the detection volume, which is nearly 4 orders of magnitude more sensitive than standard OD methods. RUSD can measure minimum inhibitory concentrations (MICs) of commonly used antibiotics against gram-negative and gram-positive bacteria, including *Staphylococcus aureus*, *Pseudomonas aeruginosa*, and *Escherichia coli*, within 2 to 4 h. Here, we demonstrate that antibiotic susceptibility tests for several pathogens can rapidly be performed with RUSD using both small inoculum sizes (500 cells/mL) and larger inoculum sizes ( $5 \times 10^5$  cells/mL) used in standard antibiotic susceptibility tests. We anticipate that the RUSD system will be particularly useful for the cases in which antibiotic susceptibility tests have to be done with a limited number of bacterial cells that are available. Its compatibility with standard antibiotic susceptibility tests, simplicity, and low cost can make RUSD a viable and rapidly deployed diagnostic tool.

## Introduction

Optimal treatment of infectious diseases requires early detection of pathogenic microbes [1]. Despite advances in medical technology, both detection and characterization of pathogenic microbes can still take up to several days [2–4]. In many cases, clinicians are relegated to starting empiric antibiotic therapies that are typically broad in coverage and may have deleterious sequelae such as inducing gut microbiome dysbiosis and potentially exacerbating the ongoing

study design, data collection and analysis, decision to publish, or preparation of the manuscript.

**Competing interests:** A provisional patent application for RUSD is filed by ET and MFC. AYK is a consultant for Merck Research Laboratories.

**Abbreviations:** A/S, ampicillin/sulbactam; AST, antibiotic susceptibility testing; Aug, amoxicillin/clavulanic acid; Azt, aztreonam; BP, breakpoint; CA, clavulanic acid; Cax, ceftriaxone; Cf, cephalothin; Cfz, cefazolin; CMLCMC, Clinical Microbiology Laboratory of Children's Medical Center; CFU, colony forming unit; Cp, ciprofloxacin; Cpe, cefepime; Crm, cefuroxime; FN, false negative; Fd, nitrofurantoin; Gm, gentamicin; iFAST, in Fiber Antibiotics Susceptibility Testing; Imp, imipenem; LOD, limit of detection; LOQ, limit of quantification; LB, lysogeny broth; Mer, meropenem; MIC, minimum inhibitory concentration; Mxf, moxifloxacin; ND, no data; Neg Contr., negative control;  $n_i$ , index of refraction; OD, optical density; P-T, piperacillin-tazobactam; RUSD, rapid ultrasensitive detector; T/S, trimethoprim/sulfamethoxazole; Te, tetracycline; Tgc, tigecycline; To, tobramycin.

antibiotic resistance crisis [5]. Therefore, there is an urgent need for a rapid, affordable, and highly sensitive detection platform that can significantly reduce the time needed for antibiotic susceptibility determination and enable optimized, targeted therapy selection sooner [1,2,6].

Conventional culture-based assays require microbial growth at high cell densities and are thus inherently slow [3,4]. Here, we introduce rapid ultrasensitive detector (RUSD), a label-free and low-cost fiber-based platform (see [Materials and methods](#)). The hollow fiber in the RUSD apparatus is utilized as an optofluidic channel, which serves as a selective waveguide for laser light and as a detection and/or growth chamber for microbial cells. Microbial cells flow through the channel either by continuous circulation that includes a computer-operated pump and a degassing/bubble trap mechanism to avoid bubble formations, or simply by manual injection via a syringe ([Fig 1A](#)). RUSD takes advantage of the loss of reflectivity within the hollow fiber because of both optical absorption and scattering events. Photons that hit obstacles on the travel path are deflected and violate the condition for high reflectivity. The laser beam is coupled into the hollow core of the fiber, together with cells in growth media (index of refraction  $[n_i] = 1.33$ ). The laser beam is focused to the entrance of the fiber such that the incidence angle of the laser at the fiber wall remains at a grazing of  $\ge 89^\circ$ , which keeps the reflectance coefficient  $R > 0.82$  for both s and p polarizations of light ([Fig 1B](#)). Photons that hit obstacles on the travel path, however, lose the condition for high reflectivity through mainly scattering or absorption events and are selectively filtered out along the hollow fiber waveguide. This creates a 2D cross-sectional projection shadow of the cells dispersed inside a 3D volume at the end of fiber ([Fig 1C](#)). Total light lost during travel is estimated by  $A = I_0(\sum_{i=1}^{n} a_i/a_{\text{fiber}}) \approx I_0 n \pi r^2 / a_{\text{fiber}}$  (Equation 1), where  $I_0$  is the intensity of light entering the fiber,  $a_i$  is the cross-sectional area of the  $i^{\text{th}}$  cell,  $a_{\text{fiber}}$  is the cross-sectional area of the fiber (i.e., approximately  $0.2 \text{ mm}^2$ ),  $n$  is the cell number, and  $r$  is the average radius of a cell (assuming spherical cell shape, i.e., approximately  $1 \text{ } \mu\text{m}$  for bacteria). This equation remains valid when the total cross-sectional area of cells is less than the cross-sectional area of the fiber. The light intensity at the end of the fiber is measured through a photodiode, in which the difference in reference to blank media measurement ( $\Delta V$ ) is converted to optical density (OD) readings (i.e.,  $OD = 1$  corresponds to approximately  $5 \times 10^8$  cells per milliliter of *E. coli* culture) using a calibration curve ([Fig 1D](#)).

The physical model explaining the working principle of RUSD suggests that the detector response ( $\Delta V$ ) is proportional to the ratio between projected cell area and fiber cross-sectional area (Equation 1). Thus, increased cell size or decreased fiber diameter enhances sensitivity, making it possible to detect larger cells (e.g., eukaryotic cells) at lower densities. At a sensitivity threshold of  $\Delta V = 1 \text{ mV}$ , which is typical for low-cost electronics, the detection system is estimated to be capable of sensing about 27 spherical cells of  $1 \text{ } \mu\text{m}$  radius, or a single spherical cell of  $8 \text{ } \mu\text{m}$  diameter in a  $500 \text{ } \mu\text{m}$  diameter,  $40 \text{ cm}$  long (L) fiber setup ([Fig 1E](#)). The projection coverage of the cells also increases linearly with the encapsulated fiber volume, laying out a simple ( $\Delta V \propto L$ ) relation with the length of the optical fiber. Signal strength ( $\Delta V$ ) in RUSD behaves in accordance with  $\Delta V \propto 1/R^2$ , where  $R$  is the inner diameter of the hollow core. Thus, a decrease in fiber diameter will enhance the sensitivity per cell with the cost of reducing the detection volume. The signal in the detection system model saturates at relatively low cell densities (approximately  $OD \text{ 0.01}$  for *E. coli* cells, [Fig 1D](#)) because the narrow cross section of the fiber is optically blocked by randomly distributed cells in 3D space.

On the other hand, in the conventional absorption-based OD measurements, which employ the Beer-Lambert relation, absorption is given as  $A = I_0(1 - e^{-\mu l})$  (Equation 2), where  $\mu$  is the attenuation coefficient, and  $l$  is the length (thickness) of the specimen. For a well-dispersed absorbing species,  $\mu$  is also dependent on the volumetric concentration. In a nonuniform

![](3cab54230d8ae3b786ddda81346602cc_img.jpg)

**a)** Schematic of the RUSD platform. A 632 nm laser beam is coupled into a fiber (Fiber) embedded in a PDMS substrate. The fiber is surrounded by a glass layer (Glass) and has an inlet and outlet for fluid flow. The fiber is positioned within a channel made of soda lime glass and PDMS. The channel is filled with a liquid containing cells (green dots). The laser beam is deflected by the cells, and the deflected light is detected.

**b)** Schematic of the light deflection mechanism. A guided beam (red arrow) passes through a fiber wall (gray bars). When a cell (green oval) is present, it absorbs some of the light and deflects the remaining light (yellow arrow). The deflection angle is  $\theta < 1^\circ$ .

**c)** Schematic of the light source and fiber. A light source (black sphere) emits light that is coupled into a fiber (white cylinder). The fiber is filled with cells (gray dots). The light is deflected by the cells as it travels through the fiber.

**d)** Plot of the change in voltage ( $\Delta V$  in mV) versus the optical density (OD). The plot shows experimental data (open circles) and simulation results (red line). The data points follow a sigmoidal curve, indicating a threshold effect. The x-axis ranges from  $10^{-7}$  to 1, and the y-axis ranges from  $10^0$  to  $10^4$ .

**e)** Heatmap showing the relationship between cell diameter ( $\mu\text{m}$ ) and the number of cells. The color scale represents the change in voltage ( $\Delta V$  in mV), ranging from 0.1 (light blue) to 10000 (dark blue). Red asterisks (\*) indicate specific data points. The x-axis represents the number of cells (1 to 16), and the y-axis represents the cell diameter (1 to 16  $\mu\text{m}$ ).

**Fig 1. RUSD.** (a) Optical schematics of the RUSD apparatus, which utilizes the high reflectance coefficient of light at the interface between thin and dense media (water and glass) at high incidence angles. (b) The focal distance of the laser is set such that the incidence angle ( $\theta$ ) of the laser at the fiber wall remains  $> 89^\circ$ . At  $\theta > 89^\circ$ , the reflectance coefficient of laser light is  $R > 0.82$  for both s and p polarizations of light, allowing the laser beam to travel in liquid and reflect multiple times within the fiber. (c) During travel, any photon encountering a cell or a particle is either absorbed or scattered, losing the angular condition to be guided by the fiber (i.e.,  $\theta > 89^\circ$ ), and any cell on the light path reduces the total intensity proportional to its cross-sectional area and creates a 2D shadow-projection image on the optical detector. The current from the reverse-biased optical detector is passed through a resistor in which the potential difference is converted to a signal for data acquisition. (d) The voltage signal as a function of cell density. Simulation data based on the mathematical model described here and actual RUSD exhibit a high degree of concordance ( $R^2 = 0.97$ ) up to  $OD > 10^{-3}$  and ( $R^2 = 0.93$ ) for the whole data range used here. (e) Signal strength versus number of cells and cell dimensions in RUSD: As the cell size increases, signal strength is multiplied proportionally to the cell cross-sectional area. The cell shape is taken as a square pattern with the specified dimensions. The region marked with red asterisks indicates the boundary of detection at which the signal is above the 1 mV limit. RUSD signal rapidly saturates over approximately OD 0.1 as cells optically block the fiber cross section. OD, optical density; PDMS, polydimethylsiloxane; RUSD, rapid ultrasensitive detector.

<https://doi.org/10.1371/journal.pbio.3000291.g001>

absorption case, as in liquid bacterial cultures, light absorption per single cell is correlated with the size of the cell and hence is almost undetectable. Therefore, in order to increase the sensitivity of absorption-based methods to that of RUSD, the optical path length would have to be increased approximately  $10^3$ – $10^4$  times (e.g., 100-meter-long sample thickness), which is not feasible.

## Results

To determine the sensitivity of the RUSD platform, we first calibrated our system using bacterial (*E. coli*, *S. aureus*, and *P. aeruginosa*) and fungal (*Saccharomyces cerevisiae*, *Candida glabrata*) cells. Overnight cultures were serially diluted, and the voltage signals generated ( $\Delta V$ ) in RUSD were recorded. The cell densities of diluted cultures were also confirmed by colony forming unit (CFU) counts conducted for the very same bacterial cultures ( $1 \text{ OD} \approx 5 \times 10^8 \text{ CFU/mL}$  for all tested bacteria) and fungal cultures ( $1 \text{ OD} \approx 2.2 \times 10^7 \text{ CFU/mL}$  for *S. cerevisiae* and  $1 \text{ OD} \approx 1.25 \times 10^7 \text{ CFU/mL}$  for *C. glabrata*). The measured  $\Delta V$  values and corresponding OD values were linearly correlated on a logarithmic scale on both axes (S1A Fig). Based on this linear correlation, we used a power function ( $\log_{10}[\Delta V] = a + b \log_{10}[\text{OD}]$ ) to fit our data and converted voltage readings to OD values and cell counts. In our experimental settings, for bacteria and fungi, the value of  $a$  was typically between 2.9 and 3.1, whereas  $b$ , the slope of the calibration curve, was found to be between 0.9 and 1.1. The limit of detection (LOD) [7,8] attained at the standard RUSD setup (400 mm long fiber with 500  $\mu\text{m}$  inner diameter) was  $OD \sim 5 \times 10^{-7}$  for bacteria (S1B Fig), which corresponds to approximately 250 bacterial CFU/mL. The limit of quantification (LOQ, [7,8] minimum level of signal after which detector response increases proportional with the cell density) for RUSD was  $OD \ge 1.5 \times 10^{-6}$  for bacteria (S1B Fig), which corresponds to approximately 750 bacterial CFU/mL. Given that our detection volume is roughly 80  $\mu\text{L}$ , we can detect as low as about 20 bacterial cells, which we measured to be about  $10^4$ -fold more sensitive than our commercial plate reader (Tecan M200 Pro). We showed that RUSD can detect a single fungal cell (spherical *S. cerevisiae* or *C. glabrata* with 5–6  $\mu\text{m}$  diameter). All measurements with bacterial cells were done in lysogeny broth (LB) media. The system is, as all optical methods are, limited by the transparency of the medium to the laser light used. Using a more transparent media such as minimal M9 media improves the sensitivity of the instrument by increasing the signal-to-noise ratio, especially in longer fiber setup schemes, decreasing LOD down to about  $2 \times 10^{-7}$ , which corresponds to approximately 8–10 bacterial cells. For practical MIC measurement purposes, any transparent media commonly available can be utilized in measurements.

Depending on the growth conditions and cell type, conventional approaches to detect microbial growth may require several hours to days. In laboratory or clinical settings, the time required for quantitatively measuring bacterial growth largely depends on the inoculum size of

bacteria and growth conditions. For *P. aeruginosa* (PAO1), *S. aureus* (RN4220), *E. coli* (MG1655), and an *E. coli* clinical isolate (ET-CI28), we first quantified the lag time before statistically significant growth as a function of inoculum size using a microplate reader ([S2 Fig](#)). For each microbial strain, the lag time was defined as the first time point in which cell density exceeded the LOQ for our plate reader (LOQ = 0.02, OD<sub>600</sub>). When the initial OD of the bacterial culture is 10<sup>-6</sup> (nearly equal to the LOQ of RUSD), the lag times for the tested microbial strains ranged between 6 and 10 h. Long lag times hinder clinical applications such as antibiotic susceptibility testing (AST) and thus necessitate using large microbial inoculums (i.e., 5 × 10<sup>5</sup> CFU/mL and OD<sub>600</sub> > 0.001).

In contrast, RUSD detects bacterial growth within 1 h. For all 4 bacterial strains, rapid growth was exhibited even at the very initial stages in measurements taken at intervals of about 30 min ([Fig 2D, 2E, 2F and 2G](#)). The doubling times were 29.3 min for *P. aeruginosa* strain PAO1, 21.1 min for *S. aureus* RN4220, 20.6 min for *E. coli* MG1655, and 25.7 min for the *E. coli* (ET-CI28) isolate. We were also able to use the fiber in the RUSD apparatus as a growth chamber. When we injected *E. coli* (MG1655) culture with an initial OD of 10<sup>-5</sup> inside the fiber (37°C, LB media, no mixing or shaking), we observed bacterial growth within the first 30 min and exponential growth within the first 2.5 h, for which the doubling time was approximately 28 min ([S1C Fig](#)). Being able to detect microbial growth at such low cell densities will substantially expedite the time required for AST.

Existing standard antibiotic susceptibility tests are primarily based on 3 methods: (1) disk diffusion assays and (2) liquid-based minimum inhibitory concentration (MIC) measurements in microtiter plates and (3) linear gradient diffusion MIC strips (eTest). The clinical efficiencies of these methods are limited by requirement for overnight incubation of the bacterial cultures [9]. To determine whether the RUSD platform could expedite the antibiotic resistance detection process, we developed a simple assay called “in Fiber Antibiotic Susceptibility Testing” (iFAST). Briefly, we either grow bacterial cells in flasks and periodically monitor growth using RUSD or utilize the hollow fiber as a growth chamber. As a proof of concept, we conducted antibiotic susceptibility assays for levofloxacin, amikacin, and piperacillin-tazobactam (P-T) for strains of *E. coli* (MG1655, ET-CI28), *P. aeruginosa* (PAO1), and *S. aureus* (RN4220), as indicated, using RUSD and microbroth dilution approach (initial cell density = approximately 500 cells/mL or OD of approximately 10<sup>-6</sup>).

For *E. coli* strains (MG1655 and ET-CI28), *P. aeruginosa* (PAO1), and *S. aureus* (RN4220), RUSD revealed the levofloxacin dose response within about the first 2 h of the iFAST assay, with constant MIC values of 0.05 µg/mL over time (range 60–270 min) for both *E. coli* strains and 0.5 µg/mL for both PAO1 and RN4220. ([Fig 3](#)). The MIC values for levofloxacin measured by the robotic platform for both *E. coli* strains, *P. aeruginosa*, and *S. aureus* were 0.04 µg/mL, 0.3 µg/mL, and 0.2 µg/mL, respectively. For the clinical *E. coli* isolate (ET-CI28), the MIC values for amikacin and P-T obtained by iFAST assays were 20 and 10 µg/mL, respectively. Corresponding MIC values by the robotic platform were 10 µg/mL and 3 µg/mL, which required 7 to 14 h ([S1 Movie, S3 Fig](#)). The minor differences between the MIC values measured by RUSD and our robotic platform are likely due to nonidentical experimental conditions used for these assays. In order to confirm that as the cause for those differences, we grew *E. coli* cells (MG1655 and ET-CI28) in large flasks using increasing concentrations of antibiotics (P-T and amikacin, respectively) and periodically measured cell densities in both RUSD and a spectrophotometer ([S4A Fig](#) and [S4B Fig](#)). In both cases, the MIC values measured using both RUSD and spectrophotometer were concordant, suggesting the initial differences in MIC values we observed were unlikely to be due to differences in detection method. Also, the time required to obtain MIC values using RUSD was about 5 h shorter than the time required using the

![Figure 2: RUSD detects extremely low bacterial and fungal cell counts. Panels a-c show histograms of cell counts for C. glabrata, S. cerevisiae, and E. coli at low ODs. Panels d-g show growth curves for E. coli (MG1655), S. aureus (RN4220), P. aeruginosa (PA01), and ET-CI28, with doubling times indicated.](55d2bfe1c3d04e86df8d7a104d802172_img.jpg)

**a) *C. glabrata* OD:  $10^{-6}$**

**b) *S. cerevisiae* OD:  $10^{-6}$**

**c) *E. coli* OD:  $5 \times 10^{-7}$**

**d) *E. coli* (MG1655) Doubling Time: 20.6 min**

**e) *S. aureus* (RN4220) Doubling Time: 21.1 min**

**f) *P. aeruginosa* (PA01) Doubling Time: 29.3 min**

**g) ET-CI28 Doubling Time: 25.7 min**

Figure 2: RUSD detects extremely low bacterial and fungal cell counts. Panels a-c show histograms of cell counts for C. glabrata, S. cerevisiae, and E. coli at low ODs. Panels d-g show growth curves for E. coli (MG1655), S. aureus (RN4220), P. aeruginosa (PA01), and ET-CI28, with doubling times indicated.

**Fig 2. RUSD detects extremely low bacterial and fungal cell counts.** (a) Top panel: Counts for *C. glabrata* at approximately OD  $10^{-6}$  displays a Poisson distribution with counts of 0, 1, 2, and 3 with a mean value of about 1. Bottom panel: Increasing the yeast cell density shifts distribution toward a normal distribution with a mean value of about 5.3 cells. (b) *S. cerevisiae* at an OD nearly  $10^{-6}$

(top panel) results in a Poisson distribution with counts of 0, 1, and 2 and a mean value of approximately 0.48; (lower panel) a slight increase of cell density moves distribution toward a normal distribution with a mean value of approximately 4 cells. (c) Counts for *E. coli* culture at (top panel) an OD of approximately  $5 \times 10^{-7}$ , yields about 25 cells; (lower panel) increasing the bacterial cell density slightly shifts distribution toward a normal distribution with a similar mean value of about 24 cells with smaller standard deviation, which shows the sensitivity limit of the device. ODs of bacterial cultures grown in LB (started from OD roughly  $5 \times 10^{-7}$ ) and recorded by RUSD: (d) *E. coli* (MG1655), (e) *S. aureus* (RN4220), (f) *P. aeruginosa* (PAO1), and (g) an *E. coli* clinical isolate (ET-CI28). (The data for Fig 2 can be found in [S1 Data](#)). LB, lysogeny broth; OD, optical density; RUSD, rapid ultrasensitive detector.

<https://doi.org/10.1371/journal.pbio.3000291.g002>

spectrophotometer. In summary, for several bacterial strains and antibiotics, RUSD reduced the time for susceptibility characterization by 5 to 12 h.

Finally, we devised an antibiotic susceptibility assay to compare the RUSD method with the clinically approved standard antibiotic susceptibility tests, which typically start from higher cell densities (i.e.,  $OD > 10^{-3}$ ). We utilized a commercially available gram-negative MIC panel (NM43, Beckmann Coulter B1017-420) that includes 29 antibiotics and antibiotic combinations ([Table 1](#)). We used 10 clinical *E. coli* isolates (CIET-001 to 010) that were previously phenotyped at the Clinical Microbiology Laboratory of Children's Medical Center (CMLCMC), Dallas, Texas. For these measurements, we adhered to the manufacturer's protocol for preparation and inoculation of the MicroScan Neg MIC Panel Type 43 (NM43, Beckman Coulter) in which a starting cell density of 0.5 McFarland (about 0.25  $OD_{600}$ ) is then further diluted before inoculating into the antibiotic panel with a final target inoculum of  $3-7 \times 10^5$  CFU/mL. First, we grew every clinical strain for 24 h and determined MIC values by visual inspection following the guidelines provided by the manufacturer and confirmed that the MIC values we obtained were in line with the MIC values provided by the CMLCMC. Then, we grew one of the clinical strains (CIET-001) that was resistant to some of the compounds in the antibiotic panel, using different incubation times for optimizing minimum inhibition time required for MIC determination with RUSD ([Fig 4A, Table 1](#)). We performed 10 consecutive cell density measurements using RUSD at hourly intervals and tracked the growth in each well of the NM43 MIC test panel ([Fig 4A](#)). Using 3 different growth thresholds (half, one, and two doublings compared to initial inoculum size of about  $OD 2 \times 10^{-3}$ ), we converted growth curves to binary resistance maps, in which blue indicates growth/resistance and white indicates inhibition/susceptibility ([Fig 4B](#)). This data set was compared to the expected resistance map for the same *E. coli* isolate. Correlations between the observed resistance map at different time points and the expected resistance map were calculated using the Matthews correlation coefficient  $C = \frac{(TP \times TN) - (FP \times FN)}{\sqrt{(TP+FP) \times (TP+FN) \times (TN+FN) \times (TN+FP)}}$  (Equation 3, in which TP is true positive, FP is false positive, TN is true negative, and FN is false negative). We also evaluated how this correlation changed as a function of growth threshold ([Fig 4C](#)). We found that for this particular strain (CIET-001), when a growth threshold of half doubling was considered, waiting 3 h or longer was enough to precisely reproduce the MIC values we obtained by 24 h incubation. Therefore, for consistency and improved accuracy, we set the growth threshold to one doubling ([Fig 4A](#), dashed horizontal red lines,  $OD > 4 \times 10^{-3}$ ) and incubation time to 4 h. Clinical isolates (CIET-002 to CIET-010) were tested by taking single measurements after 4 h of incubation. The correlation coefficient is 1.00 (perfect correlation) for 7 strains tested, with the remaining 3 isolates exceeding 0.9 ([Fig 4C, right panel](#)). Growth map for all 10 strains in ([S5 Fig](#)) shows the robustness with only 4 false positive (out of 950 measurements) reads. The complete MIC information for the 10 clinical isolates obtained with iFAST is provided in [Table 1](#). Entries underlined and marked bold indicate disagreements with the clinical data. For example, we found the MIC for ampicillin for the CIET-10 strain as  $>16 \mu\text{g/mL}$ , whereas the clinical report suggested that it was  $\le 16 \mu\text{g/mL}$ . The breakpoint (BP) value for ampicillin for

![Figure 3: iFAST yields antibiotic resistance profile of pathogenic bacteria in 1 to 3 h. The figure is divided into two main sections, (a) and (b), each showing heatmaps and dose-response curves for different bacterial strains and antibiotics.](a71911ad87414271aeb190e0eebcb989_img.jpg)

**Section (a):** Time-resolved dose-response measurements for laboratory strains.

- P. aeruginosa* (PA01) treated with Levofloxacin. Heatmap shows growth over 270 minutes at Levofloxacin concentrations of 0, 0.01, 0.03, 0.05, 0.15, and 0.45  $\mu\text{g/ml}$ . A dose-response curve at  $t=60$  minutes shows a sharp drop in OD at 0.05  $\mu\text{g/ml}$ .
- E. coli* (MG1655) treated with Levofloxacin. Heatmap shows growth over 270 minutes. A dose-response curve at  $t=90$  minutes shows a sharp drop in OD at 0.05  $\mu\text{g/ml}$ .
- S. aureus* (RN4220) treated with Levofloxacin. Heatmap shows growth over 270 minutes. A dose-response curve at  $t=120$  minutes shows a sharp drop in OD at 0.05  $\mu\text{g/ml}$ .

**Section (b):** Time-resolved dose-response measurements for a clinical *E. coli* isolate (ET-CI28).

- Treated with Levofloxacin. Heatmap shows growth over 270 minutes. A dose-response curve at  $t=90$  minutes shows a sharp drop in OD at 0.05  $\mu\text{g/ml}$ .
- Treated with P-T (piperacillin-tazobactam). Heatmap shows growth over 270 minutes. A dose-response curve at  $t=90$  minutes shows a sharp drop in OD at 10  $\mu\text{g/ml}$ .
- Treated with Amikacin. Heatmap shows growth over 270 minutes. A dose-response curve at  $t=150$  minutes shows a sharp drop in OD at 10  $\mu\text{g/ml}$ .

Heatmaps: The y-axis represents Time (min) from 0 to 270. The x-axis represents Antibiotic concentration ( $\mu\text{g/ml}$ ). The color scale represents OD (optical density) on a logarithmic scale from  $10^{-7}$  (white) to  $10^{-2}$  (dark blue). Red diamonds indicate MIC values. Dose-response curves: The y-axis represents OD on a logarithmic scale from  $10^{-7}$  to  $10^{-5}$ . The x-axis represents Antibiotic concentration ( $\mu\text{g/ml}$ ). The curves show the OD over time for different concentrations. LOQ (limit of quantification) is indicated by a dashed magenta line at  $10^{-6}$  OD.

Figure 3: iFAST yields antibiotic resistance profile of pathogenic bacteria in 1 to 3 h. The figure is divided into two main sections, (a) and (b), each showing heatmaps and dose-response curves for different bacterial strains and antibiotics.

**Fig 3. iFAST yields antibiotic resistance profile of pathogenic bacteria in 1 to 3 h.** Bacterial cultures with initial OD of approximately  $10^{-6}$  were grown in different concentrations of antibiotics, and their densities were periodically monitored in RUSD. Heat map plots show growth of bacteria as a function of time and antibiotic dosage. Colored bars indicate ODs of bacterial cultures. Red diamonds indicate MIC values measured at different time points at which bacterial growth is statistically significant ( $\text{OD} > \text{LOQ}$ ). Below each heat map plot, a dose-response curve is provided for the first statistically significant MIC measurement. A calibration curve is generated for every strain before every measurement, and LOQ values are shown by using dashed magenta lines. (a) Time-resolved dose-response measurements for laboratory strains of *P. aeruginosa* (PA01), *E. coli* (MG1655), and *S. aureus* (RN4220) in levofloxacin, a DNA gyrase inhibitor. (b) Time-resolved dose-response measurements for a clinical *E. coli* isolate (ET-CI28) in levofloxacin, P-T (a beta-lactam cell-wall synthesis inhibitor and beta-lactamase inhibitor), and amikacin (an aminoglycoside). (The data for Fig 3 can be found in [S2 Data](#)). iFAST, in Fiber Antibiotics Susceptibility Testing; LOQ, limit of quantification; MIC, minimum inhibitory concentration; OD, optical density; P-T, piperacillin-tazobactam; RUSD, rapid ultrasensitivity detector.

<https://doi.org/10.1371/journal.pbio.3000291.g003>

Table 1. MIC values obtained by iFAST and a standard clinical assay.

| Drug<br>(MIC values are<br>in µg/mL) | Abbreviation | Breakpoint*  | CIET-1                        | CIET-2                        | CIET-3                        | CIET-4                        | CIET-5                        | CIET-6             | CIET-7             | CIET-8                        | CIET-9                        | CIET-10                       |
|--------------------------------------|--------------|--------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|-------------------------------|--------------------|--------------------|-------------------------------|-------------------------------|-------------------------------|
| Source                               |              |              | Urinary<br>tract<br>infection | Urinary<br>tract<br>infection | Urinary<br>tract<br>infection | Urinary<br>tract<br>infection | Urinary<br>tract<br>infection | Blood<br>infection | Blood<br>infection | Urinary<br>tract<br>infection | Urinary<br>tract<br>infection | Urinary<br>tract<br>infection |
| Ampicillin                           | Am           | <b>8</b>     | >16                           | >16                           | >16                           | >16                           | >16                           | >16                | >8                 | >16                           | >16                           | <b>&gt;16<br/>(≤16)</b>       |
| Amoxicillin/<br>clavulanic acid      | Aug          | ND           | ≤8/4                          | ≤16/8                         | ≤8/4                          | ≤16/8                         | ≤8/4                          | >16/8              | >16/8              | ≤16/8                         | ≤16/8                         | >16/8                         |
| Cefazolin                            | Cfz          | ND           | ≤2                            | ≤4                            | ≤2                            | ≤16                           | >16                           | >16                | >16                | >16                           | >16                           | >16                           |
| Ampicillin/<br>subactam              | A/S          | <b>8</b>     | >16/8                         | >16/8                         | ≤4/2                          | >16/8                         | ≤8/4                          | >16/8              | >16/8              | ≤8/4                          | >16/8                         | >16/8                         |
| Aztreonam                            | Azt          | <b>0.25</b>  | ≤4                            | ≤4                            | ≤4                            | ≤4                            | >16                           | >16                | >16                | >16                           | ≤4                            | >16                           |
| Ceftriaxone                          | Cax          | <b>0.125</b> | ≤1                            | ≤1                            | ≤1                            | ≤1                            | >32                           | >32                | >32                | >32                           | ≤1                            | >32                           |
| Cephatholin                          | Cf           | <b>32</b>    | >16                           | >16                           | ≤8                            | ≤8                            | ≤8                            | ≤8                 | ≤8                 | ≤8                            | ≤8                            | ≤8                            |
| Cefotaxime                           | Cft          | <b>0.25</b>  | ≤2                            | ≤2                            | ≤2                            | ≤2                            | <b>&gt;32<br/>(≤16)</b>       | ≤2                 | ≤2                 | ≤2                            | >32                           | >32                           |
| Cefotixin                            | Cfx          | <b>8</b>     | ≤4                            | ≤4                            | ≤4                            | ≤4                            | ≤4                            | ≤4                 | ≤4                 | ≤4                            | ≤4                            | ≤4(>16)                       |
| Amikacin                             | Ak           | <b>8</b>     | ≤8                            | ≤8                            | ≤8                            | ≤8                            | ≤8                            | ≤8                 | ≤8                 | ≤8                            | ≤8                            | ≤8                            |
| Cefotaxime/<br>clavulanic acid       | Cft/CA       | <b>0.25</b>  | ≤0.5/4                        | ≤0.5/4                        | ≤0.5/4                        | ≤0.5/4                        | ≤0.5/4                        | ≤0.5/4             | ≤0.5/4             | ≤0.5/4                        | ≤0.5/4                        | ≤0.5/4                        |
| Cefepime                             | Cpe          | <b>0.25</b>  | ≤2                            | ≤2                            | ≤2                            | ≤2                            | >16                           | >16                | >16                | >16                           | ≤2                            | >16                           |
| Cefuroxime                           | Crm          | <b>8</b>     | ≤8                            | ≤4                            | ≤4                            | ≤4                            | >16                           | >16                | >16                | >16                           | ≤4                            | >16                           |
| Tobramycin                           | To           | <b>2</b>     | ≤2                            | ≤2                            | ≤2                            | ≤2                            | >8                            | ≤2                 | ≤2                 | >8                            | ≤2                            | ≤4                            |
| Ceftazidime                          | Caz          | <b>0.5</b>   | ≤1                            | ≤1                            | ≤1                            | ≤1                            | <b>&gt;16(&gt;8)</b>          | ≤8                 | ≤8                 | ≤8                            | <b>&gt;16(≤1)</b>             | ≤1                            |
| Piperacillin/<br>tazobactam          | P/T          | <b>8</b>     | ≤8                            | ≤8                            | ≤8                            | ≤32                           | ≤8                            | ≤16                | ≤8                 | ≤8                            | ≤32                           | >64                           |
| Gentamicin                           | Gm           | <b>2</b>     | ≤1                            | ≤1                            | ≤1                            | >8                            | >8                            | ≤1                 | ≤1                 | >4                            | ≤1                            | >4                            |
| Ceftazidime/<br>clavulanic acid      | Caz/CA       | <b>0.5</b>   | ≤0.25/4                       | ≤0.25/4                       | ≤0.25/4                       | ≤0.25/4                       | ≤0.25/4                       | ≤0.25/4            | ≤0.25/4            | ≤0.25/4                       | ≤0.25/4                       | >2/4                          |
| Ciprofloxacin                        | Cp           | <b>0.064</b> | ≤0.5                          | >2                            | >2                            | ≤0.5                          | >2                            | >2                 | ≤1                 | >2                            | ≤0.5                          | >2                            |
| Levofloxacin                         | Lvx          | <b>0.25</b>  | ≤1                            | >4                            | >4                            | ≤1                            | >4                            | ≤1                 | ≤1                 | ≤4                            | ≤1                            | ≤4                            |
| Moxifloxacin                         | Mxf          | <b>0.25</b>  | ≤2                            | >4                            | >4                            | ≤2                            | >4                            | ≤2                 | ≤2                 | >4                            | ≤2                            | ≤2                            |
| Nitrofurantoin                       | Fd           | <b>64</b>    | ≤32                           | ≤32                           | ≤32                           | ≤32                           | ≤32                           | ≤32                | ≤32                | ≤32                           | ≤32                           | ≤32                           |
| Piperacillin                         | Pi           | <b>8</b>     | ≤16                           | >64                           | >64                           | >64                           | >64                           | >64                | >64                | >64                           | >64                           | >64                           |
| Tetracycline                         | Te           | <b>8</b>     | ≤2                            | >8                            | ≤2                            | >8                            | >8                            | ≤2                 | ≤2                 | ≤2                            | ≤2                            | ≤8                            |
| Tigecycline                          | Tgc          | <b>0.5</b>   | ≤1                            | ≤1                            | ≤1                            | ≤1                            | ≤1                            | ≤1                 | ≤1                 | ≤1                            | ≤1                            | ≤1                            |
| Trimethoprim/<br>sulfamethoxazole    | T/S          | <b>1</b>     | ≤0.5/9.5                      | >2/38                         | ≤0.5/9.5                      | >2/38                         | ≤0.5/9.5                      | >2/38              | >2/38              | ≤0.5/9.5                      | >2/38                         | >2/38                         |
| Imipenem                             | Imp          | <b>0.5</b>   | ≤1                            | ≤1                            | ≤1                            | ≤1                            | ≤1                            | ≤1                 | ≤1                 | ≤1                            | ≤1                            | ≤1                            |
| Meropenem                            | Mer          | <b>0.125</b> | ≤1                            | ≤1                            | ≤1                            | ≤1                            | ≤1                            | ≤1                 | ≤1                 | ≤1                            | ≤1                            | ≤1                            |
| Ertapenem                            | Etp          | ND           | ≤0.5                          | ≤0.5                          | ≤0.5                          | ≤0.5                          | ≤0.5                          | ≤0.5               | ≤0.5               | ≤0.5                          | ≤0.5                          | ≤1(≤2)                        |

For a set of 29 antibiotics and/or antibiotic combinations. Bold and underlined text indicates the 4 cases in which iFAST indicated higher MIC concentrations than expected from the data (given in parenthesis).

\*Breakpoint values are obtained from EUCAST MIC database.

Abbreviations: iFAST, in Fiber Antibiotics Susceptibility Testing; MIC, minimum inhibitory concentration; ND, no data.

<https://doi.org/10.1371/journal.pbio.3000291.t001>

![Figure 4: iFAST yields reliable results in shorter times in comparison to standard commercial clinical antibiotic susceptibility testing. (a) Utilizing the high sensitivity of the RUSD platform, iFAST can track growth of clinical isolates starting from the initial OD = 2 x 10^-3 in antibiotic susceptibility test panels (NM43, Beckman Coulter). Cell densities of a clinical E. coli isolate (CIET-001) growing in 16 antibiotic panels are shown. (b) Comparison of Expected vs Observed growth patterns. (c) Correlation analysis for different growth thresholds.](7801d00a216dc4dc8a7d210dcb5fe3c5_img.jpg)

**(a) Growth Tracking**

OD (Y-axis,  $10^{-3}$  to  $10^{-2}$ ) vs Time (h) (X-axis, 0 to 8). Panels show growth for various antibiotics: Neg Contr., No Drug, Am 2, Am 4, Am 8, Am 16, Aug 8/4, Aug 16/8, Cfx 2, Cfx 4, Cfx 8, Cfx 16, Cfx 32, Cfx 16, Cfx 16, A/S 4/2, A/S 8/4, A/S 16/8, Azt 4, Azt 8, Azt 16, Cax 1, Cax 2, Cax 8, Cax 32, Cft 2, Cft 4, Cft 8, Cft 16, Cft 32, Cfx 4, Cfx 8, Cfx 16, LOC, Ak 8, Ak 16, Ak 32, Cft/CA 0.5/4, Cft/CA 4/4, Cpe 2, Cpe 4, Cpe 8, Cpe 16, Crm 4, Crm 8, Crm 16, To 2, To 4, To 8, Caz 1, Caz 2, Caz 8, Caz 16, P/T 8, P/T 16, P/T 32, P/T 64, Gm 1, Gm 2, Gm 4, Gm 8, Caz/CA 0.25/4, Caz/CA 2/4, Cp 0.5, Cp 1, Cp 0.2, Lvx 1, Lvx 2, Lvx 4, Mxf 2, Mxf 4, Fd 32, Fd 64, Pi 16, Pi 32, Pi 64, Te 2, Te 4, Te 8, Tgc 1, Tgc 2, Tgc 4, T/S 0.5/9.5, T/S 1/9, T/S 2/38, Imp 1, Imp 2, Imp 4, Imp 8, Mer 1, Mer 2, Mer 4, Mer 8, Etp 0.5, Etp 1, Etp 2, Etp 4.

**(b) Comparison of Expected vs Observed**

Legend: No growth = 0 (white square), Growth = 1 (blue square).

Observed vs Expected grid (A-H, 1-12):

| Observed \ Expected | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---------------------|---|---|---|---|---|---|---|---|---|----|----|----|
| A                   | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1  | 1  | 1  |
| B                   | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1  | 1  | 1  |
| C                   | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1  | 1  | 1  |
| D                   | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1  | 1  | 1  |
| E                   | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1  | 1  | 1  |
| F                   | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1  | 1  | 1  |
| G                   | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1  | 1  | 1  |
| H                   | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1  | 1  | 1  |

Observed vs Expected summary:

| Observed \ Expected | 85 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
|---------------------|----|---|---|---|---|---|---|---|---|---|---|---|
| A                   | 85 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| B                   | 85 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| C                   | 85 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| D                   | 85 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| E                   | 85 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| F                   | 85 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| G                   | 85 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| H                   | 85 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Legend: NoGrw (white), Grow (blue).

**(c) Correlation Analysis**

Correlation =  $\frac{(TP \times TN) - (FP \times FN)}{\sqrt{(TP+FP) \times (TP+FN) \times (TN+FP) \times (TN+FN)}}$

Correlation vs Time (h) (0 to 10) for three growth thresholds:

- Growth=1 if  $OD > (OD_{init} \times 1.5)$  (Half Doubling)
- Growth=1 if  $OD > (OD_{init} \times 2)$  (One Doubling)
- Growth=1 if  $OD > (OD_{init} \times 4)$  (Two Doublings)

Correlation vs Clinical Isolates (CIET) (1 to 10) for the Two Doublings threshold.

Figure 4: iFAST yields reliable results in shorter times in comparison to standard commercial clinical antibiotic susceptibility testing. (a) Utilizing the high sensitivity of the RUSD platform, iFAST can track growth of clinical isolates starting from the initial OD = 2 x 10^-3 in antibiotic susceptibility test panels (NM43, Beckman Coulter). Cell densities of a clinical E. coli isolate (CIET-001) growing in 16 antibiotic panels are shown. (b) Comparison of Expected vs Observed growth patterns. (c) Correlation analysis for different growth thresholds.

**Fig 4. iFAST yields reliable results in shorter times in comparison to standard commercial clinical antibiotic susceptibility testing methods.** (a) Utilizing the high sensitivity of the RUSD platform, iFAST can track growth of clinical isolates starting from the initial  $OD = 2 \times 10^{-3}$  in antibiotic susceptibility test panels (NM43, Beckman Coulter). Cell densities of a clinical *E. coli* isolate (CIET-001) growing in

different doses of 29 antibiotic compounds were periodically recorded at hourly intervals. Cell densities exceeding the growth threshold ( $4 \times 10^{-3}$ , horizontal red dashed lines, one doubling) are shown in green filled circles. Cell densities lower than the threshold are shown in gray filled circles. (b) Growth information was converted to a binary resistance map for the test panel, in which blue and white indicate growth and no growth in a given well, respectively. The Matthews correlation coefficient is calculated using the true–false matrix between observed and expected resistance data. (c) Correlation coefficient between iFAST measurements and clinical data changes as a function of growth threshold and hovers to acceptable levels as incubation times increase. For consistency and reliability purposes, we chose a 4 h incubation time and threshold of one population size doubling for the rest of the clinical *E. coli* strains. (Right panel) Histogram showing the correlations between iFAST measurements and clinical reports demonstrate the accuracy and power of the iFAST assay. (The data for Fig 4 can be found in [S3 Data](#)). Ak, amikacin; Am, ampicillin; A/S, ampicillin/sulbactam; Aug, amoxicillin/clavulanic acid; Azl, aztreonam; CA, clavulanic acid; Cax, ceftriaxone; Caz, ceftazidime; Cf, cephalothin; Cft, cefotaxime; Cfz, cefazolin; Cp, ciprofloxacin; Cpe, cefepime; Crm, cefuroxime; Etp, ertapenem; Fd, nitrofurantoin; FN, false negative; FP, false positive; Gm, gentamicin; iFAST, in Fiber Antibiotics Susceptibility Testing; Imp, imipenem; LOQ, limit of quantification; Lvx, levofloxacin; Mer, meropenem; Mxf, moxifloxacin; Neg Contr., negative control; OD, optical density; Pi, piperacillin; P/T, piperacillin/tazobactam; RUSD, rapid ultrasensitivity detector; Te, tetracycline; Tge, tigecycline; TN, true negative; To, tobramycin; TP, true positive; T/S, trimethoprim/sulfamethoxazole.

<https://doi.org/10.1371/journal.pbio.3000291.g004>

*E. coli* is 8  $\mu\text{g/mL}$ . Since the AST panel we used cannot determine the exact MIC for ampicillin at this point, the discrepancy for this case might be considered as minor, as both tests indicate some resistance against ampicillin. In 5 other cases in which there are discrepancies between the NM-43 AST panel and iFAST, the errors for the cases of cefotaxime (BP = 0.25  $\mu\text{g/mL}$ , iFAST MIC > 32  $\mu\text{g/mL}$ , and NM-43 MIC  $\le$  16  $\mu\text{g/mL}$ ), cefoxitin (BP 4  $\mu\text{g/mL}$ , iFAST MIC  $\le$  4  $\mu\text{g/mL}$ , and NM-43 MIC > 16  $\mu\text{g/mL}$ ), ceftazidime (BP 0.25  $\mu\text{g/mL}$ , iFAST MIC > 16  $\mu\text{g/mL}$ , and NM-43 MIC > 8  $\mu\text{g/mL}$  [CIET-5],  $\le$  1  $\mu\text{g/mL}$  [CIET-9]) could be classified as major errors. In the last case of ertapenem, we found an MIC  $\le$  1 versus  $\le$  2 by the plate method; however, the EUCAST system does not indicate a BP value for this drug. These differences might be due to experimental error or better sensitivity of our system. Finally, none of our measurements yielded false negative (FN) measurements when we missed growth of a bacterial strain in a drug condition in which it was expected to grow. These findings further articulate the power of the RUSD platform and the iFAST assay.

## Discussion

The RUSD platform is a rapid, label-free, highly sensitive, and low-cost optical detection system that could be used as a field-deployable device. RUSD can detect about as few as 20–25 bacterial cells and a single fungal cell. RUSD can detect bacterial growth in less than an hour and quantitatively measure antibiotic susceptibility of pathogenic bacteria within 2 to 4 h using both small and large inoculum sizes. However, the use of RUSD will be particularly advantageous in cases for which the number of bacterial cells available are limited. RUSD can also be utilized to monitor contaminations in water or other fluids. In contrast to present technologies [10–12], RUSD can be easily assembled with readily available materials at a cost of about US\$25 per device and a simple voltmeter device. In comparison to imaging-based or spectroscopic techniques, RUSD has higher throughput with higher sensitivity, without the need for image or signal processing. Here, we demonstrate RUSD as a viable platform that may be implemented into the current clinical framework of AST standards. Furthermore, the RUSD platform is amenable to technological modifications such as integration of advanced microfluidic and particle separation systems and portable electronics. The simplicity and the low-cost nature of RUSD will make it a viable diagnostic platform that can be employed in laboratories, hospitals, and industry.

## Materials and methods

### RUSD

RUSD is built around a hollow fused-silica optical fiber (500  $\mu\text{m}$  diameter, 50–400 mm length, P.N. 25739 Supelco,  $n_1$  = 1.458). The hollow fiber is capped with a polydimethylsiloxane

(PMDS)-glass assembly at both ends, each of which has a cavity cast using a small glass bead, connecting the hollow fiber and fluid inlet/outlet channels at 90° (Fig 1A). One side of the cavity in the PDMS layer is covered with a 1 mm thick soda lime glass, which creates a direct optical access into the fiber. The optical setup components include a 650 nm laser diode assembly with a focusing lens (5 mW, P. N. 0710893–000, AixiZ, Amazon.com) and a silicon photodiode (Digi-key 1080-1148-ND) as the detector. The current output from the detector is converted to voltage readings, which are recorded using a data acquisition card (DAQ card; MCC, 1408 HS) or a simple voltmeter and processed by a custom Matlab code. Code used for data acquisition is available on request. For the measurements with DAQ card, voltage is typically measured at 1,000 Hz sampling. Voltage is recorded for 10 s, and the median of these readings is used for OD measurements.

### Bacterial and fungal strains

Ten strains of *E. coli* (CIET-001 to CIET-010) isolated from pediatric patients (Children's Medical Center, Dallas, TX, United States), 2 laboratory strains of *E. coli* (MG1655 and BW25113), a pan-sensitive clinical *E. coli* strain (ET-CI28) isolated from a pediatric patient, a laboratory strain of *P. aeruginosa* (PAO1, courtesy of Greenberg Lab, UTSW), and a laboratory strain of *S. aureus* (RN4220, courtesy of Marrafini Lab, Rockefeller University) were used in this study. Fungal strains used in this study were *C. glabrata* (ATCC 18126) and *S. cerevisiae* (S288c, courtesy of Springer Lab, Harvard Medical School).

### Calculating LOQ and LOD

For all cell density detection devices (including RUSD), we calculated LOD and LOQ values. Briefly, by measuring the corresponding OD or voltage readings for serially diluted cell cultures with known ODs and of multiple known blank media samples that contain no particles and/or cells, we generated calibration curves and identified LOD, which is the first data point with cells, where the measurement is significantly higher than the blank reading for LB media with no cells and can be reliably distinguished from the blank and at which detection is achievable. LOD was typically about 0.007 for our plate reader, about 0.002 for our spectrophotometer, and  $5 \times 10^{-7}$  for RUSD. These values improved slightly when a more transparent media was used. LOQ is the lowest concentration at which the cells can not only be reliably detected but at which our detection devices start responding proportionately with the sample density. LOQ was typically about 0.02 for our plate reader, about 0.006 for our spectrophotometer, and  $1.5 \times 10^{-6}$  for RUSD.

### Data analysis workflow

Voltage readings for serially diluted cell cultures with known ODs for the strain and media at hand were measured. Then, the recorded sample voltage was subtracted from the blank measurement voltage to obtain  $\Delta V$  with respect to a blank measurement medium. This procedure was repeated for actual sample measurements. A calibration curve was plotted, and a  $\Delta V$  to  $OD_{600}$  conversion function was generated using log-log regression. The LOD and LOQ were also calculated in this step using the log-log regression model and the recorded blank measurements. After running the samples through the device and collecting the voltage measurements, we converted the readings to corresponding  $OD_{600}$  using the conversion function. Then, any measurements below the LOQ were discarded to ensure that the analysis is based solely on statistically significant data.

### Cell counting with RUSD

Bacterial and fungal cells were diluted down to ODs nearly  $10^{-6}$ , which approximates the LOD for RUSD. RUSD is first blanked with growth media (LB for bacteria; yeast extract–peptone–dextrose [YPD] or yeast synthetic complete media for fungal cells). We then manually flow-diluted cell cultures and recorded corresponding OD values using RUSD. OD values were then converted to cell numbers using the following OD-to-CFU conversion factors: OD<sub>600</sub> of 1 corresponded to approximately  $5 \times 10^8$  CFU/mL for *E. coli*, approximately  $2.2 \times 10^7$  CFU/mL for *S. cerevisiae*, and approximately  $1.25 \times 10^7$  CFU/mL for *C. glabrata*. Finally, calculated cell numbers were rounded to the closest integer. At very low cell densities approaching LOD, 5%–10% of the readings gave negative values such as –1 or –2, which we attributed to measurement noise or variability in blank measurements. These values were assumed to be zero in cell count histograms. Negative cell count values were not observed when cell densities were increased.

### Bacterial lag-time measurements

Isogenic bacterial cells were grown overnight in LB (RPI L24040-500.0) at 37°C with continuous shaking (220 rpm). OD (OD<sub>600</sub>) values for the overnight cultures were measured using a spectrophotometer (Eppendorf BioSpectrometer). Overnight bacterial cultures were serially diluted down to a cell density of  $10^{-6}$  (OD<sub>600</sub>) in LB growth media in 96-well plates (12 replicates, 200  $\mu$ L volume in each well), and cells were in an automated (temperature and humidity controlled) Tecan robotic system at 37°C with continuous shaking (about 200 rpm) for 24 h. OD of growing bacterial cultures was recorded approximately every 10 min. Lag times necessary for the cultures to reach OD<sub>600</sub> of 0.02, the LOQ for our plate reader (Tecan Infinite M200), were calculated using a custom Matlab code. Code used for the analysis is available on request.

### AST for bacteria

Isogenic bacterial cells were grown overnight in LB at 37°C with continuous shaking (220 rpm), diluted to a final density of (OD<sub>600</sub>)  $10^{-6}$  in 96-well plates, and grown in an increasing range of antibiotic concentrations. OD of these cultures was periodically (every 10–12 min) recorded by a plate reader (Tecan Infinite M200). Time-resolved dose-response curves were generated using OD readings. ODs that were significantly larger than 0.02 (Student *t* test, *p* < 0.05) were considered as growth for MIC calculations. Corresponding dose-response curves were analyzed for predicting MIC values using a custom Matlab code [13]. Antibiotics used for this study are levofloxacin (Alfa Aesar J66943), amikacin (Alfa Aesar J63862), and P-T (Apotex Corp #763).

#### iFAST

Isogenic bacterial cells were grown overnight in LB at 37°C with continuous shaking (220 rpm) and were diluted to a final density of (OD<sub>600</sub>)  $10^{-6}$  in glass flasks. These cultures were typically split into 6 subcultures (150 mL volume, LB media), and antibiotic solutions were added to each culture such that predicted MIC values were spanned across the flasks. Flasks were continuously shaken at 220 rpm at 37°C in a commercial shaker. Samples (approximately 1 mL) were periodically taken from each culture every 30 min, and cell densities of bacterial cultures were recorded by RUSD and a spectrophotometer for comparison. Corresponding dose-response curves were analyzed for predicting MIC values using a custom Matlab code [13]. Code used for the analysis is available on request. LOQ and LOD were calculated for

every experiment, and ODs that were significantly larger than LOQ (Student *t* test,  $p < 0.05$ ) were considered as growth for MIC calculations. A calibration measurement was done before each iFAST test in order to calculate LOQ and LOD values.

#### Clinical AST for bacteria using a commercial antibiotic panel

Clinical isolates were plated from  $-80^{\circ}\text{C}$  stocks overnight on LB agar. Using a 1  $\mu\text{l}$  inoculation loop, 5–6 isolated colonies were collected from the overnight plate. The bacterial mass was emulsified in 3 mL of sterile inoculum water (Beckmann Coulter B1015-2) by vortexing. Per the clinical standards, the final turbidity is adjusted to the equivalent of 0.5 McFarland standard, which corresponds to  $\text{OD}_{600} = 0.25$  for *E. coli*. The standardized suspension (0.1 mL, or 100  $\mu\text{l}$ ) was transferred into 25 mL of inoculum water with PLURONIC (Beckmann Coulter B1015-7). The resulting inoculum was transferred into NM43 antibiotic susceptibility panel (by Beckmann Coulter B1017-420), with 0.2 mL in each well. The panels were covered with lids and incubated at  $37^{\circ}\text{C}$  without shaking in a humidified environment following instructions provided with the NM43 panels. The plates were visually checked 24 hr after inoculation per Beckman Coulter NM43 guidelines.

#### Clinical AST for bacteria with NM43 MIC panel by iFAST

The bacterial response to the antibiotics on the NM43 panels were tracked using RUSD at hourly intervals. In order to track the susceptibility through a 10 h period, 10 panels were inoculated as described above and simultaneously started incubation. At the end of each interval, background and base signal levels were recorded. For the rest of the iFAST measurements, bacteria were grown in NM43 panels for 4 h, and cell densities were measured using RUSD. Cell densities exceeding  $4 \times 10^{-3}$  OD were considered to be positive for growth. In between each measurement, RUSD was flushed with DI water in order to avoid contamination and false positive measurements.

## Supporting information

**S1 Fig. Calibration measurements for RUSD.** (a) Calibration measurements for *E. coli*, *S. aureus*, *P. aeruginosa*, and *S. cerevisiae*. (b) LOD (red dashed lines) and LOQ (blue dashed lines) of RUSD for a typical bacterial measurement. (b) Bacterial growth track of *E. coli* MG1655 at  $37^{\circ}\text{C}$  LB between  $\text{OD} = 1 \times 10^{-5}$  and  $\text{OD} = 2 \times 10^{-3}$ . (The data for S1 Fig can be found in S4 Data). LB, lysogeny broth; LOD, limit of detection; LOQ, limit of quantification; OD, optical density; RUSD, rapid ultrasensitivity detector. (TIF)

**S2 Fig. Lag time as a function of inoculum size.** Lag time before any statistically significant growth as a function of inoculum size for *P. aeruginosa* (PA01), *S. aureus* (RN4220), *E. coli* (MG1655), and clinical isolate *E. coli* (ET-CI28). (The data for S2 Fig can be found in S5 Data) (TIF)

**S3 Fig. Microbroth dilution assays to measure the first MIC values.** Microbroth dilution assays performed using an automated robotic platform requires 7 to 14 h to yield the first MIC value. (a) Dose-response curves of levofloxacin for *P. aeruginosa*, *S. aureus*, and *E. coli*. (b) Comparison of dose-response curves of levofloxacin, amikacin, and piperacillin-tazobactam for *E. coli*. (The data for S3 Fig can be found in S6 Data). MIC, minimum inhibitory concentration. (TIF)

**S4 Fig. MIC determination time comparisons of RUSD and plate reader.** MIC determination time comparisons of RUSD and plate reader for (a) amikacin (ET-CI28) and (b) piperacillin-tazobactam (BW25113). (The data for [S4 Fig](#) can be found in [S7 Data](#)). MIC, minimum inhibitory concentration; RUSD, rapid ultrasensitivity detector. (TIF)

**S5 Fig. Antibiotic susceptibility tests of clinical isolates using iFAST.** Clinical isolates (CIET-001 to CIET-010) from  $-80^{\circ}\text{C}$  stocks were plated on LB agar. Using a 1  $\mu\text{l}$  inoculation loop, 5–6 colonies were collected and were emulsified in 3 mL of sterile inoculum water (Beckmann coulter B1015-2). The concentration was adjusted to OD = 0.2. The standardized suspension (100  $\mu\text{l}$ ) was transferred into 25 mL of inoculum water with PLURONIC (Beckmann Coulter B1015-7). The resulting inoculum was transferred into NM43 Antibiotic Susceptibility MIC Panel by Beckmann coulter, with 0.2 mL in each well. The panels were incubated at  $37^{\circ}\text{C}$  without shaking in a humidified environment. iFAST measurements were done after a 4 hr incubation period. In between each measurement, RUSD was flushed with sterile water in order to eliminate contamination. For each isolate, a resistance map was created and was compared to the expected resistance map by calculating Matthews correlation coefficient as described in the main text. (The data for [S5 Fig](#) can also be found in [S3 Data](#)). iFAST, in Fiber Antibiotics Susceptibility Testing; LB, lysogeny broth; MIC, minimum inhibitory concentration; OD, optical density; RUSD, rapid ultrasensitivity detector. (TIF)

**S1 Movie. Progress of microbroth dilution assays to measure the first MIC values.** MIC, minimum inhibitory concentration. (MOV)

**S1 Data. Data file for [Fig 2](#): Low bacterial and fungal cell counts taken by RUSD.** RUSD, rapid ultrasensitivity detector. (XLSM)

**S2 Data. Data file for [Fig 3](#): Heat map plots of bacterial growth as a function of time and antibiotic dosage.** (XLSM)

**S3 Data. Data file for [Fig 4](#) for growth track of clinical isolates using iFAST in antibiotic susceptibility test panels.** iFAST, in Fiber Antibiotics Susceptibility Testing. (XLSM)

**S4 Data. Data for [S1 Fig](#). Calibration measurements for RUSD.** RUSD, rapid ultrasensitivity detector. (XLSM)

**S5 Data. Data for [S2 Fig](#). Lag time as a function of inoculum size.** (XLSM)

**S6 Data. Data for [S3 Fig](#). Microbroth dilution assays to measure the first MIC values.** MIC, minimum inhibitory concentration. (XLSM)

**S7 Data. Data for [S4 Fig](#).** Antibiotic susceptibility tests of clinical isolates using iFAST. iFAST, in Fiber Antibiotics Susceptibility Testing. (XLSM)

## Acknowledgments

We thank Dr. Laura Filkins from the Department of Pathology, University of Texas South-western Medical Center, Dallas, Texas, for providing the clinical isolates and reagents used in this study as well as technical expertise on the clinical antibiotic susceptibility tests performed. We also thank Marinelle Rodrigues and Laura Coughlin for technical help and advice.

## Author Contributions

**Conceptualization:** Mehmet F. Cansizoglu, Erdal Toprak.

**Formal analysis:** Mehmet F. Cansizoglu, Yusuf Talha Tamer, Michael Farid.

**Funding acquisition:** Erdal Toprak.

**Investigation:** Erdal Toprak.

**Methodology:** Mehmet F. Cansizoglu, Erdal Toprak.

**Project administration:** Erdal Toprak.

**Software:** Yusuf Talha Tamer, Michael Farid.

**Supervision:** Erdal Toprak.

**Validation:** Yusuf Talha Tamer, Andrew Y. Koh, Erdal Toprak.

**Writing – original draft:** Mehmet F. Cansizoglu, Erdal Toprak.

**Writing – review & editing:** Mehmet F. Cansizoglu, Andrew Y. Koh, Erdal Toprak.

## References

1. Lv X, Ge W, Li Q, Wu Y, Jiang H, Wang X. Rapid and ultrasensitive electrochemical detection of multi-drug-resistant bacteria based on nanostructured gold coated ITO electrode. *Acs Appl Mater Inter*. 2014; 6(14):11025–11031.
2. Besant JD, Sargent EH, Kelley SO. Rapid electrochemical phenotypic profiling of antibiotic-resistant bacteria. *Lab Chip*. 2015; 15(13):2799–2807. <https://doi.org/10.1039/c5lc00375j> PMID: 26008802
3. Verma MS, Tsujii JM, Hall B, Chen PZ, Forrest J, Jones L, Gu FX. Towards point-of-care detection of polymicrobial infections: rapid colorimetric response using a portable spectrophotometer. *Sensing and Bio-Sensing Research*. 2016; 10:15–19.
4. Yoo SM, Lee SY. Optical Biosensors for the Detection of Pathogenic Microorganisms. *Trends Biotechnol*. 2016; 34(1):7–25. <https://doi.org/10.1016/j.tibtech.2015.09.012> PMID: 26506111
5. Ahmed A, Rushworth JV, Hirst NA, Millner PA. Biosensors for Whole-Cell Bacterial Detection. *Clin Microbiol Rev*. 2014; 27(3):631–646. <https://doi.org/10.1128/CMR.00120-13> PMID: 24982325
6. Kalsi S, Valiadi M, Tsaloglou MN, Parry-Jones L, Jacobs A, Watson R, Turner C, Amos R, Hadwen B, Buse J, Brown C, Sutton M, Morgan H. Rapid and sensitive detection of antibiotic resistance on a programmable digital microfluidic platform. *Lab Chip*. 2015; 15(14):3065–3075. <https://doi.org/10.1039/c5lc00462d> PMID: 26086197
7. Shrivastava A, Gupta VB. Methods for the determination of limit of detection and limit of quantitation of the analytical methods. *Chronicles of Young Scientists*. 2011; 2(1):21.
8. Armbruster DA, Pry T. Limit of blank, limit of detection and limit of quantitation. *The Clinical Biochemist Reviews*. 2008; 29(Suppl 1):S49.
9. Liu C-Y, Han Y-Y, Shih P-H, Lian W-N, Wang H-H, Lin C-H, Hsueh P-R, Wang J-K, Wang Y-L. Rapid bacterial antibiotic susceptibility test based on simple surface-enhanced Raman spectroscopic biomarkers. *Sci Rep-Uk*. 2016; 6:23375.
10. Giordano C, Piccoli E, Brucculeri V, Barnini S. A Prospective Evaluation of Two Rapid Phenotypical Antimicrobial Susceptibility Technologies for the Diagnostic Stewardship of Sepsis. *Biomed Res Int*. 2018; 2018:6976923. <https://doi.org/10.1155/2018/6976923> PMID: 29862284
11. Marschal M, Bachmaier J, Autenrieth I, Oberhettinger P, Willmann M, Peter S. Evaluation of the Accelerate Pheno System for Fast Identification and Antimicrobial Susceptibility Testing from Positive Blood

Cultures in Bloodstream Infections Caused by Gram-Negative Pathogens. J Clin Microbiol. 2017; 55 (7):2116–2126. <https://doi.org/10.1128/JCM.00181-17> PMID: 28446572

12. Lupetti A, Barnini S, Castagna B, Nibbering PH, Campa M. Rapid identification and antimicrobial susceptibility testing of Gram-positive cocci in blood cultures by direct inoculation into the BD Phoenix system. Clin Microbiol Infect. 2010; 16(7):986–991. <https://doi.org/10.1111/j.1469-0691.2009.03006.x> PMID: 19681952
13. Toprak E, Veres A, Michel JB, Chait R, Hartl DL, Kishony R. Evolutionary paths to antibiotic resistance under dynamically sustained drug selection. Nat Genet. 2012; 44(1):101–105.