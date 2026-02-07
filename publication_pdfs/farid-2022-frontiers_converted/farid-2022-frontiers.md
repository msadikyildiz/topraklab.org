

![Check for updates icon](5fb340ad68b0c71df0b56698b137e35b_img.jpg)

Check for updates icon

# Label-Free Optical Detection of Pathogenic Bacteria and Fungi at Extremely Low Cell Densities for Rapid Antibiotic Susceptibility Testing

Michael Farid<sup>1†</sup>, Marinelle Rodrigues<sup>1†</sup>, Robert England<sup>2</sup> and Erdal Toprak<sup>1,3\*</sup>

<sup>1</sup>Department of Pharmacology, University of Texas Southwestern Medical Center, Dallas, TX, United States, <sup>2</sup>Independent Engineering and Technology Consultant, Dallas, TX, United States, <sup>3</sup>Lyda Hill Department of Bioinformatics, University of Texas Southwestern Medical Center, Dallas, TX, United States

###### OPEN ACCESS

###### Edited by:

Somenath Bakshi,  
University of Cambridge,  
United Kingdom

###### Reviewed by:

Jason H. Yang,  
The State University of New Jersey,  
United States

Abdelrahim H. A. Hassan,  
Beni-Suef University, Egypt

Rozhina Elvira,

Kazan Federal University, Russia

###### \*Correspondence:

Erdal Toprak

erdal.toprak@utsouthwestern.edu

<sup>†</sup>These authors share first authorship

###### Specialty section:

This article was submitted to

Nanobiotechnology,

a section of the journal

Frontiers in Bioengineering and  
Biotechnology

**Received:** 25 February 2022

**Accepted:** 14 June 2022

**Published:** 30 June 2022

###### Citation:

Farid M, Rodrigues M, England R and  
Toprak E (2022) Label-Free Optical  
Detection of Pathogenic Bacteria and  
Fungi at Extremely Low Cell Densities  
for Rapid Antibiotic  
Susceptibility Testing.  
*Front. Bioeng. Biotechnol.* 10:884200.  
doi: 10.3389/fbioe.2022.884200

Antibiotic resistance is a rapidly expanding public health problem across the globe leading to prolonged hospital admissions, increased morbidity and mortality, and associated high healthcare costs. Effective treatment of bacterial infections requires timely and correct antibiotic administration to the patients which relies on rapid phenotyping of disease-causing bacteria. Currently, antibiotic susceptibility tests can take several days and as a result, indiscriminate antibiotic use has exacerbated the evolution and spread of antibiotic resistance in clinical and community settings. In order to address this problem, we have developed a novel optical apparatus that we called RUSD (Rapid Ultra-Sensitive Detection). RUSD is built around a hollow silica fiber and utilizes bacterial cells as spatial light modulators. This generates a highly sensitive modulation transfer function due to the narrow reflectivity angle in the fiber-media interface. We leveraged the RUSD technology to allow for robust bacterial and fungal detection. RUSD can now detect pathogenic cell densities in a large dynamic window ( $OD_{600}$  from  $\sim 10^{-7}$  to  $10^{-1}$ ). Finally, we can generate dose response curves for various pathogens and antimicrobial compounds within one to three hours by using RUSD. Our antibiotic-susceptibility testing (AST) assay that we call iFAST (in-Fiber-Antibiotic-Susceptibility-Testing) is fast, highly sensitive, and does not change the existing workflow in clinical settings as it is compatible with FDA-approved AST. Thus, RUSD platform is a viable tool that will expedite decision-making process in the treatment of infectious diseases and positively impact the antibiotic resistance problem in the long term by minimizing the use of ineffective antibiotics.

**Keywords:** AST (antibiotic susceptibility testing), optical fiber, biomedical application, clinical microbial infection, rapid assay

## INTRODUCTION

Effective clinical diagnoses of infections require rapid and accurate species characterization and antibiotic-susceptibility testing (AST) of disease agents to develop most efficacious treatment strategies (Singh et al., 2006; van Belkum et al., 2020). AST in particular is vital due to the ubiquitous nature of antibiotic resistance genes leading to a significant risk of antibiotic treatment failures, particularly for infections occurring in clinical settings (Merli et al., 2015). Such failures not only cause short term problems but can also cause long-term health problems because antibiotics can induce dysbiosis in patient microbiome (Francino 2016).

![Schematic diagram of the RUSD device components. The setup includes a Laser Diode housed in an Oven with a TEC (Thermo Electric Cooler) and controlled by a TEC Control unit and a Power Supply. The laser beam is directed through a Fiber Pigtail, a Focus Lens, and a Mirror into a Silica Fiber. The fiber is mounted on a Watchglass and has a Sample Inlet and a Sample Outlet. A photodiode is positioned at the Sample Outlet to measure the light signal. The photodiode is connected to an Amplifier, which is then connected to an ADC (Analog-to-Digital Converter). The diagram also shows the internal light path within the fiber, where light is guided, absorbed, or deflected by particles, with an Offset signal indicated.](aa9e46d6f962be5cebcbb5c654c9b13e_img.jpg)

Schematic diagram of the RUSD device components. The setup includes a Laser Diode housed in an Oven with a TEC (Thermo Electric Cooler) and controlled by a TEC Control unit and a Power Supply. The laser beam is directed through a Fiber Pigtail, a Focus Lens, and a Mirror into a Silica Fiber. The fiber is mounted on a Watchglass and has a Sample Inlet and a Sample Outlet. A photodiode is positioned at the Sample Outlet to measure the light signal. The photodiode is connected to an Amplifier, which is then connected to an ADC (Analog-to-Digital Converter). The diagram also shows the internal light path within the fiber, where light is guided, absorbed, or deflected by particles, with an Offset signal indicated.

**FIGURE 1** | Schematic depicting the RUSD device components. The laser beam emitted by the laser diode is directed into the optical fiber through a focus lens and mirror such that the angle at which the beam enters the fiber is  $>89^\circ$ . The Sample inlet part of the fiber also is fitted with tubing used to inject fluid samples into the fiber as well. On the other end of the fiber, the sample outlet directs the liquid sample out of the tube. A photodiode is also present at this end of the fiber to measure the optical signal received from light that was able to pass completely through the optical fiber and convert these units into voltage units. This diode is connected to an amplifier that feeds signal into an ADC which converts these signals into a digital output.

Current methods to determine antibiotic susceptibility testing of clinical isolates mostly use culture-based techniques that rely on visual inspection or optical density-based measurements for final result (van Belkum et al., 2020). These methods are time-consuming, taking up to several days to obtain results in a setting where prompt results could play a deterministic role in patient health outcomes. A key disadvantage to current optical density-based diagnostics is decreased confidence at low values of density or slow growing pathogens. Consequentially a reliable reading for growth measured by spectrophotometry can only be attained for *Escherichia coli* when there are  $10^6$  cells/ml (approx.  $OD_{600}$  0.01) (Cansizoglu et al., 2019). Therefore, these assays are limited by the variation in growth rates of different pathogenic species so the time taken to arrive at these high cell densities could be considerable. Instead, a method able to detect the presence and subsequent growth of even small numbers of bacteria would greatly accelerate current diagnostics.

We have previously described a novel experimental apparatus [Rapid Ultrasensitive Detector (RUSD)] utilizing scattering of light as a method for detecting small numbers of bacteria in culture (Cansizoglu et al., 2019). We have validated our findings by showing faster, more accurate results for detecting small numbers of prokaryotic bacterial cells and small numbers of eukaryotic yeast cells. The RUSD is capable of detecting as small as single pathogenic fungal cells such as *Candida glabrata* and  $\sim 25$  bacterial cells (e.g., *E. coli*) in its detection volume ( $\sim 80 \mu\text{l}$ ). The set-up utilizes a hollow fiber which serves as an opto-fluidic channel and a light guide. Media is pumped through this fiber continuously with the use of programmable pumps or can be injected manually. A laser is focused through the fiber in such a way that the incidence angle at the fiber wall is  $>89^\circ$  (almost parallel to the long axis of the fiber), thus ensuring light is total internally reflected through the fiber (Figure 1). Photons that encounter micron sized particles in the media get deflected and can no longer travel through the fiber because they violate the

![Image of the RUSD device showing its physical components. The device is mounted on a base and includes a Laser Oven, a TIA (trans Impedance amplifier), a Photodiode, a Liquid Port, a Monitor Port, and a Power Supply. The setup is labeled with 'Optical Frame' and 'Alignment Stage'.](cb00037bd3b3af9720d5551ad2f818dd_img.jpg)

Image of the RUSD device showing its physical components. The device is mounted on a base and includes a Laser Oven, a TIA (trans Impedance amplifier), a Photodiode, a Liquid Port, a Monitor Port, and a Power Supply. The setup is labeled with 'Optical Frame' and 'Alignment Stage'.

**FIGURE 2** | Image of the RUSD device. The image is labelled with the salient features of the device. TIA, trans Impedance amplifier; TEC, thermo electric cooler.

condition for reflectivity. Thus, light encountering obstacles in their path will be blocked and will result in a decrease of detected light intensity at the other end of the fiber (Figure 1). This reduction in light intensity relative to media that is free of obstacles (e.g., bacterial cells) can be measured by the change in voltage captured by a photodiode (hereafter referred to as  $\Delta V$ ). These differences can be converted to  $OD_{600}$  values (i.e.,  $OD_{600} = 1$  corresponds to approximately  $5 \times 10^8$  cells/ml of *E. coli* culture).

In this paper, we introduce an instrument built with RUSD specifications which is portable, cost-effective and performs at comparable analytical power with adjustable dynamical range for cell density measurements (Figures 1, 2). The device is equipped with a hollow fiber mounted for stability and the laser-photo diode setup for detection of cells. There are some small differences between the previously developed RUSD apparatus

![Figure 3: Calibration curves for yeast and E. coli. (A) Calibration curve for E. coli BW25113 showing ΔV vs OD600. (B) Calibration curve for yeast strain S. cerevisiae showing ΔV vs OD600.](3cab54230d8ae3b786ddda81346602cc_img.jpg)

Figure 3 consists of two scatter plots, A and B, showing calibration curves. Plot A (left) shows the relationship between  $\Delta V$  (Y-axis, logarithmic scale from  $1 \times 10^{-3}$  to  $1 \times 10^{1}$ ) and  $OD_{600}$  (X-axis, logarithmic scale from  $1 \times 10^{-3}$  to  $1 \times 10^{-1}$ ) for *E. coli* BW25113. The data points show a linear trend on the log-log plot. Plot B (right) shows the relationship between  $\Delta V$  (Y-axis, logarithmic scale from  $3 \times 10^{-2}$  to  $1 \times 10^{0}$ ) and  $OD_{600}$  (X-axis, logarithmic scale from  $1 \times 10^{-5}$  to  $1 \times 10^{-3}$ ) for yeast strain *S. cerevisiae*. The data points in both plots follow a linear trend on the log-log scale, indicating a power-law relationship between  $\Delta V$  and  $OD_{600}$ .

Figure 3: Calibration curves for yeast and E. coli. (A) Calibration curve for E. coli BW25113 showing ΔV vs OD600. (B) Calibration curve for yeast strain S. cerevisiae showing ΔV vs OD600.

**FIGURE 3** | Calibration curves for yeast and *E. coli*. **(A)** *E. coli* BW25113 strains were cultured overnight in M9 media and the following day, serial dilutions were made in M9 media supplemented with chloramphenicol. The  $\Delta V$  values were plotted against  $OD_{600}$  values corresponding to spectrophotometer values of the original culture. **(B)** Yeast strain *S. cerevisiae* was cultured in YPD media and dilutions of the culture were made.  $\Delta V$  values were measured using RUSD device and were plotted against spectrophotometer values based on dilutions of the overnight culture.

and the instrument we describe in this paper. Besides including a temperature control module for the laser power stability, the RUSD device was built with clinical and field use in mind, and as such was constructed in a more compact form. Additionally, the electronic and mechanical components of the RUSD device were redesigned to ensure ease of use, robustness, and simplicity. A detailed schematic describing the components of the device can be found in **Figure 1**. We show the limit of detection (LOD) of this device is 1,000–10,000 times lower than the LOD for conventional spectrophotometers and plate readers. The adjustable dynamic range of detectable densities allows us to quantitatively measure phenotypic signatures of pathogens such as growth rates much faster than conventional optical-density-based methods. Finally, we use this new RUSD prototype to determine the MIC of a clinically relevant antibiotic, cefepime, arriving at a conclusive result for inhibitory/sub-inhibitory concentrations in 1 h versus at least 8–10 h using conventional methods.

## RESULTS

### Range of Detection

To determine the range of detection for the device, overnight *E. coli* cultures were serially diluted and the  $\Delta V$  for each of the diluted samples were measured using RUSD (**Figure 3A**). The ODs were calculated using a spectrophotometer and corresponding values for colony forming units (or CFUs) were also simultaneously determined by colony counting method. For our calibration we started at  $OD_{600} \sim 3 \times 10^{-6}$  corresponding to 1,500 CFU/ml (**Figure 3A**). This represents a  $\sim 1,000$ -fold more sensitivity compared to conventional spectrophotometers whose lower limit of detection (LOD) typically range between  $10^{-3}$  and  $10^{-2}$ .

The maximum  $OD_{600}$  that could be detected using the RUSD setting we used for this paper was  $\sim 10^{-2}$  corresponding to  $5 \times 10^6$  bacterial cells per milliliter. At these cell densities the instrument reached its maximum reading threshold and higher densities of cells registered identical saturated readings (**Figure 3A**). This metric shows the sensitivity of the RUSD compared to conventional optical-based methods. While

spectrophotometers often have a range of detection spanning  $10^6$  CFU/ml– $5 \times 10^8$  CFU/ml, the range for the RUSD is much wider for far lower cell densities leading to more precise detection of lower quantities of cells in biological samples. M9 minimal growth media was used in the device due to its transparent color enabling more sensitive detection of smaller numbers of cells (Methods). Of note, the dynamic range can be rapidly adjusted on the fly and the same RUSD device can perform equally well at different dynamical ranges when necessary.

Eukaryotic cells such as yeast are generally larger than bacteria and hence their detection range differs. Using yeast cultures in YPD media, we made a calibration curve starting at  $OD_{600} 10^{-6}$  ( $\sim 20$  cells) to  $OD_{600} 10^{-3}$  (**Figure 3B**). The sensitivity of the RUSD can be increased when necessary to detect even single yeast cells by simply increasing laser power and gain in the detector.

### RUSD for Detecting Cell Growth Dynamics

The bacterial “lag” phase refers to the initial period when bacteria are introduced into a new environment when no growth is detectable (Bertrand 2019). When measured with conventional methods such as a plate reader or spectrophotometer this phase can last several hours depending on the initial density of the inoculum. However, one reason for this extended lag time is because these methods can only detect higher cell densities. Bacterial growth below the method’s limit of detection is not detected and falsely extends the observed lag time (Cansizoglu et al., 2019). Therefore, methods that can measure miniscule concentrations of bacteria at that initial growth phase present a method to combat inflated lag times delaying results. Using a very low concentration initial inoculum of  $5 \times 10^{-5}$   $OD_{600}$  (approx. 25,000 CFU/ml) in the RUSD, we were able to detect growth in as little as 45 min (**Figure 4**) following inoculation. This represents an important technical advancement since measuring growth of a culture is an essential step when determining Minimum Inhibitory Concentrations (MIC) for antibiotics and performing antibiotic susceptibility testing (AST).

We followed the growth curve of this inoculum using an initial density of  $5 \times 10^{-5}$  and were able to obtain a growth curve that matched the growth dynamics such as growth rate and doubling time ( $\sim 40$  min in minimal M9 media, **Figure 4D**) obtained using other optical methods at higher cell densities (Reshes et al., 2008).

![Figure 4: Growth of bacteria in RUSD device. Panel A shows 8 line graphs of Equivalent OD600 vs Time (min) for cefepime concentrations from 0 to 1 µg/ml. Panel B is a heat map of Equivalent OD600 vs Time (min) and Cefepime (µg/ml). Panel C is a line graph of Equivalent OD600 vs Cefepime (µg/ml) for times 45, 60, 90, and 120 min. Panel D is a line graph of Growth Rate (h⁻¹) vs Cefepime (µg/ml).](7fb5215fd72210a2e4cce6df55550c89_img.jpg)

**A**

| Cefepime Concentration (µg/ml) | Approximate Growth Threshold (OD <sub>600</sub> ) |
|--------------------------------|---------------------------------------------------|
| 0                              | ~3.5 × 10 <sup>-4</sup>                           |
| 0.0125                         | ~2.5 × 10 <sup>-4</sup>                           |
| 0.025                          | ~2.0 × 10 <sup>-4</sup>                           |
| 0.05                           | ~1.5 × 10 <sup>-4</sup>                           |
| 0.1                            | ~8 × 10 <sup>-5</sup>                             |
| 0.2                            | ~7 × 10 <sup>-5</sup>                             |
| 0.5                            | ~6 × 10 <sup>-5</sup>                             |
| 1                              | ~5 × 10 <sup>-5</sup>                             |

**B**

**C**

| Cefepime (µg/ml) | 45 min OD <sub>600</sub> | 60 min OD <sub>600</sub> | 90 min OD <sub>600</sub> | 120 min OD <sub>600</sub> |
|------------------|--------------------------|--------------------------|--------------------------|---------------------------|
| 0                | ~0.00010                 | ~0.00010                 | ~0.00010                 | ~0.00010                  |
| 0.0125           | ~0.00024                 | ~0.00024                 | ~0.00024                 | ~0.00024                  |
| 0.025            | ~0.00024                 | ~0.00024                 | ~0.00024                 | ~0.00024                  |
| 0.05             | ~0.00015                 | ~0.00015                 | ~0.00015                 | ~0.00015                  |
| 0.1              | ~0.00008                 | ~0.00008                 | ~0.00008                 | ~0.00008                  |
| 0.2              | ~0.00005                 | ~0.00005                 | ~0.00005                 | ~0.00005                  |
| 0.5              | ~0.00002                 | ~0.00002                 | ~0.00002                 | ~0.00002                  |
| 1                | ~0.00001                 | ~0.00001                 | ~0.00001                 | ~0.00001                  |

**D**

| Cefepime (µg/ml) | Growth Rate (h <sup>-1</sup> ) |
|------------------|--------------------------------|
| 0                | ~1.00                          |
| 0.0125           | ~1.00                          |
| 0.025            | ~1.00                          |
| 0.05             | ~0.70                          |
| 0.1              | ~0.00                          |
| 0.2              | ~0.00                          |
| 0.5              | ~0.00                          |
| 1                | ~0.00                          |

Figure 4: Growth of bacteria in RUSD device. Panel A shows 8 line graphs of Equivalent OD600 vs Time (min) for cefepime concentrations from 0 to 1 µg/ml. Panel B is a heat map of Equivalent OD600 vs Time (min) and Cefepime (µg/ml). Panel C is a line graph of Equivalent OD600 vs Cefepime (µg/ml) for times 45, 60, 90, and 120 min. Panel D is a line graph of Growth Rate (h⁻¹) vs Cefepime (µg/ml).

**FIGURE 4** | Growth of bacteria in RUSD device. **(A)** Overnight cultures of *E. coli* were diluted to  $5 \times 10^{-5}$  OD<sub>600</sub> and circulated through the device for 2 h in M9 media supplemented with different concentrations of cefepime. Bacterial growth can be detected as early as 45 min. Growth within the 2-h time frame indicated sub-MIC concentrations of cefepime. **(B)** Heat map of bacterial OD<sub>600</sub> (equivalent of measured as RUSD  $\Delta V$ ) versus different concentrations of cefepime over time. T = 45, 60, 90, and 120 min are highlighted to emphasize the earliest interpretation of antibiotic resistance/susceptibility. **(C)** Plot of equivalent OD<sub>600</sub> of cultures at different times during growth with cefepime. Definitive results for growth (i.e., resistance/susceptibility) can be seen after only 1 h. **(D)** Figure showing growth rate vs. concentration of cefepime as measured in the RUSD device.

This illustrates how the RUSD device can replicate bacterial growth measurements obtained from other methods even for cultures with a much lower initial bacterial concentration, which attests to the accuracy of this device at lower cell densities.

### Rapid Antibiotic Susceptibility Testing With iFAST

Timely determination of antibiotic susceptibilities and MIC is important in clinical settings to decide effective treatment interventions. However, since these clinical AST assays are usually based on spectrophotometer readings and rely on substantial bacterial growth, these can take up to several days to obtain a result. Using the RUSD, we have established a novel technique to quickly determine the MIC of a sample termed “iFAST” or in-Fiber-Antibiotic-Susceptibility-Testing. In this method, using the RUSD and bacterial inoculums of  $5 \times 10^{-5}$  OD, we determined the MIC of *E. coli* to the antibiotic cefepime (a fourth-generation cephalosporin). Since our current set up has a single fiber, we were only able to use one antibiotic concentration at a time, but each concentration gave us definitive readings for growth and growth rate by hour two post injection and using these values, we were able to determine the MIC for cefepime within 45 min (**Figure 4B**) hours, substantially faster than any other AST method known to us. The first 15 min of data measurements were not shown in **Figure 4B** as the readings from the device were erroneous due to the bacteria still mixing in the fiber after injection. Using these values, we were able to plot the equivalent OD<sub>600</sub> of cultures measured as  $\Delta V$  in the RUSD versus time for the different antibiotic concentrations used (**Figure 4C**). The graphs show the magnitude of the difference between the different antibiotic concentrations which becomes visible as early as 45 min after the start of the assay and progresses for the duration of the 2 h.

## CONCLUSION AND DISCUSSION

In conclusion, our the RUSD device we developed is able to recapitulate the benefits of our previously validated experimental setup with small reductions in sensitivity in exchange for greater stability and adjustable dynamic range. The lower limit of detection for this instrument is key to its advantage over other conventional methods since it can detect fewer cells in the medium and monitor their growth very early. Another advantage of this setup is how it fits in with standard operating procedures already in place for clinical AST.

Currently in clinics, blood cultures are the gold standard for the diagnosis of sepsis and bacteremia, despite the test requiring many hours or even days to return a result leading to prolonged treatment using empiric broad-spectrum antibiotics (Sweeney et al., 2019). A positive blood culture, while indicative of an underlying infection does not yield any information on species identification and antibiotic susceptibility testing. These types of tests are often performed using matrix-assisted laser desorption ionization time-of-flight (\_MALDI-TOF) or nucleic-acid-based methods (PCR or sequencing) (Opota et al., 2015) which can add

hours to the proper diagnosis of the underlying cause of infection worsening patient outcomes. AST testing which relies on growth-based assays is also a time-consuming step relying on standard broth microdilution assays or disk diffusion assays (CLSI, 2012; CLSI, 2018).

There is currently an urgent need to develop AST devices/protocols that are cost-effective and deliver results fast. Some innovative methods that have been developed include lab-on-a-chip setups that use DNA hybridization and amplification (Kalsi et al., 2015). Another promising method uses electrochemical signals from a redox reaction to indicate growth with a particular antibiotic (Besant et al., 2015). These methods, while effective, still require the use of consumable reagents and additional processing steps before the assays can be performed. Our RUSD device, however, is compatible with current clinical lab protocols and will require minimal specialized training to operate. To our knowledge, this is the first application of an optical fiber wherein it is directly used for culturing and detection of bacteria. Other medical devices have employed the use of these fibers merely to transmit signals from a separate detection apparatus (Hayman 2008; Ahmed et al., 2014; Yoo and Lee 2016; Janik et al., 2021). Therefore this technology represents a paradigm shift for clinical laboratories. Using RUSD can save precious hours in clinical testing and enable healthcare workers to quickly proceed with correct treatment of patients thereby alleviating infectious burdens faster. We are currently working towards making RUSD a fully automated and multiplexed platform as antibiotic susceptibility testing require testing many antibiotic compounds at various concentrations. This can be achieved by either building many RUSD devices operating in parallel or utilizing an advanced fluidic platform for time-sharing between channels and automating sample injection and sterilization.

## MATERIALS AND METHODS

### Device Design

The core design of the second version of the device is identical to the one described in the original RUSD paper (Cansizoglu et al., 2019). However, several additions were added to the system to ameliorate it (**Figures 1, 2**). First, the laser diode was placed under temperature control using a closed feed-back loop system to enhance beam stability and quality. The silica fiber we use is highly sensitive to temperature changes because of its large length (e.g., 40 cm) and small wall thickness ( $\sim 0.15$  mm). This presented an issue when performing susceptibility testing experiments as the higher temperature of the media and incubation environment would alter the power output of the laser diode, thereby skewing the readings. Additionally, a programmable hot plate and a peristaltic pump were added to the system to allow for continuous measurements and growth of bacteria directly in the testing chamber. This addition was invaluable from a practical and user case perspective as it allowed autonomous continuous measurement of bacterial growth rate without the need for taking samples out of the incubator to inject them into the device for measurement. Overall, while the changes might

seem minor, they truly expanded the capabilities and robustness of the device as a clinical tool.

### Calibration

Before utilizing the device for AST, we first calibrated the device to have a correspondence formula between voltage drop in the device as a result of the presence of bacteria and their concentration in OD<sub>600</sub>. This was done with *E. coli* bacteria (K12, BW25113) and brewer yeast (*Saccharomyces cerevisiae*). *E. coli* was grown overnight in M9 minimal media supplemented with 0.4% glucose (Fisher Scientific B152-1), 0.2% Amicase (MP Biomedicals 104778), 2 mM MgSO<sub>4</sub> (Fisher Scientific M63-500), 100  $\mu$ M of CaCl<sub>2</sub> (Fisher Scientific S25222A), while yeast was grown in YPD media (Fisher Scientific BP-2469). The following day (or 2 days in the case of yeast) the concentration of the overnight culture was measured using a spectrophotometer and 2-fold dilutions were made in the range between 10<sup>-5</sup> and 10<sup>-1</sup> OD for bacteria and 10<sup>-6</sup> and 10<sup>-3</sup> for yeast. Then, the voltage drop for each dilution of *E. coli* or yeast was measured for 30 s at 1000 Hz sampling frequency, and the average value of the signal was calculated. Then, log-log linear regression was used to derive the conversion formula for both yeast and *E. coli*.

### Antibiotic Susceptibility Testing

To demonstrate the clinical potential of the new version RUSD, we utilized it to conduct rapid antibiotic susceptibility testing against cefepime, a new-generation beta-lactam antibiotic. Eight culture media solutions (using M9 minimal media supplemented with glucose and cas amino acids) were made with increasing cefepime concentrations ranging from 0 to 1  $\mu$ g/ml. For each sample, bacteria was added to roughly a level of 0.00005 OD<sub>600</sub> and then the sample was circulated in the device at 37°C, and measurements were collected using DASYLab® software for 2 h. This was accomplished by placing the sample tube in a hotplate set to 37°C and using a peristaltic pump for pushing the sample solution into the device's fiber and back to the conical tube. The

initial 10–15 min of measurement data was not used as the bacteria was still being mixed in the device chamber, yielding sporadic noisy readings. Between sample measurements, the device was cleaned of any residue by pumping the sample media out of the fiber and running 70% isopropyl alcohol for 2 min. After all eight samples were run through the device and measurements were collected, they were converted to OD<sub>600</sub> from  $\Delta V$  and the growth dynamics and MIC could be interpreted starting around 45 min (Figure 4).

## DATA AVAILABILITY STATEMENT

The raw data supporting the conclusion of this article will be made available by the authors, without undue reservation.

## AUTHOR CONTRIBUTIONS

MF performed the experiments and wrote the manuscript, MR provided strains and wrote the manuscript, RE constructed the device, ET conceived and planned experiments and wrote the manuscript.

## FUNDING

This work was supported by the UTSW Endowed Scholars Program, Human Frontiers Science Program Research grant RGP0042/2013, National Institutes of Health grant R01GM125748 and Welch Foundation I-2082-20210327.

## ACKNOWLEDGMENTS

We thank all the members of Toprak lab for their help.

## REFERENCES

Ahmed, A., Rushworth, J. V., Hirst, N. A., and Millner, P. A. (2014). Biosensors for Whole-Cell Bacterial Detection. *Clin. Microbiol. Rev.* 27 (3), 631–646. doi:10.1128/CMR.00120-13

Bertrand, R. L. (2019). Lag Phase Is a Dynamic, Organized, Adaptive, and Evolvable Period that Prepares Bacteria for Cell Division. *J. Bacteriol.* 201 (7), e00697-18. doi:10.1128/JB.00697-18

Besant, J. D., Sargent, E. H., and Kelley, S. O. (2015). Rapid Electrochemical Phenotypic Profiling of Antibiotic-Resistant Bacteria. *Lab. Chip* 15 (13), 2799–2807. doi:10.1039/C5LC00375J

Cansizoglu, M. F., Tamer, Y. T., Farid, M., Koh, A. Y., and Toprak, E. (2019). Rapid Ultrasensitive Detection Platform for Antimicrobial Susceptibility Testing. *PLoS Biol.* 17 (5), e3000291. doi:10.1371/JOURNAL.PBIO.3000291

CLSI (2012). *Laboratory Standards I. Methods for Dilution Antimicrobial Susceptibility Tests for Bacteria that Grow Aerobically: Approved Standard*. Wayne, PA: Clinical and Laboratory Standards Institute.

CLSI (2018). *Laboratory Standards I. Performance Standards for Antimicrobial Disk Susceptibility Tests*. Wayne, PA: Clinical and Laboratory Standards Institute.

Francino, M. P. (2016). Antibiotics and the Human Gut Microbiome: Dysbioses and Accumulation of Resistances. *Front. Microbiol.* 6, 1543–43. doi:10.3389/FMICB.2015.01543/BIBTEX

Hayman, R. B. (2008). "Fiber Optic Biosensors for Bacterial Detection," in *Principles of Bacterial Detection: Biosensors, Recognition Receptors and Microsystems*. Editors M. Zourob, S. Elwary, and A. Turner (New York, NY: Springer).

Janik, M., Brzozowska, E., Czyszczon, P., Celebańska, A., Koba, M., Gamian, A., et al. (2021). Optical Fiber Aptasensor for Label-free Bacteria Detection in Small Volumes. *Sensors Actuators B Chem.* 330, 129316. doi:10.1016/j.snb.2020.129316

Kalsi, S., Valiadi, M., Tsaloglou, M.-N., Parry-Jones, L., Jacobs, A., Watson, R., et al. (2015). Rapid and Sensitive Detection of Antibiotic Resistance on a Programmable Digital Microfluidic Platform. *Lab. Chip* 15 (14), 3065–3075. doi:10.1039/C5LC00462D

Merli, M., Lucidi, C., Di Gregorio, V., Falcone, M., Giannelli, V., Lattanzi, B., et al. (2015). The Spread of Multi Drug Resistant Infections Is Leading to an Increase in the Empirical Antibiotic Treatment Failure in Cirrhosis: A Prospective Survey. *PLOS ONE* 10 (5), e0127448. doi:10.1371/JOURNAL.PONE.0127448

Opota, O., Croxatto, A., Prod'hom, G., and Greub, G. (2015). Blood Culture-Based Diagnosis of Bacteremia: State of the Art. *Clin. Microbiol. Infect.* 21, 313–322. doi:10.1016/j.cmi.2015.01.003

Reshes, G., Vanounou, S., Fishov, I., and Feingold, M. (2008). Timing the Start of Division in *E. coli*: a Single-Cell Study. *Phys. Biol.* 5 (4), 046001. doi:10.1088/1478-3975/5/4/046001

Singh, A., Goering, R. V., Simjee, S., Foley, S. L., and Zervos, M. J. (2006). Application of Molecular Techniques to the Study of Hospital Infection. *Clin. Microbiol. Rev.* 19 (3), 512–530. doi:10.1128/CMR.00025-05

Sweeney, T. E., Liesenfeld, O., and May, L. (2019). Diagnosis of Bacterial Sepsis: Why Are Tests for Bacteremia Not Sufficient? *Expert Rev. Mol. Diagnostics* 19, 959–962. doi:10.1080/14737159.2019.1660644

van Belkum, A., Burnham, C.-A. D., Rossen, J. W. A., Mallard, F., Rochas, O., and Dunne, W. M. (2020). Innovative and Rapid Antimicrobial Susceptibility Testing Systems. *Nat. Rev. Microbiol.* 18 (5), 299–311. doi:10.1038/s41579-020-0327-x

Yoo, S. M., and Lee, S. Y. (2016). Optical Biosensors for the Detection of Pathogenic Microorganisms. *Trends Biotechnol.* 34 (1), 7–25. doi:10.1016/J.TIBTECH.2015.09.012

**Conflict of Interest:** The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

**Publisher's Note:** All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

Copyright © 2022 Farid, Rodrigues, England and Toprak. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.