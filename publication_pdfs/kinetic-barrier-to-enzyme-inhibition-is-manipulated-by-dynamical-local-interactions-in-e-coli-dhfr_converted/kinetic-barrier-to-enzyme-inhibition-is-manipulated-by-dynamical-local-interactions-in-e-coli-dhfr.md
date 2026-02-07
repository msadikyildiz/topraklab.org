

# Kinetic Barrier to Enzyme Inhibition Is Manipulated by Dynamical Local Interactions in *E. coli* DHFR

Ebru Cetin, Tandac F. Guclu, Isik Kantarcioglu, Ilona K. Gaszek, Erdal Toprak, Ali Rana Atilgan, Burcu Dedeoglu,\* and Canan Atilgan\*

![Checkmark icon indicating citation information.](0538daaa5583c23e17db3a12f2281a55_img.jpg)

Checkmark icon indicating citation information.

Cite This: *J. Chem. Inf. Model.* 2023, 63, 4839–4849

![Globe icon indicating online reading.](6ed175c791b5e156d9c98a8dbcc3318c_img.jpg)

Globe icon indicating online reading.

Read Online

ACCESS |

![Metrics & More icon.](d3294dc879b451b369c0b06f42e9b39f_img.jpg)

Metrics & More icon.

Metrics & More

![Article Recommendations icon.](8740e63f5546e4004e600f24d883acba_img.jpg)

Article Recommendations icon.

Article Recommendations

![Supporting Information icon.](5a36d88d3904f3f2d386c7cf63fa5053_img.jpg)

Supporting Information icon.

Supporting Information

**ABSTRACT:** Dihydrofolate reductase (DHFR) is an important drug target and a highly studied model protein for understanding enzyme dynamics. DHFR's crucial role in folate synthesis renders it an ideal candidate to understand protein function and protein evolution mechanisms. In this study, to understand how a newly proposed DHFR inhibitor, 4'-deoxy methyl trimethoprim (4'-DTMP), alters evolutionary trajectories, we studied interactions that lead to its superior performance over that of trimethoprim (TMP). To elucidate the inhibition mechanism of 4'-DTMP, we first confirmed, both computationally and experimentally, that the relative binding free energy cost for the mutation of TMP and 4'-DTMP is the same, pointing the origin of the characteristic differences to be kinetic rather than thermodynamic. We then employed an interaction-based analysis by focusing first on the active site and then on the whole enzyme. We confirmed that the polar modification in 4'-DTMP induces additional local interactions with the enzyme, particularly, the M20 loop. These changes are propagated to the whole enzyme as shifts in the hydrogen bond networks. To shed light on the allosteric interactions, we support our analysis with network-based community analysis and show that segmentation of the loop domain of inhibitor-bound DHFR must be avoided by a successful inhibitor.

![Figure showing WT:TMP and L28R:4'-DTMP interactions. The top panel, 'WT:TMP interactions', shows a bar chart of interaction frequencies over 1000 ns for residues ILE5 (8.2%), ALA6 (20.0%), MET20 (0.0%), ASP27 (75.8%), LEU28 (0.0%), and THR113 (8.9%). A 3D molecular model shows the binding site with residues I5, A6, D27, T113, and L28. The bottom panel, 'L28R:4'-DTMP interactions', shows a bar chart for residues ILE5 (11.1%), ALA6 (33.6%), MET20 (15.1%), ASP27 (87.0%), ARG28 (40.8%), and THR113 (41.7%). A 3D model shows the binding site with residues I5, A6, D27, T113, R28, and M20.](520fdfae556127af5098809fb6ff0243_img.jpg)

Figure showing WT:TMP and L28R:4'-DTMP interactions. The top panel, 'WT:TMP interactions', shows a bar chart of interaction frequencies over 1000 ns for residues ILE5 (8.2%), ALA6 (20.0%), MET20 (0.0%), ASP27 (75.8%), LEU28 (0.0%), and THR113 (8.9%). A 3D molecular model shows the binding site with residues I5, A6, D27, T113, and L28. The bottom panel, 'L28R:4'-DTMP interactions', shows a bar chart for residues ILE5 (11.1%), ALA6 (33.6%), MET20 (15.1%), ASP27 (87.0%), ARG28 (40.8%), and THR113 (41.7%). A 3D model shows the binding site with residues I5, A6, D27, T113, R28, and M20.

## INTRODUCTION

Antibiotics play a critical role in the treatment and prevention of bacterial infections by inhibiting the growth of these organisms in the host. The discovery of antibiotics has been a breakthrough for mankind by reducing mortality and morbidity from infectious diseases.<sup>1</sup> However, antibiotic resistant bacteria have emerged due to the often unnecessary and indiscriminate use of antibiotics; in fact, only a few years may suffice for a new drug to become ineffective in the clinic.<sup>2,3</sup> New generation antibiotics are being developed to overcome the resistance problems against existing ones, but bacteria fight back by developing resistance against these new agents.<sup>4</sup> Thus, it is of great importance to elucidate the mechanisms that cause resistance and accordingly design drugs that will impede the evolution of resistance.

The design of new and more active drugs based on a knowledge of their mechanism of action plays a central role to overcome antibiotic resistance.<sup>5,6</sup> Dihydrofolate reductase (DHFR) is an enzyme that has been frequently studied in this framework since it is widely found in all living organisms and has an important role in cell metabolism.<sup>7,8</sup> In fact, due to its key biological function, it is an important therapeutic target for anticancer, antimalarial, and antibacterial medicine.<sup>9–14</sup>

DHFR is necessary for cell growth due to its role in the production of DNA precursors. It catalyzes the reduction of dihydrofolate (DHF) in the presence of the cofactor NADPH to tetrahydrofolate (THF), the precursors for purine and thymine. *Escherichia coli* DHFR (Figure 1a) has 159 residues and features eight  $\beta$  strands and four  $\alpha$  helices, forming an  $\alpha/\beta$  structure arranged into the adenosine binding (ABD) and loop (LD) domains.

Trimethoprim (TMP, Figure 1b) is a widely used antibiotic compound to treat various bacterial infections.<sup>15,16</sup> TMP binds the orthosteric site of DHFR, inhibiting the reduction of DHF to THF (Figure 1b), an essential precursor in the synthesis of nucleic acids.<sup>17</sup> The affinity of TMP for bacterial DHFR is much greater than that of the vertebrate enzyme, making this drug highly effective.<sup>18</sup> On the other hand, its efficacy is limited due to the TMP resistance acquired by bacteria.<sup>19</sup>

Received: May 29, 2023

Published: July 26, 2023

![Thumbnail image of the journal cover for J. Chem. Inf. Model. 2023, 63, 4839–4849.](cb5eaf8e70e3c5f8770cd7649d1ec5dd_img.jpg)

Thumbnail image of the journal cover for J. Chem. Inf. Model. 2023, 63, 4839–4849.

![Figure 1: DHFR structure, mechanism, and its binding partners. (a) DHFR structure of the last snapshot of the TMP bound trajectory of the wild type structure, WT<sup>TMP</sup>. (b) Schematics of the catalytic reaction of DHFR and its inhibition by TMP. (c) Enzyme-substrate interactions for DHFR-WT and DHFR-L28R. (d) Chemical structures of Trimethoprim (TMP), protonated Trimethoprim (TMP<sup>+</sup>), and 4'-Desmethyltrimethoprim (4'-DTMP<sup>+</sup>).](baf3bd2968ee415961b89429d3d49642_img.jpg)

Figure 1 consists of four panels (a-d). Panel (a) shows a ribbon diagram of the DHFR protein structure with various loops and helices labeled: E helix, CD loop, Adenosine Binding Domain (ABD), F helix, M20 loop, C helix, B helix, Loop Domain (LD), FG loop, and GH loop. Panel (b) illustrates the catalytic cycle of DHFR, showing the conversion of DHF to THF using NADPH as a cofactor, and the inhibition of this process by Trimethoprim (TMP). Panel (c) details the specific interactions between the enzyme and the substrate (DHF) in the wild-type (DHFR-WT) and the L28R mutant (DHFR-L28R), highlighting residues R52, R57, R28, and the glutamate tail. Panel (d) displays the chemical structures of Trimethoprim (TMP), its protonated form (TMP<sup>+</sup>), and the 4'-Desmethyltrimethoprim derivative (4'-DTMP<sup>+</sup>).

Figure 1: DHFR structure, mechanism, and its binding partners. (a) DHFR structure of the last snapshot of the TMP bound trajectory of the wild type structure, WT<sup>TMP</sup>. (b) Schematics of the catalytic reaction of DHFR and its inhibition by TMP. (c) Enzyme-substrate interactions for DHFR-WT and DHFR-L28R. (d) Chemical structures of Trimethoprim (TMP), protonated Trimethoprim (TMP<sup>+</sup>), and 4'-Desmethyltrimethoprim (4'-DTMP<sup>+</sup>).

**Figure 1.** DHFR structure, mechanism, and its binding partners studied in this work. a) DHFR structure of the last snapshot of the TMP bound trajectory of the wild type structure, WT<sup>TMP</sup>. ABD spans residues 38–104, while LD comprises the rest. Loops are identified as M20 (9–24), CD (64–71), FG (116–132), and GH (142–150), whereas the helices are named B (24–36), C (43–51), E (79–86), and F (95–106). b) Schematics of the catalytic reaction of DHFR and its inhibition by TMP. c) Enzyme–substrate interactions. d) TMP and its derivative were studied in this work.

Pathogenic bacteria can rapidly render antibiotics ineffective through the acquisition of mutations that lead to resistance. Understanding the evolutionary processes of these mutations is of great importance for the discovery of next-generation drugs. Toward this end, it was shown via evolutionary experiments, that it is possible to observe antibiotic resistance emerging in the DHFR encoding gene of bacterial cultures in the laboratory with a device called “morbidostat”.<sup>20,21</sup> It was later shown that there was a disproportionate amount of resistant strains carrying the L28R mutation as the first mutation<sup>22</sup> and has therefore been used as part of studies for understanding antibiotic resistance.<sup>23</sup> Molecular dynamics (MD) simulations and biochemical experiments carried out in our group have shown the unique resistance mechanism of the L28R mutant.<sup>22,24</sup> The extra hydrogen bonds formed dynamically between the L28R mutant (via residues R52, R57, and especially R28) and the glutamate tail of the DHF substrate lead to an increase in substrate affinity (Figure 1c), thus indirectly leading to TMP resistance. Based on this observation, we hypothesized that a more effective drug could be developed against strains carrying the L28R mutant by making a modification with a polar group at the para and meta positions of the trimethoxybenzene ring of TMP that would induce additional electrostatic and/or hydrogen-bonding interactions (Figure 1d).

Using this rationale, we synthesized an L28R-specific inhibitor by modifying the methyl group at the para (4') position to a polar hydroxyl group.<sup>25</sup> Among several other modifications, this new inhibitor (4'-deoxy trimethoprim; 4'-DTMP) was the only TMP derivative that was effective on both the wild type (WT) and the L28R mutant enzyme. Furthermore, under 4'-DTMP selection, the L28R mutation is largely eliminated, diverting the genetic trajectories to less resistant genotypes. In fact, the derivative exhibited 30–90-fold enhanced antimicrobial activity against isogenic *E. coli*-L28R compared to native TMP molecule. This study is important in terms of showing that it is possible to impede evolution of antibiotic resistance by blocking plausible evolutionary path-

ways with the most frequently observed mutant specific inhibitor (see Figure 4c in ref 25). Therein, TMP-bound WT and L28R structures were also elucidated by X-ray crystallography where TMP is bound to the orthosteric site.<sup>25</sup> In another study, we also showed that substrate-enzyme complex (DHF-bound DHFR) is synchronized at the precatalytic step and this behavior is governed by the active site residues which play a gating role, but the effects are propagated to the whole enzyme.<sup>26</sup>

If utilized to monitor the differences in the dynamics of a protein under varying conditions, MD simulations can inform on not only the thermodynamics but also kinetics of the system.<sup>27–29</sup> Therefore, to inspect the mechanistic effects of the inhibitor derivatives, here, we study TMP and 4'-DTMP in the WT and L28R mutant protein environments. Since the binding event is controlled by the hydrogen bonds, we first analyze the orthosteric site interactions for the WT and L28R mutant enzymes for each inhibitor. We supplement these with free energy difference calculations using the free energy perturbation (FEP) method which are also supported by experimental measurements.<sup>30,31</sup> We then expand our analysis protein-wide, by inspecting both the hydrogen bond occupancies and the formation of dynamical communities in the residue networks formed in this protein.<sup>26,32</sup>

## MATERIALS AND METHODS

**Parametrization of 4'-DTMP.** Trimethoprim derivatives were parametrized using the Force Field ToolKit (FFTK)<sup>33</sup> plugin implemented in Visual Molecular Dynamics (VMD).<sup>34</sup> The protocol used in our previous study<sup>24</sup> to parametrize TMP and TMP<sup>+</sup> was followed herein for the TMP derivative. All quantum mechanical calculations necessary for this protocol (optimization of charges, bonds, angles, and dihedrals) were performed by Gaussian09.<sup>35</sup>

Although it is known that TMP is neutral in water, it may also be in protonated form in the local protein environment depending on the mutant.<sup>36</sup> In our previous study, the simulations were conducted in the presence of both neutral

and protonated TMP (TMP<sup>+</sup>), and the protonation state was determined according to the maximum stabilization of the drug in the active site of DHFR.<sup>24</sup> Similarly, both neutral and protonated states of 4'-DTMP structures were parametrized in this work, and the resulting parameters are given in Table S1. We find the protonation state of 4'-DTMP to be the same as TMP; *i.e.*, it is protonated when bound both to the WT and to the mutant enzyme according to its hydrogen bonding profile (Figure S1). Therefore, in this study, only results from the protonated forms will be discussed.

**System Preparation.** All simulations were conducted with the NAMD program.<sup>37</sup> The water box was set to the dimensions of  $62 \times 68 \times 60$  Å with a padding of 10 Å TIP3P water layer in each direction. The salt concentration was set to isotonic conditions (0.15 M) by using K and Cl ions. The crystal structure was used in the closed conformation (PDB code 6XG5 and 6XG4) as the initial structure,<sup>25</sup> and the L28R mutation was introduced using the VMD Mutator Plugin.<sup>34</sup> Charmm36 parameter set<sup>38</sup> for proteins was utilized. The cofactor NADPH was present in all simulations. The systems were minimized for 10 000 steps. Particle mesh Ewald sum was utilized to calculate long-range electrostatics with a cutoff distance of 12 Å and a switching distance of 10 Å. The RATTLE algorithm was applied, and the Verlet algorithm was used with a time step of 2 fs. The temperature was controlled by Langevin dynamics with a dampening coefficient of 5 ps<sup>-1</sup>. The pressure was set to 1 atm, and the pressure was regulated by the Langevin piston. The resulting structures were subjected to two 210 ns long production runs as duplicates and a 1  $\mu$ s long run in the NPT ensemble. As in our previous work, the first 10 ns part of the trajectories was discarded for equilibration. The root mean squared deviation (RMSD) of the 210 ns-long and 1  $\mu$ s-long simulations are shown in Figures S2 and S3, respectively. The root mean fluctuation (RMSE) values are reported as averages over all 200 ns long chunks of the trajectories (Figure S4). RMSD values in the equilibrated portion of the trajectories are  $1.16 \pm 0.19$  and  $1.28 \pm 0.20$  for protonated WT<sup>TMP</sup> trajectories.

**Analysis of Hydrogen Bonds.** The hydrogen bonds were initially obtained via the Hydrogen Bond plugin implemented in VMD by setting the criteria for the formation of hydrogen bonds with an acceptor–donor heavy atom distance of 3.2 Å and a bond angle of 20°. Hydrogen bonds between the ligand and the protein were extracted using an in-house script that shows neighboring hydrogen bonds of selected residues, and the corresponding distances were calculated using a Tcl script on the TK console of the Visual Molecular Dynamics (VMD) program. For protein wide hydrogen bond occupancies, the method for acquiring hydrogen bonds was used as in ref 26 with an occupancy difference criteria of %20; these were the hydrogens bonds whose occupancies change by more than three standard deviations of the mean ( $\sigma = 6.6$ , Figure S5) which provide the fingerprints of the hydrogen bonds. To select those with significant deviations from the WT, we also calculated errors on these occupancy changes by splitting the 1  $\mu$ s trajectory into five chunks of 200 ns each. Bonds that show less than  $2\sigma$  fluctuation were chosen for further refinement (Table S2).

**Alchemical Free Energy Perturbation Calculations.** Zwanzig's formulation<sup>30</sup> was followed for all the free energy difference calculations. A soft-core potential was introduced to the Lennard-Jones potential by truncating the potential function shifting van der Waals radius 2 Å for reducing

singularities occurring during the calculations. Dual topology was used for the TMP<sup>+</sup> to 4'-DTMP<sup>+</sup> conversions. Initial conformations from seven different time points of the MD simulations were used in sampling to enhance the coverage of the potentially available conformational states. All calculations were carried out with the Charmm36 force field. Particle mesh Ewald sum was employed to control the electrostatics. Langevin piston was used for pressure control. Switching was implemented with a cutoff of 13 Å and a switching distance of 10 Å. The time step was set to 2 fs. The SHAKE algorithm was used for all bonds. Systems were equilibrated for 0.5 ns posterior to 500 steps of minimization. The window size was set to 0.2 ns, 0.1 ns being the window for equilibration. The systems were run for 32 windows in forward and backward simulations. Acquired results were merged and analyzed by the multistate Bennett-acceptance ratio (MBAR)<sup>31</sup> method using the established protocol.<sup>39</sup>

**Dynamical Community Composition.** Residue networks (RNs) were built by using a frame for every 10 ns of the last 100 ns part of each trajectory.  $C_{\beta}$  ( $C_{\alpha}$  for Glycine) atoms were taken as nodes for the amino acids. C2 atom (Table S1) was used as a node for TMP and 4'-DTMP. Hence, the graphs were constructed with a total number of 160 nodes, and 6.7 cutoff was used to add a link between a pair of nodes. Resulting RNs were undirected and did not have self-loops. Girvan-Newman algorithm<sup>40,41</sup> was employed to separate the protein into six communities ( $\Omega = 6$ ) in each snapshot. This algorithm searches for communities by breaking the most central (highest betweenness centrality) edge in each iteration. The calculations were repeated for the equally spaced frames obtained from the MD trajectories. Three well-separated nodes were then selected to visualize the dynamical communities. These represent two locations at the outskirts of each of the LD (N142) and ABD (S64), and one bridging the two domains (I94). Red-green-blue (RGB) scores were accumulated on these three residues such that for each snapshot, if a residue was in the same community as one of these three residues, the color belonging to that residue (I94, N142, and S64 for red, blue, and green, respectively) was incremented by one. Dynamic community composition was then projected on the three-dimensional protein structure by using the normalized (to 256) color score of each residue. For example, if a residue was always in the same community as I94 (RGB value 256,0,0), it was colored red; if another residue was in the same community with I94 and N142 50% of the time each (RGB value 128,0,128), it was colored magenta. See ref 32 for more details.

**Protein Overexpression and Purification.** The L28R mutation in folA gene was constructed by using the Quick-Change Site-Directed Mutagenesis kit (Stratagene). SixXHisTag was added at the C-termini of the protein sequence for the WT and L28R constructs. The constructs were cloned into expression plasmids pET24a-KanR. BL21 *E. coli* cells were transformed with pET24a-folA-6XHisTag and were grown overnight in selective media (LB + Kan) and then diluted 100 times into Terrific Broth (TB) media for further growth at 37 °C. Protein overexpression was induced when OD600 reached 0.6–0.8, using 250 mM isopropyl  $\beta$ -D-1-thiogalactopyranoside (IPTG) per 1 L of the medium, and the temperature was decreased to 18 °C for overnight growth, with 230 rpm shaking. Recombinant protein was purified using Ni-NTA columns (Qiagen), dialyzed overnight against 50 mM Tris-HCl, 300 mM NaCl, 0.5 mM tris(2-carboxyethyl)phosphine

(TCEP), pH 8, and further purified using size-exclusion chromatography.

**Steady-State Kinetic Measurements.** We followed the protocol outlined in our previous work.<sup>22</sup> Briefly, in the DHFR reaction, reactants DHF (Sigma-Aldrich D7006) and NADPH (Sigma-Aldrich N7505) have light absorption at 340 nm wavelength, where the products THF and NADP<sup>+</sup> do not absorb light at this wavelength. The reaction concentrations were quantitated using extinction coefficients of 28 mM<sup>-1</sup> cm<sup>-1</sup> for DHF at 282 nm and 6.22 mM<sup>-1</sup> cm<sup>-1</sup> for NADPH at 340 nm. The reactions were run in MTEN buffer (50 mM 2-(N-morpholino) ethanesulfonic acid, 25 mM tris base, 25 mM ethanolamine, 100 mM NaCl) pH 7.00, and 5 mM dithiothreitol (DTT, Fisher Scientific BP172-25) was added freshly before starting the reaction. MTEN solution with 150 nM DHFR protein and 200 mM NADPH was prepared. Reaction progression was measured using UV/vis Spectrophotometer (PerkinElmer LAMBDA 650) with 1 s time intervals for two cells. The first cuvette contained the reaction components (DHFR, DHF, and NADPH), and the second cuvette was the reference used for background correction which contained only MTEN and DTT. The reaction concentration for DHF in the first cuvette was 12.5  $\mu$ M, and the data was collected until DHF was consumed completely, which happens when the curve reaches plateau. To observe the effect of TMP and 4'-DTMP on the reactions, 12.5  $\mu$ M DHF consumption measurements were used as control. The consumption of 12.5  $\mu$ M DHF was measured in either WT and L28R mutant in the presence of either TMP or 4'-DTMP. The inhibitor concentration was 500 nM in each case, and all measurements were done in duplicate.

## RESULTS AND DISCUSSION

**Relative Binding Energies Reveal Similar Energetic Cost for 4'-DTMP and TMP Binding to WT and L28R Mutant.** 4'-DTMP was designed<sup>25</sup> based on our observation that the L28R mutant of DHFR establishes dynamical hydrogen bonds with the substrate DHF in the precatalytic step<sup>22,24</sup> and that a TMP derivative exploiting similar dynamics might be effective on both the WT and the mutant enzyme. This observed effect was shown to be of kinetic origin,<sup>24</sup> as the free energy difference calculated for binding to WT vs L28R mutants was  $1.2 \pm 1.4$  kcal mol<sup>-1</sup> for DHF and  $0.6 \pm 1.1$  kcal mol<sup>-1</sup> for TMP. Therein, the calculations were carried out via steered MD simulations. Due to the similarity in the structures of TMP and 4'-DTMP, here we can calculate the thermodynamics of their relative binding with high accuracy using FEP.

The thermodynamic cycle constructed to compute relative free-energy changes due to ligand binding is illustrated in Figure 2. In these cycles, the vertical energy differences ( $\Delta G_{\text{bind, TMP}/4'\text{-DTMP}}$ ) can be obtained from experimental binding affinities using the relation  $\Delta G = -RT \ln K_i$  (Table 1). The horizontal ones ( $\Delta G_{\text{TMP} \to 4'\text{-DTMP}}$ ) are the theoretical values obtained through FEP simulations.

Experimentally, we find that, while binding to the protein is tighter in the WT than the mutant, they are all in the nanomolar range for both inhibitors. Moreover, our calculations have led to the results,  $\Delta G_{\text{TMP} \to 4'\text{-DTMP}}^{\text{WT}} = -3.2 \pm 0.3$  kcal/mol and  $\Delta G_{\text{TMP} \to 4'\text{-DTMP}}^{\text{L28R}} = -3.4 \pm 0.4$  kcal/mol.

The relative effect of the inhibitors may be obtained from the difference:  $\Delta \Delta G = \Delta G_{\text{TMP} \to 4'\text{-DTMP}}^{\text{WT, bound}} - \Delta G_{\text{TMP} \to 4'\text{-DTMP}}^{\text{L28R, bound}}$ . Employing the outermost and innermost cycles from

![Figure 2: Illustration of mutation and ligand binding thermodynamic cycles of two inhibitors to DHFR. The diagram shows two cycles: one for WT (light gray enzyme) and one for L28R (darker gray enzyme). Each cycle compares the binding of TMP (burgundy ligand) and 4'-DTMP (fuchsia ligand). The vertical values (ΔG_bind) are experimental, and the horizontal values (ΔG_TMP→4'-DTMP) are computed. The values are: WT: ΔG_bind,TMP = -11.4 kcal/mol, ΔG_bind,4'-DTMP = -11.3 kcal/mol, ΔG_TMP→4'-DTMP = -3.2 ± 0.3 kcal/mol. L28R: ΔG_bind,TMP = -9.8 kcal/mol, ΔG_bind,4'-DTMP = -10.2 kcal/mol, ΔG_TMP→4'-DTMP = -3.4 ± 0.4 kcal/mol.](32acdaad6c921e80fd17e42562858b80_img.jpg)

Figure 2: Illustration of mutation and ligand binding thermodynamic cycles of two inhibitors to DHFR. The diagram shows two cycles: one for WT (light gray enzyme) and one for L28R (darker gray enzyme). Each cycle compares the binding of TMP (burgundy ligand) and 4'-DTMP (fuchsia ligand). The vertical values (ΔG\_bind) are experimental, and the horizontal values (ΔG\_TMP→4'-DTMP) are computed. The values are: WT: ΔG\_bind,TMP = -11.4 kcal/mol, ΔG\_bind,4'-DTMP = -11.3 kcal/mol, ΔG\_TMP→4'-DTMP = -3.2 ± 0.3 kcal/mol. L28R: ΔG\_bind,TMP = -9.8 kcal/mol, ΔG\_bind,4'-DTMP = -10.2 kcal/mol, ΔG\_TMP→4'-DTMP = -3.4 ± 0.4 kcal/mol.

**Figure 2.** Illustration of mutation and ligand binding thermodynamic cycles of two inhibitors to DHFR. The upper and lower cycles represent the binding of ligands TMP and 4'-DTMP to WT and L28R, respectively. Enzymes are depicted in pacman style, representing WT in light gray and L28R in darker gray. The ligands of each type are represented by burgundy and fuchsia. Throughout the text, we kept the same coloring for TMP (burgundy) and 4'-DTMP (fuchsia). Vertical values are from experiments; horizontal ones are computed. Created with BioRender.com.

**Table 1. Experimental Binding Affinities and Corresponding Calculated Binding Free Energies**

| protein | inhibitor | $K_i$ (nM) <sup>a</sup> | $\Delta G$ (kcal/mol) | label                                           |
|---------|-----------|-------------------------|-----------------------|-------------------------------------------------|
| WT      | TMP       | $4.2 \pm 0.5$           | $-11.5 \pm 0.1$       | $\Delta G_{\text{bind, TMP}}^{\text{WT}}$       |
| WT      | 4'-DTMP   | $5.1 \pm 1.0$           | $-11.4 \pm 0.1$       | $\Delta G_{\text{bind, 4'-DTMP}}^{\text{WT}}$   |
| L28R    | TMP       | $65.0 \pm 7.5$          | $-9.9 \pm 0.1$        | $\Delta G_{\text{bind, TMP}}^{\text{L28R}}$     |
| L28R    | 4'-DTMP   | $34.3 \pm 2.9$          | $-10.3 \pm 0.1$       | $\Delta G_{\text{bind, 4'-DTMP}}^{\text{L28R}}$ |

<sup>a</sup>From ref 25.

Figure 2, and plugging in the measured/calculated values we get,

$$\begin{aligned}\Delta \Delta G &= (\Delta G_{\text{bind, 4'-DTMP}}^{\text{L28R}} - \Delta G_{\text{bind, TMP}}^{\text{L28R}}) \\ &- (\Delta G_{\text{bind, 4'-DTMP}}^{\text{WT}} - \Delta G_{\text{bind, TMP}}^{\text{WT}}) = -0.5 \text{ kcal/mol} \\ &= (\Delta G_{\text{TMP} \to 4'\text{-DTMP}}^{\text{L28R}} - \Delta G_{\text{TMP} \to 4'\text{-DTMP}}^{\text{WT}}) \\ &= -0.2 \pm 0.7 \text{ kcal/mol}\end{aligned}$$

Thus, both the experiments of ref 25 and our calculations point out that the effect of the mutation is thermodynamically similar for the two inhibitors. Therefore, the 30–90-fold enhanced activity in the inhibition of the L28R mutant by 4'-DTMP we previously observed<sup>25</sup> must have kinetic origins.

**Steady-State Kinetic Measurements Point out an Inhibitory Difference for TMP and 4'-DTMP.** In kinetic assays, we measured the consumption of DHF in the absence and presence of the inhibitors (Figure 3). The initial DHF concentration was 12.5  $\mu$ M, and these assays were performed for WT and L28R mutant enzymes. DHF was consumed in 30 s in control experiments in the absence of any inhibitor for WT DHFR. When 500 nM TMP and 4'-DTMP molecules were added, we did not observe any DHF consumption; *i.e.*, the enzyme is completely inhibited. This is in accordance with the 4–5 nM  $K_i$  values of these drugs for the WT. On the other hand, in the DHF consumption control experiment for the

![Figure 3: Kinetic assays for WT and L28R mutant enzyme. The figure consists of two line graphs. The left graph is for WT and the right graph is for L28R. Both graphs plot DHF concentration (μM) on the y-axis (0 to 12) against Time (min) on the x-axis (0.0 to 2.0 for WT, 0.0 to 3.5 for L28R). A dotted line at 12.5 μM represents the initial concentration. Gray curves represent controls without inhibitors. Colored curves represent systems with 500 nM inhibitors: DHF (gray), DHF+TMP (purple), DHF+TMP (blue), and DHF+4'DTMP (red). Raw data points are shown as circles, and lines guide the eye. In the L28R graph, the DHF+4'DTMP curve is the highest, followed by DHF+TMP, then DHF, and the control is the lowest.](6de7dcb072cef2388026fb0f504084b2_img.jpg)

Figure 3: Kinetic assays for WT and L28R mutant enzyme. The figure consists of two line graphs. The left graph is for WT and the right graph is for L28R. Both graphs plot DHF concentration (μM) on the y-axis (0 to 12) against Time (min) on the x-axis (0.0 to 2.0 for WT, 0.0 to 3.5 for L28R). A dotted line at 12.5 μM represents the initial concentration. Gray curves represent controls without inhibitors. Colored curves represent systems with 500 nM inhibitors: DHF (gray), DHF+TMP (purple), DHF+TMP (blue), and DHF+4'DTMP (red). Raw data points are shown as circles, and lines guide the eye. In the L28R graph, the DHF+4'DTMP curve is the highest, followed by DHF+TMP, then DHF, and the control is the lowest.

**Figure 3.** Kinetic assays for WT and L28R mutant enzyme. Initial DHF concentration in each case is  $12.5 \mu\text{M}$  (dotted lines). Gray curves are the controls in the absence of inhibitors; colored curves are for the systems under competitive inhibition of the  $500 \text{ nM}$  drug. Experiments are done in duplicate; raw data are shown in circles; lines guide the eye.

![Figure 4: L28R variant of DHFR forms additional and stronger hydrogen bonds with 4'-DTMP compared to TMP. (a) Bar charts for WT and L28R showing H-Bond Distance (Å) for various atom pairs (N18O, M20N, W22O, D27O, S49O, R52NH1, R52NH2) with TMP (purple) and 4'-DTMP (red). 4'-DTMP consistently shows shorter distances. (b) Bar charts for L28R showing H-Bond Distance (Å) for R28 interactions (R28NE, R28NH1, R28NH2) with TMP (purple) and 4'-DTMP (red). 4'-DTMP shows significantly shorter distances. (c) Zoomed-in structural representations of the interactions, showing the ligand (purple/red) and residues (gray) with dashed lines indicating hydrogen bonds. The color code for inhibitors is consistent across the charts and structures.](6bbc398f520a7bcc5491cab18d3e4cac_img.jpg)

Figure 4: L28R variant of DHFR forms additional and stronger hydrogen bonds with 4'-DTMP compared to TMP. (a) Bar charts for WT and L28R showing H-Bond Distance (Å) for various atom pairs (N18O, M20N, W22O, D27O, S49O, R52NH1, R52NH2) with TMP (purple) and 4'-DTMP (red). 4'-DTMP consistently shows shorter distances. (b) Bar charts for L28R showing H-Bond Distance (Å) for R28 interactions (R28NE, R28NH1, R28NH2) with TMP (purple) and 4'-DTMP (red). 4'-DTMP shows significantly shorter distances. (c) Zoomed-in structural representations of the interactions, showing the ligand (purple/red) and residues (gray) with dashed lines indicating hydrogen bonds. The color code for inhibitors is consistent across the charts and structures.

**Figure 4.** L28R variant of DHFR forms additional and stronger hydrogen bonds with 4'-DTMP compared to TMP. Average distances between the ligands and the binding site of WT and L28R for selected atom pairs; since the hydrogen bond distance definition is  $3.2 \text{ \AA}$ , values less than  $6 \text{ \AA}$  imply formation of frequent hydrogen bonds in the dynamical trajectories. (a) Trimethoxybenzene tail and the surrounding loop interactions; (b) R28 interactions with the ligand. Zoomed-in representations of these interactions are also displayed on the structures on the right, with the same color code for the inhibitors.

![Figure 5: Inhibitors share enzyme interactions but prefer different dynamic conformations. (a) Interactions of active site residues with TMP (purple) and 4'-DTMP (pink) in both WT and L28R at the end of one of the replicated 210 ns trajectories. (b) Superposition of the interactions of the inhibitors with the WT (top) and L28R variant (bottom).](55807fe92060150f5307fea4a40e00ad_img.jpg)

Figure 5 consists of two panels, (a) and (b). Panel (a) shows four molecular docking models of the DHFR enzyme active site. The top row shows the wild-type (WT) enzyme with TMP (purple) and 4'-DTMP (pink) bound. The bottom row shows the L28R mutant with the same inhibitors. Labels indicate residues S49, R52, M18, M20, D27, and W22. Panel (b) shows a superposition of the inhibitor binding poses for WT (top) and L28R (bottom), highlighting differences in the conformation of the R52 side chain and the TMP molecule.

Figure 5: Inhibitors share enzyme interactions but prefer different dynamic conformations. (a) Interactions of active site residues with TMP (purple) and 4'-DTMP (pink) in both WT and L28R at the end of one of the replicated 210 ns trajectories. (b) Superposition of the interactions of the inhibitors with the WT (top) and L28R variant (bottom).

**Figure 5.** Inhibitors share enzyme interactions but prefer different dynamic conformations. (a) Interactions of active site residues with TMP (purple) and 4'-DTMP (pink) in both WT and L28R at the end of one of the replicated 210 ns trajectories. Note how the R52 side chain that turns away from the binding cavity in the L28R<sup>TMP</sup> system is held in place by the 4'-DTMP. Also, TMP has alternative conformations, while 4'-DTMP has a single stable pose. (b) Superposition of the interactions of the inhibitors with the WT (top) and L28R variant (bottom).

![Figure 6: Enhancement of pyrimidine ring interactions through trimethoxy tail stabilization. Barcode graphs for the hydrogen bonds between binding cavity residues and TMP and 4'-DTMP for WT and L28R were obtained from the 1 μs-long MD trajectory; similar statistics hold for the duplicated 210 ns-long trajectories. A value of one is assigned if there is at least one hydrogen bond between any atom of the residue and the ligand and zero if there is no interaction. These interactions with the inhibitors are displayed on the structures on the right of each barcode graph.](0ad3f61f997eb05afb341fc46024bf2b_img.jpg)

Figure 6 displays four barcode graphs and their corresponding molecular structures. The top row shows WT<sup>TMP</sup> (left) and WT<sup>4'-DTMP</sup> (right). The bottom row shows L28R<sup>TMP</sup> (left) and L28R<sup>4'-DTMP</sup> (right). The barcodes represent the occupancy of hydrogen bonds over time (0 to 1000 ns) for residues ILE5, ALA6, MET20, ASP27, LEU28, and THR113. The structures on the right show the specific residues (I5, A6, T113, M20, D27, R28) and the inhibitors (TMP or 4'-DTMP) in their binding poses.

Figure 6: Enhancement of pyrimidine ring interactions through trimethoxy tail stabilization. Barcode graphs for the hydrogen bonds between binding cavity residues and TMP and 4'-DTMP for WT and L28R were obtained from the 1 μs-long MD trajectory; similar statistics hold for the duplicated 210 ns-long trajectories. A value of one is assigned if there is at least one hydrogen bond between any atom of the residue and the ligand and zero if there is no interaction. These interactions with the inhibitors are displayed on the structures on the right of each barcode graph.

**Figure 6.** Enhancement of pyrimidine ring interactions through trimethoxy tail stabilization. Barcode graphs for the hydrogen bonds between binding cavity residues and TMP and 4'-DTMP for WT and L28R were obtained from the 1  $\mu$ s-long MD trajectory; similar statistics hold for the duplicated 210 ns-long trajectories. A value of one is assigned if there is at least one hydrogen bond between any atom of the residue and the ligand and zero if there is no interaction. These interactions with the inhibitors are displayed on the structures on the right of each barcode graph.

L28R mutant, we observed a slower trend continuing for a few minutes. Since WT protein is optimized for the environmental conditions, the slower reaction kinetics for L28R is expected; in fact, the more resistant mutants of bacteria are likely to grow slower than WT, introducing a resistance cost.<sup>42</sup> When 500 nM inhibitors are added to the mutants, both are able to introduce a slowing down in product release, more so for 4'-DTMP than for TMP. Thus, the slight edge introduced by 4'-DTMP on the L28R mutant finds its origins in these kinetic differences. We next explore the modified interactions in the dynamics of inhibitor bound DHFR to illuminate this point.

**Hydrogen Bond Occupancies Differentiate Binding Modes of the Two Inhibitors.** To elucidate the mechanism of binding of the new inhibitor and thus to highlight the interactions responsible for its enzymatic activity, a detailed hydrogen bond analysis in the WT and L28R mutant of *E. coli* DHFR with TMP derivatives has been conducted by analyzing the MD simulations for each system.

In the crystal structure of WT<sup>TMP</sup> and L28R<sup>TMP</sup> (PDB codes 6XG5 and 6XG4<sup>25</sup>), the pyrimidine ring of TMP is stabilized by the backbone oxygen atoms of I5 and I94 and the side chains of D27, Y100, and T113, whereas the trimethoxybenzene ring is stabilized via the side chain of S49 (also see

Figure S1). We monitored the average hydrogen bond distances in the WT and the L28R mutant in the presence of TMP and its derivative 4'-DTMP. The hydrogen bonds established between the 2,4-diamino pyrimidine ring of the ligand and the active site residues of the protein are highly conserved, contributing to the stabilization of the ligand within the active site of DHFR (Figure S1). While the pyrimidine ring of the ligand is stabilized with strong hydrogen bonds both in WT and in L28R, we observe a dynamic stabilization of the trimethoxybenzene ring of the ligand. Residues N18, M20, W22, D27, S49, and R52 come in proximity occasionally and sometimes lose their contact resulting in larger average values for the contacts determining hydrogen bond distances. In particular, N18, M20, and W22 show significant changes in hydrogen bonding distances in both WT and L28R for 4'-DTMP (Figure 4a). On the other hand, for the L28R mutant, the most fundamental difference is the interactions of oxygen atoms at the 4' and 5' positions on the inhibitors with the R28 atoms whereby frequent strong interactions are formed with 4'-DTMP, which do not form with TMP (Figure 4b).

That the pyrimidine ring in both WT and L28R shares the same binding partners while the trimethoxybenzene ring is stabilized by dynamic interactions in the latter is depicted in Figure 5. We observe a highly dynamic trimethoxy tail for TMP, even displaying rotational jumps between two ring conformations during a given 200 ns-long trajectory, constantly making and breaking hydrogen bond contacts. Conversely, 4'-DTMP is lodged in place due to the effect of the N18, M20, W22 and, in the case of L28R, R28 interactions.

Figure 6 displays the time trace of residues that are hydrogen bonded to the inhibitors for more than 10% of the time in any one of the trajectories. In all systems, the pyrimidine ring is stabilized predominantly by D27 supported by the dynamical interplay with I5, A6, and T113 residues. We observe that interactions are slightly decreased for D27 in 4'-DTMP proteins due to inclusion of additional binding partners. In the L28R mutant, there are additional interactions of the tail of 4'-DTMP due to positively charged arginine residue in the vicinity. With the stabilization of the tail of the ligand for 4'-DTMP, the pyrimidine ring is further immobilized in the active site, quantified with an increase in the occupancies, particularly for A6 (from 16 to 20% to 33–35%). In the presence of 4'-DTMP, there is a significant enhancement of the T113–inhibitor interactions, from 9 to 21% in the WT and from 30 to 42% in L28R. T113 engages the pyrimidine ring (Figure S1), and additional stabilization of the trimethoxy tail ensures further stabilization of this portion of the inhibitor.

**Changes in Local Dynamics Propagates to Total Enzyme Motions and Expose the Dynamical Mechanism of Action.** We next question if these increased local dynamical interactions between the enzyme and the inhibitor permeate the rest of the protein by examining the cross-correlation maps (Figure S6). We find that for either of the inhibitor bound forms, the L28R mutation reinforces both positive and negative correlations observed across the enzyme (comparing upper and lower maps in Figure S6). On the other hand, the modification of the inhibitor from TMP to 4'-DTMP substantially increases the negative correlations of the GH loop (residues 142–150) with the rest of the protein (blue vertical/horizontal stripe in the second column correlation maps). In fact, 4'-DTMP suppresses correlations occurring elsewhere in the system (compare the shades of red/blue from left to right), except for the positive correlations between CD (residues 64–

71) and GH loops. We note that we have previously observed that CD loop has allosteric effects on DHFR dynamics.<sup>26</sup> Thus, although binding free energy differences are comparable, there are important mechanism changes due to both the mutation and ligand modification that are only reflected in the dynamics of the enzyme.

**Dynamic Interplay between Allosteric Regions Determines Enzyme Inhibition Outcomes.** Our previous work on DHFR mutational landscape has irrevocably put forth that one needs to analyze the dynamical behavior of this enzyme in the presence of its various ligands to fully explain its behavior.<sup>22</sup> To answer the question of how the different regions in the enzyme are connected, we first resort to construct a visual of the community structures in the trajectories. To achieve this, we have selected three residues that predominantly remain in separate communities and are also far apart from each other; S64, I94, and N142. These are assigned the color codes blue, red, and green, respectively. Residues that remain in the same community are represented as single colors (red, green, or blue); otherwise, they appear in mixed colors reflected on the three-dimensional protein structures in Figure 7.

![Figure 7: Distinct communities imply segmentation. (a) Schematic summarizing community analysis. (b) Dynamic communities illustrate the community sharing for WT and L28R bound forms with TMP and 4'-DTMP.](da31c47c21ba3492d3df8a49462b9238_img.jpg)

Figure 7 consists of two panels. Panel (a) is a schematic showing a protein structure (represented as a mesh) being projected onto a graph. The graph nodes are labeled with letters A through H, representing different regions of the protein. Panel (b) shows four 3D protein structures: WT-TMP, WT-4'-DTMP, L28R-TMP, and L28R-4'-DTMP. The structures are colored based on community membership. In the WT-TMP structure, residues S64, I94, and N142 are highlighted in blue, red, and green respectively. In the WT-4'-DTMP structure, these residues are highlighted in blue, red, and green respectively. In the L28R-TMP structure, residues S64, I94, and N142 are highlighted in blue, red, and green respectively. In the L28R-4'-DTMP structure, residues S64, I94, and N142 are highlighted in blue, red, and green respectively.

Figure 7: Distinct communities imply segmentation. (a) Schematic summarizing community analysis. (b) Dynamic communities illustrate the community sharing for WT and L28R bound forms with TMP and 4'-DTMP.

**Figure 7.** Distinct communities imply segmentation. a) Schematic summarizing community analysis. First, a protein structure is projected onto a graph by taking  $C_\beta$  ( $C_\alpha$  for glycine) as nodes and connected by links if they are within a cutoff distance of 6.7 Å. Then, by iteratively cutting the most central links, segmentation into communities is computed for each MD snapshot. Coloring is directly proportional to a residue belonging to the selected reference RGB nodes over the entirety of the trajectory (I94 = red, N142 = green, S64 = blue). b) Dynamic communities illustrate the community sharing for WT and L28R bound forms with TMP and 4'-DTMP.

We first note that in all the systems, the ABD is colored purple-magenta indicating that it shares communities with the binding site (red). Community structures indicate in L28R<sup>TMP</sup> that the LD is split into three independent regions (pure red, pure green, and black colors) throughout the trajectory. This suggests that these regions are dynamically independent from each other, not sharing communication pathways during the

![Figure 8: Three molecular models of DHFR complexes. The left model is L28R^TMP, showing residues R57, T35, T46, I50, N147, and D144 in green (decreased occupancy). The middle model is WT^4'DTMP, showing residues R158, D139, K109, Y111, A16, and M19 in blue (increased occupancy). The right model is L28R^4'DTMP, showing residues R44, E48, R158, D132, D127, R28, A16, M19, and N147 in green and blue. The models illustrate how a hairpin in the M20 loop manipulates internal communication pathways.](86bc87f7876d150f4ca9684c6848082f_img.jpg)

Figure 8: Three molecular models of DHFR complexes. The left model is L28R^TMP, showing residues R57, T35, T46, I50, N147, and D144 in green (decreased occupancy). The middle model is WT^4'DTMP, showing residues R158, D139, K109, Y111, A16, and M19 in blue (increased occupancy). The right model is L28R^4'DTMP, showing residues R44, E48, R158, D132, D127, R28, A16, M19, and N147 in green and blue. The models illustrate how a hairpin in the M20 loop manipulates internal communication pathways.

**Figure 8.** Hairpin formed on the M20 loop manipulates internal communication pathways of DHFR. Hydrogen bonded pairs whose occupancies change by more than 20% with respect to the WT<sup>TMP</sup>. Green: decrease in occupancy; blue: increase in occupancy.

time scale of the observations (1  $\mu$ s). Thus, in L28R<sup>TMP</sup> the binding site is isolated from the rest of the LD so that the allosteric role of the CD loop is abolished. This situation contrasts with the rest of the systems, where various other color tones emerge in the LD.

One can be conjectured that it is easier to separate the ABD from the LD in this scenario so that the barrier to inhibitor release is lowered, rendering the inhibition of L28R by TMP unsuccessful so that the protein remains functional. Based on this finding, we hypothesize that isolation of the communities belonging to the CD loop and E helix is necessary to confer resistance. Considering that TMP disrupts the function of WT DHFR, the purple-red color of F helix in WT<sup>TMP</sup> and L28R<sup>4'-DTMP</sup> further indicates that the community sharing between ABD and LD is another successful indicator of inhibition of the enzyme. Furthermore, the C-termini of WT<sup>TMP</sup>, L28R<sup>TMP</sup>, and L28R<sup>4'-DTMP</sup> complexes do not share communities with other parts of the protein by being colored in black. This community structure might be one explanation as to why the C-terminus is independent of the rest of protein dynamics during the product release step.<sup>43</sup> WT<sup>4'-DTMP</sup> differs from the other three systems in this respect, where the C-terminus shares a community with I94 on the F helix.

We find that the dominant factors that contribute to the shifts in communities are those hydrogen bonds in the overall system that display significant changes in their occupancies. We thus resort to tracking residue pairs which consistently shift their hydrogen bond occupancies with respect to the WT<sup>TMP</sup> by more than 20% (see Table S2 for selection criteria and process). The results are listed in Figure 8. In L28R<sup>TMP</sup>, the decreased occurrence (green spheres) of T46-I50 and T35-R57 in the ABD leads to the increased fluctuations in the C helix (Figure S4). The significant loss of the D144-N147 interaction in the GH loop of the LD further contributes to the long-range communication with the CD loop which modulates its allosteric character. Together, they lead to the isolated communities of the LD in Figure 7.

For the WT<sup>4'-DTMP</sup> and L28R<sup>4'-DTMP</sup> systems, there is generally a decrease in some of the C-termini interactions compensated by the newly formed A16-M19 interaction (Figure 8). The hairpin formed between A16 and M19 creates a hybrid conformation of the loop which is connected to the bound ligand. This rigidification of the M20 loop might be responsible for slowing down the inhibitor release step. While there is significant overlap in the residues involved at C-termini

hydrogen bond occupancy loss, others require further inspection. The loss of the E90–K109–Y111 network in WT<sup>4'-DTMP</sup> could be providing the flexibility necessary for increasing the communication pathways present in the enzyme, so that the allosteric communication between the CD–GH loops prevails. Otherwise, the systems need to acquire additional flexibility in the GH loop (see the bond D144–N147 in L28R<sup>4'-DTMP</sup>). With the introduction of R28 in L28R<sup>4'-DTMP</sup>, the further branching of binding partners introduces attenuation in the binding occupancies overall shifting M20 loop toward the binding site which results in the loss of R12-D127 bond. These motions then lead to the blending of the binding region motions with the ABD completely, reaching all the way to the CD loop, which we have previously predicted to be an important allosteric communicator in DHFR,<sup>26</sup> also corroborated with enhanced cross correlations (Figure S6).

In sum, maintaining the delicate balance of the interaction network in DHFR seems to be the key to the success of an inhibitor and is a mechanism also exploited by resistance-conferring mutations. Thompson et al. find that the destabilization of the enzyme is found in most of the advantageous mutations and the mutants are thought to function through accelerated breathing motions which eases the way of product release.<sup>44</sup> In fact, the increased hydrogen bond occupancy of 4'-DTMP with N18, M20, and W22 in the M20 loop is the only logical source of the hydrogen bond rupturing. Sawaya and Kraut point out that when the M20 loop changes conformation, the hydrogen bonds between the M20 loop and FG loop (G15-D122 in the closed state, E17-D122 in the open state) rupture and the new bond between GH and M20 loop (N23–S148 in the occluded state) forms.<sup>45</sup> Here we see similar behavior between the domains, albeit not permanently as in those discussed X-ray structures but dynamically.

## CONCLUSIONS

DHFR is a highly flexible and dynamic protein with many allosteric residues.<sup>46–48</sup> The effective TMP derivative, 4'-DTMP, developed specifically toward steering evolutionary trajectories away from the L28R mutation which emerges frequently under TMP pressure, is studied along with MD and FEP simulations. Using both experimental and computational means, we find that the two inhibitors are thermodynamically similar to comparable binding energy differences between the

WT and L28R systems. This leaves alteration of the kinetics as the most plausible means for explaining the 30–90-fold enhanced antimicrobial activity<sup>25</sup> which might be due to, e.g., modified dissociation pathways or increased kinetic barriers in the reaction steps. We therefore seek to understand the underlying dynamic causes of the effectiveness of the derivative. We first analyze the local interactions and find that the original design parameter that targeted a polar modification in TMP indeed caused the formation of extra hydrogen bonds with L28R, and these interactions were demonstrated in MD simulations.

For the inhibition of DHFR in the orthosteric site, we elucidated that dynamic stabilization of the inhibitor is crucial to slow down the functioning of the L28R mutant. Enhanced M20 loop interactions with the trimethoxy tail are triggered in addition to those intended with the R52 region during the design of the inhibitor (Figures 4a and 5). In addition, the enhancement of hydrogen bonds with the pyrimidine ring through A6 and T113 shows that there is also an intrinsic effect due to the charge density of the polar group added to the molecule. However, this effect is not significant, since we do not see any change in the inhibitory behavior in the WT.

We next focused on how these local interactions propagated to the total enzyme. Our community analyses showed that the community separation in L28R<sup>TMP</sup> indicates a distinct communication regime utilizing segmentation of the enzyme, which causes the recovery of the function. On the other hand, the community composition of WT<sup>TMP</sup> and L28R<sup>4DTMP</sup> displays long-range slow-motion communication, which results in inhibition. This is because, the further the coverage of the dynamical hydrogen bond network, the slower will be the breathing motions which play a role in ligand release.<sup>44</sup>

In this study, we have put forth the atomistic scale mechanism of action of the 4'-DTMP that is effective on a high resistance-conferring mutant of DHFR. This is a proof-of-concept work that shows that focusing on the dynamical mutant-inhibitor interactions through computational means can save time and money for practical designs for strains that need urgent preventive measures due to antibiotic resistance.

## ■ ASSOCIATED CONTENT

### Data Availability Statement

All codes used for the analyses presented here can be found at [https://github.com/midstlab/JCIM\\_Cetin\\_et\\_al\\_2023](https://github.com/midstlab/JCIM_Cetin_et_al_2023) (those for Figures 2, 4, 6, and 8) and [https://github.com/midstlab/JCIM\\_Cetin\\_et\\_al\\_2023\\_community](https://github.com/midstlab/JCIM_Cetin_et_al_2023_community) (those for Figure 7). The trajectories are listed at <https://zenodo.org/record/7966540>.

### ■ Supporting Information

The Supporting Information is available free of charge at <https://pubs.acs.org/doi/10.1021/acs.jcim.3c00818>.

Force field parameters for 4'-DTMP derivatives (Table S1), hydrogen occupancy data and distributions (Table S2 and Figure S5), enzyme-ligand interactions (Figure S1), RMSD, RMSF and cross-correlations from MD simulations (Figures S2–S4, S6) (PDF)

## ■ AUTHOR INFORMATION

### Corresponding Authors

**Burcu Dedeoglu** – Department of Chemistry, Gebze Technical University, Gebze 41400 Kocaeli, Turkey; [orcid.org/0000-0001-9504-2913](https://orcid.org/0000-0001-9504-2913); Email: [b.dedeoglu@gtu.edu.tr](mailto:b.dedeoglu@gtu.edu.tr)

**Canan Atilgan** – Faculty of Engineering and Natural Sciences, Sabanci University, Tuzla 34956 Istanbul, Turkey;

[orcid.org/0000-0003-0557-6044](https://orcid.org/0000-0003-0557-6044); Email: [canan@sabanciuniv.edu](mailto:canan@sabanciuniv.edu)

### Authors

**Ebru Cetin** – Faculty of Engineering and Natural Sciences, Sabanci University, Tuzla 34956 Istanbul, Turkey;

[orcid.org/0000-0001-7355-8345](https://orcid.org/0000-0001-7355-8345)

**Tandac F. Guclu** – Faculty of Engineering and Natural Sciences, Sabanci University, Tuzla 34956 Istanbul, Turkey; [orcid.org/0000-0002-2516-1922](https://orcid.org/0000-0002-2516-1922)

**Isik Kantarcioğlu** – Faculty of Engineering and Natural Sciences, Sabanci University, Tuzla 34956 Istanbul, Turkey; Department of Pharmacology, University of Texas Southwestern Medical Center, Dallas 75390 Texas, United States

**Ilona K. Gaszek** – Department of Pharmacology, University of Texas Southwestern Medical Center, Dallas 75390 Texas, United States

**Erdal Toprak** – Department of Pharmacology, University of Texas Southwestern Medical Center, Dallas 75390 Texas, United States

**Ali Rana Atilgan** – Faculty of Engineering and Natural Sciences, Sabanci University, Tuzla 34956 Istanbul, Turkey; [orcid.org/0000-0003-0604-6301](https://orcid.org/0000-0003-0604-6301)

Complete contact information is available at: <https://pubs.acs.org/10.1021/acs.jcim.3c00818>

### Notes

The authors declare no competing financial interest.

## ■ ACKNOWLEDGMENTS

The numerical calculations reported in this paper were partially performed at TUBITAK ULAKBIM, High Performance and Grid Computing Center (TRUBA resources). We thank TUBITAK project no. 121Z329 for partial support. This work was partially supported by National Institutes of Health grant R01GM125748 (E.T.) and Welch Foundation I-2082-20210327 (E.T.). B.D. thanks TUBITAK project no. 118C487 for the support. I.K. was partially supported by TUBITAK 2214-A visiting research fellowship (Application Number: 1059B142100453).

## ■ REFERENCES

- (1) Ventola, C. L. The antibiotic resistance crisis: part 1: causes and threats. *Pharmacy and Therapeutics* **2015**, *40* (4), 277–283.
- (2) Kime, L.; Randall, C. P.; Banda, F. I.; Coll, F.; Wright, J.; Richardson, J.; Empel, J.; Parkhill, J.; O'Neill, A. J. Transient Silencing of Antibiotic Resistance by Mutation Represents a Significant Potential Source of Unanticipated Therapeutic Failure. *mBio* **2019**, *10* (5), e01755–19.
- (3) Borel, N.; Leonard, C.; Slade, J.; Schoborg, R. V. Chlamydial Antibiotic Resistance and Treatment Failure in Veterinary and Human Medicine. *Current Clinical Microbiology Reports* **2016**, *3* (1), 10–18.
- (4) Luangtongkum, T.; Jeon, B.; Han, J.; Plummer, P.; Logue, C. M.; Zhang, Q. Antibiotic resistance in *Campylobacter*: emergence, transmission and persistence. *Future Microbiology* **2009**, *4* (2), 189–200.
- (5) Gow, N. A. R.; Johnson, C.; Berman, J.; Coste, A. T.; Cuomo, C. A.; Perlin, D. S.; Bicanic, T.; Harrison, T. S.; Wiederhold, N.; Bromley, M.; Chiller, T.; Edgar, K. The importance of antimicrobial resistance in medical mycology. *Nat. Commun.* **2022**, *13* (1), 5352.

(6) Pulingam, T.; Paramasivam, T.; Gazzali, A. M.; Sulaiman, A. M.; Chee, J. Y.; Lakshmanan, M.; Chin, C. F.; Sudesh, K. Antimicrobial resistance: Prevalence, economic burden, mechanisms of resistance and strategies to overcome. *European Journal of Pharmaceutical Sciences* **2022**, 170, No. 106103.

(7) Palmer, A. C.; Kishony, R. Understanding, predicting and manipulating the genotypic evolution of antibiotic resistance. *Nat. Rev. Genet* **2013**, 14 (4), 243–8.

(8) S Askari, B.; Krajnovic, M. Dihydrofolate reductase gene variations in susceptibility to disease and treatment outcomes. *Curr. Genomics* **2010**, 11 (8), 578–83.

(9) Omar, A. M.; Alswah, M.; Ahmed, H. E. A.; Bayoumi, A. H.; El-Gamal, K. M.; El-Morsy, A.; Ghiaty, A.; Affifi, T. H.; Sherbiny, F. F.; Mohammed, A. S.; Mansour, B. A. Antimicrobial screening and pharmacokinetic profiling of novel phenyl-[1,2,4]triazolo[4,3-a]-quinoxaline analogues targeting DHFR and *E. coli* DNA gyrase B. *Bioorganic Chemistry* **2020**, 96, No. 103656.

(10) He, J.; Qiao, W.; An, Q.; Yang, T.; Luo, Y. Dihydrofolate reductase inhibitors for use as antimicrobial agents. *Eur. J. Med. Chem.* **2020**, 195, No. 112268.

(11) Ribeiro, J. A.; Hammer, A.; Libreros-Zúñiga, G. A.; Chavez-Pacheco, S. M.; Tyrakis, P.; de Oliveira, G. S.; Kirkman, T.; El Bakali, J.; Rocco, S. A.; Şorça, M. L.; Parise-Filho, R.; Coyne, A. G.; Blundell, T. L.; Abell, C.; Dias, M. V. B. Using a Fragment-Based Approach to Identify Alternative Chemical Scaffolds Targeting Dihydrofolate Reductase from *Mycobacterium tuberculosis*. *ACS Infectious Diseases* **2020**, 6 (8), 2192–2201.

(12) DeJarnette, C.; Luna-Tapia, A.; Estredge, L. R.; Palmer, G. E. Dihydrofolate Reductase Is a Valid Target for Antifungal Development in the Human Pathogen *Candida albicans*. *mSphere* **2020**, 5 (3), e00374–20.

(13) Liu, H.; Qin, Y.; Zhai, D.; Zhang, Q.; Gu, J.; Tang, Y.; Yang, J.; Li, K.; Yang, L.; Chen, S.; Zhong, W.; Meng, J.; Liu, Y.; Sun, T.; Yang, C. Antimalarial Drug Pyrimethamine Plays a Dual Role in Antitumor Proliferation and Metastasis through Targeting DHFR and TP. *Molecular Cancer Therapeutics* **2019**, 18 (3), 541–555.

(14) Gao, T.; Zhang, C.; Shi, X.; Guo, R.; Zhang, K.; Gu, J.; Li, L.; Li, S.; Zheng, Q.; Cui, M.; Cui, M.; Gao, X.; Liu, Y.; Wang, L. Targeting dihydrofolate reductase: Design, synthesis and biological evaluation of novel 6-substituted pyrrolo[2,3-d]pyrimidines as nonclassical antifolates and as potential antitumor agents. *Eur. J. Med. Chem.* **2019**, 178, 329–340.

(15) Smith, V. F.; Matthews, C. R. Testing the role of chain connectivity on the stability and structure of dihydrofolate reductase from *E. coli*: Fragment complementation and circular permutation reveal stable, alternatively folded forms. *Protein Sci.* **2001**, 10 (1), 116–128.

(16) Heikkilä, E.; Renkonen, O.-V.; Sunila, R.; Uurasmaa, P.; Huovinen, P. The emergence and mechanisms of trimethoprim resistance in *Escherichia coli* isolated from outpatients in Finland. *J. Antimicrob. Chemother.* **1990**, 25 (2), 275–283.

(17) Rashid, N.; Thapliyal, C.; Chattopadhyay, P. C. Dihydrofolate Reductase as a Versatile Drug Target in Healthcare. *J. Proteins Proteomics* **2016**, 7.

(18) Hitchings, G. H.; Burchall, J. J. Inhibition of Folate Biosynthesis and Function as a Basis for Chemotherapy. In *Adv. Enzymol. Relat. Areas Mol. Biol.* **2006**, 417–468.

(19) Eliopoulos, G. M.; Huovinen, P. Resistance to Trimethoprim-Sulfamethoxazole. *Clinical Infectious Diseases* **2001**, 32 (11), 1608–1614.

(20) Toprak, E.; Veres, A.; Michel, J.-B.; Chait, R.; Hartl, D. L.; Kishony, R. Evolutionary paths to antibiotic resistance under dynamically sustained drug selection. *Nat. Genet.* **2012**, 44 (1), 101–105.

(21) Toprak, E.; Veres, A.; Yildiz, S.; Pedraza, J. M.; Chait, R.; Paulsson, J.; Kishony, R. Building a morbidostat: an automated continuous-culture device for studying bacterial drug resistance under dynamically sustained drug inhibition. *Nat. Protoc.* **2013**, 8 (3), 555–567.

(22) Tamer, Y. T.; Gaszek, I. K.; Abdizadeh, H.; Batur, T. A.; Reynolds, K. A.; Atilgan, A. R.; Atilgan, C.; Toprak, E. High-Order Epistasis in Catalytic Power of Dihydrofolate Reductase Gives Rise to a Rugged Fitness Landscape in the Presence of Trimethoprim Selection. *Mol. Biol. Evol.* **2019**, 36 (7), 1533–1550.

(23) Rodrigues, J. V.; Bershtein, S.; Li, A.; Lozovsky, E. R.; Hartl, D. L.; Shakhnovich, E. I. Biophysical principles predict fitness landscapes of drug resistance. *Proc. Natl. Acad. Sci. U. S. A.* **2016**, 113 (11), E1478–E1478.

(24) Abdizadeh, H.; Tamer, Y. T.; Acar, O.; Toprak, E.; Atilgan, A. R.; Atilgan, C. Increased substrate affinity in the *Escherichia coli* L28R dihydrofolate reductase mutant causes trimethoprim resistance. *Phys. Chem. Chem. Phys.* **2017**, 19 (18), 11416–11428.

(25) Manna, M. S.; Tamer, Y. T.; Gaszek, I.; Poulides, N.; Ahmed, A.; Wang, X.; Toprak, F. C. R.; Woodard, D. R.; Koh, A. Y.; Williams, N. S.; Borek, D.; Atilgan, A. R.; Hulleman, J. D.; Atilgan, C.; Tambar, U.; Toprak, E. A trimethoprim derivative impedes antibiotic resistance evolution. *Nat. Commun.* **2021**, 12 (1). DOI: 10.1038/s41467-021-23191-z

(26) Cetin, E.; Atilgan, A. R.; Atilgan, C. DHFR Mutants Modulate Their Synchronized Dynamics with the Substrate by Shifting Hydrogen Bond Occupancies. *J. Chem. Inf. Model.* **2022**, 62 (24), 6715–6726.

(27) Abdizadeh, H.; Atilgan, A. R.; Atilgan, C. Detailed molecular dynamics simulations of human transferrin provide insights into iron release dynamics at serum and endosomal pH. *Journal of Biological Inorganic Chemistry* **2015**, 20 (4), 705–718.

(28) Aykut, A. Ö.; Atilgan, A. R.; Atilgan, C. Designing Molecular Dynamics Simulations to Shift Populations of the Conformational States of Calmodulin. *Plos Computational Biology* **2013**, 9 (12), e1003366.

(29) Sensoy, O.; Atilgan, A. R.; Atilgan, C. FbpA iron storage and release are governed by periplasmic microenvironments. *Phys. Chem. Chem. Phys.* **2017**, 19 (8), 6064–6075.

(30) Zwanzig, R. W. High-Temperature Equation of State by a Perturbation Method. I. Nonpolar Gases. *J. Chem. Phys.* **1954**, 22 (8), 1420–1426.

(31) Shirts, M. R.; Chodera, J. D. Statistically optimal analysis of samples from multiple equilibrium states. *J. Chem. Phys.* **2008**, 129 (12), No. 124105.

(32) Guclu, T. F.; Atilgan, A. R.; Atilgan, C. Dynamic Community Composition Unravels Allosteric Communication in PDZ3. *J. Phys. Chem. B* **2021**, 125 (9), 2266–2276.

(33) Mayne, C. G.; Saam, J.; Schulten, K.; Tajkhorsid, E.; Gumbart, J. C. Rapid parameterization of small molecules using the force field toolkit. *J. Comput. Chem.* **2013**, 34 (32), 2757–2770.

(34) Humphrey, W.; Dalke, A.; Schulten, K. VMD: Visual molecular dynamics. *J. Mol. Graphics* **1996**, 14 (1), 33–38.

(35) Frisch, J.; Trucks, G. W.; Schlegel, H. B.; Scuseria, G. E.; Robb, M. A.; Cheeseman, J. R.; Scalmani, G.; Barone, V.; Petersson, G. A.; Nakatsuji, H.; Li, X.; Caricato, M.; Marenich, A.; Bloino, J.; Janesko, B. G.; Gomperts, R.; Mennucci, B.; Hratchian, H. P.; Ortiz, J. V.; Izmaylov, A. F.; Sonnenberg, J. L.; Williams-Young, D.; Ding, F.; Lipparini, F.; Egidi, F.; Goings, J.; Peng, B.; Petrone, A.; Henderson, T.; Ranasinghe, D.; Zakrzewski, V. G.; Gao, J.; Rega, N.; Zheng, G.; Liang, W.; Hada, M.; Ehara, M.; Toyota, K.; Fukuda, R.; Hasegawa, J.; Ishida, M.; Nakajima, T.; Honda, Y.; Kitao, O.; Nakai, H.; Vreven, T.; Throssell, K.; Montgomery, J. A., Jr.; Peralta, J. E.; Ogliaro, F.; Bearpark, M.; Heyd, J. J.; Brothers, E.; Kudin, K. N.; Staroverov, V. N.; Keith, T.; Kobayashi, R.; Norman, J.; Raghavachari, K.; Rendell, A.; Burant, J. C.; Iyengar, S. S.; Tomasi, J.; Cossi, M.; Millam, J. M.; Klene, M.; Adamo, C.; Cammi, R.; Ochterski, J. W.; Martin, R. L.; Morokuma, K.; Farkas, O.; Foresman, J. B.; Fox, D. J. *Gaussian 09*; Gaussian, Inc.: Wallingford, CT, 2016.

(36) London, R. E.; Howell, E. E.; Warren, M. S.; Kraut, J.; Blakley, R. L. Nuclear magnetic resonance study of the state of protonation of inhibitors bound to mutant dihydrofolate reductase lacking the active-site carboxyl. *Biochemistry* **1986**, 25 (22), 7229–7235.

(37) Phillips, J. C.; Braun, R.; Wang, W.; Gumbart, J.; Tajkhorshid, E.; Villa, E.; Chipot, C.; Skeel, R. D.; Kalé, L.; Schulten, K. Scalable molecular dynamics with NAMD. *J. Comput. Chem.* **2005**, *26* (16), 1781–1802.

(38) MacKerell, A. D.; Bashford, D.; Bellott, M.; Dunbrack, R. L.; Evanseck, J. D.; Field, M. J.; Fischer, S.; Gao, J.; Guo, H.; Ha, S.; Joseph-McCarthy, D.; Kuchnir, L.; Kuczera, K.; Lau, F. T. K.; Mattos, C.; Michnick, S.; Ngo, T.; Nguyen, D. T.; Prodhom, B.; Reiher, W. E.; Roux, B.; Schlenkrich, M.; Smith, J. C.; Stote, R.; Straub, J.; Watanabe, M.; Wiórkiewicz-Kuczera, J.; Yin, D.; Karplus, M. All-Atom Empirical Potential for Molecular Modeling and Dynamics Studies of Proteins. *J. Phys. Chem. B* **1998**, *102* (18), 3586–3616.

(39) Pohorille, A.; Jarzynski, C.; Chipot, C. Good Practices in Free-Energy Calculations. *J. Phys. Chem. B* **2010**, *114* (32), 10235–10253.

(40) Girvan, M.; Newman, M. E. Community structure in social and biological networks. *Proc. Natl. Acad. Sci. U. S. A.* **2002**, *99* (12), 7821–6.

(41) Newman, M. E. Fast algorithm for detecting community structure in networks. *Phys. Rev. E Stat Nonlin Soft Matter Phys.* **2004**, *69* (6), No. 066133.

(42) Das, S. G.; Direito, S. O. L.; Waclaw, B.; Allen, R. J.; Krug, J. Predictable properties of fitness landscapes induced by adaptational tradeoffs. *eLife* **2020**, *9*, No. e55155.

(43) Boehr, D. D.; Dyson, H. J.; Wright, P. E. Conformational Relaxation following Hydride Transfer Plays a Limiting Role in Dihydrofolate Reductase Catalysis†. *Biochemistry* **2008**, *47* (35), 9227–9233.

(44) Thompson, S.; Zhang, Y.; Ingle, C.; Reynolds, K. A.; Kortemme, T. Altered expression of a quality control protease in *E. coli* reshapes the in vivo mutational landscape of a model enzyme. *eLife* **2020**, *9*, No. e53476.

(45) Sawaya, M. R.; Kraut, J. Loop and Subdomain Movements in the Mechanism of *Escherichia coli* Dihydrofolate Reductase: Crystallographic Evidence. *Biochemistry* **1997**, *36* (3), 586–603.

(46) Liu, C. T.; Hanoian, P.; French, J. B.; Pringle, T. H.; Hammes-Schiffer, S.; Benkovic, S. J. Functional significance of evolving protein sequence in dihydrofolate reductase from bacteria to humans. *Proc. Natl. Acad. Sci. U. S. A.* **2013**, *110* (25), 10159.

(47) Bhahba, G.; Ekiert, D. C.; Jennewein, M.; Zmasek, C. M.; Tuttle, L. M.; Kroon, G.; Dyson, H. J.; Godzik, A.; Wilson, I. A.; Wright, P. E. Divergent evolution of protein conformational dynamics in dihydrofolate reductase. *Nature Structural & Molecular Biology* **2013**, *20* (11), 1243–1249.

(48) Reynolds, K. A.; McLaughlin, R. N.; Ranganathan, R. Hot spots for allosteric regulation on protein surfaces. *Cell* **2011**, *147* (7), 1564–75.

![A 3D molecular model of a protein structure. The protein is shown in a ribbon diagram with a large, translucent blue sphere representing a specific region or binding site. The protein backbone is colored in yellow and orange, and the side chains are shown in various colors, including green and pink, indicating different amino acids or functional groups. The model is set against a plain white background.](d29cfbf30a471dc06a78be27f86bd1cf_img.jpg)

A 3D molecular model of a protein structure. The protein is shown in a ribbon diagram with a large, translucent blue sphere representing a specific region or binding site. The protein backbone is colored in yellow and orange, and the side chains are shown in various colors, including green and pink, indicating different amino acids or functional groups. The model is set against a plain white background.

CAS BIOFINDER DISCOVERY PLATFORM™

## BRIDGE BIOLOGY AND CHEMISTRY FOR FASTER ANSWERS

Analyze target relationships,  
compound effects, and disease  
pathways

Explore the platform