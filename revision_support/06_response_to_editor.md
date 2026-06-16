# Response to Academic Editor — Point-by-Point

**Manuscript ID:** pharmaceutics-4363480  
**Title:** Dual Targeting of AChE Inhibition and GPX4 Binding by Plant-Derived Compounds for the Treatment of Alzheimer's Disease: Insights from Molecular Docking and Molecular Dynamics Simulations  
**Decision:** Accept after minor revision

---

Dear Academic Editor,

Thank you for your constructive evaluation of our manuscript. We have carefully addressed all requested revisions. Below, we provide a point-by-point response. All changes are highlighted in **yellow** in the revised manuscript.

---

### Comment 1: Figure Quality & Resolution

**Editor:** Ensure all figures are submitted with a minimum resolution of 300 DPI.

**Response:** We thank the editor for this remark. All figures (Figs. 1–12 and Supplementary Figs. S1–S7) have been re-exported at ≥300 DPI in TIFF format. Multi-panel MD figures (Figs. 5–10) were regenerated from the simulation analysis modules with increased output resolution (2400 px width, 300 DPI).

**Changes:** All figure files replaced in the submission system; figure captions unchanged except for new Figure X (H-bond evolution).

---

### Comment 2: Axis Labels & Legends

**Editor:** Increase font size of axis numbers (ns, Å) and amino acid residue labels (Asp23, Lys90, etc.).

**Response:** We increased axis label fonts to 12–14 pt and tick labels to 11 pt. Residue labels in contact heatmaps and RMSF marker annotations were enlarged to 9–10 pt. All MD figures (Figs. 5–10) were re-exported with these settings.

**Changes:** Figs. 5–10 and Supplementary Figs. S2–S7 updated.

---

### Comment 3: Equation Formatting

**Editor:** Convert embedded equations to editable text; remove blurry Z-score and Composite Binding Score images in Section 2.3.

**Response:** The image-based equations in Section 2.3 have been removed and replaced with native Word equations:
- Eq. (1): *Z* = (*X* − *μ*)/*σ*
- Eq. (2): *C*<sub>score</sub> = *Z*<sub>GPX4</sub> + *Z*<sub>AChE</sub>

The MM/GBSA equation in Section 2.5 was similarly formatted as editable text (Eq. 3).

**Changes:** Section 2.3, p. 4; Section 2.5, p. 5.

---

### Comment 4: Hydrogen Bond Evolution Data

**Editor:** Include a dynamic line plot of H-bond counts for NPACT00189/NPACT01210 across 250 ns (p. 6).

**Response:** Hydrogen bond analysis was performed at 100 ps intervals using Schrödinger's SID module (distance ≤ 3.0 Å, angle ≥ 120°). Dynamic line plots were generated for all four lead complexes (NPACT00189–GPX4, NPACT01210–GPX4, NPACT00189–AChE, NPACT01210–AChE) and are presented as **Figure X** (new). A new subsection (Section 3.2.3) and corresponding Methods paragraph (Section 2.4) describe the analysis.

**Changes:** New Figure X; Sections 2.4 and 3.2.3 added; p. 6.

---

### Comment 5: MM/GBSA Calculations

**Editor:** Perform trajectory-based MM/GBSA instead of single static docking poses; extract snapshots every 2–5 ns and report averaged binding energies.

**Response:** We completely revised the MM/GBSA protocol. Structural snapshots were extracted every **5 ns** (50 frames per 250 ns trajectory) from production MD simulations. Mean ± SD Δ*G*<sub>bind</sub> values were computed for all six complexes. Section 2.5 (Methods), Table 1, and new Section 3.2.4 (Results) reflect trajectory-averaged energies. The previous single-pose values have been removed.

**Changes:** Sections 2.5, 3.1.1, 3.2.4; Table 1 updated; **[Table X — trajectory MM/GBSA summary]**.

---

### Comment 6: Consolidation of Section 3.2

**Editor:** Merge subsections 3.2.1–3.2.6 into a single comparative narrative contrasting native complexes against reference compounds.

**Response:** The six repetitive subsections were consolidated into a unified comparative narrative (Section 3.2) organized by target (GPX4, Section 3.2.1; AChE, Section 3.2.2) with integrated H-bond (3.2.3) and MM/GBSA (3.2.4) analyses and a summary (3.2.5). Figs. 5–10 are now referenced within comparative paragraphs rather than in isolated compound-specific subsections.

**Changes:** Section 3.2 entirely restructured; pp. 6–8.

---

### Comment 7: Reframing of Section 4 (Discussion)

**Editor:** Remove copy-pasted background and repeated numerical results; replace with critical biochemical interpretation, benchmarking against natural dual-inhibitors, and realistic BBB critique.

**Response:** The Discussion was substantially rewritten. Removed: redundant ferroptosis background, repeated docking scores, and AChE gorge anatomy already covered in Results. Added: (i) biochemical interpretation of dual-pocket engagement (Section 4.1); (ii) benchmarking against Thonningianin A, forsythoside A, silibinin, and huperzine A (Section 4.2); (iii) methodological implications of trajectory MM/GBSA (Section 4.3); (iv) explicit critique of BBB penetration limits for high-MW polyphenols with realistic development paths (Section 4.4).

**Changes:** Section 4 entirely revised; pp. 7–8.

---

We believe these revisions strengthen the manuscript's scientific rigor and translational honesty. We respectfully resubmit the revised manuscript for your consideration.

Sincerely,  
Suheda Rumeysa Osmanlioglu Dag & Mehmet Abdullah Alagoz
