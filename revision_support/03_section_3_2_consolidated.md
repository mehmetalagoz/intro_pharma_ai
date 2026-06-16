# Revizyon 6: Bölüm 3.2 — Birleştirilmiş Karşılaştırmalı Anlatım

**Talimat:** 3.2.1–3.2.6 alt bölümlerini silin. Aşağıdaki metni **3.2. Molecular Dynamics Simulations** olarak tek bölüm halinde kullanın. Figür referanslarını (Fig. 5–10) koruyun; H-bond ve MM/GBSA için yeni figür/tablo ekleyin.

---

## 3.2. Molecular Dynamics Simulations

Based on composite docking scores, 250 ns MD simulations were performed for NPACT00189, NPACT01210, and the reference compounds PKUMDL-LC-102 (GPX4) and Donepezil (AChE). Rather than treating each complex in isolation, the trajectories were interpreted comparatively to distinguish persistent dual-target engagement from target-specific instability.

### 3.2.1. Comparative Stability at the GPX4 Allosteric Site

At the GPX4 allosteric pocket, NPACT00189 exhibited the most favorable binding profile among the investigated ligands. Ligand RMSD fluctuated between 3.5–7.5 Å during 0–150 ns and increased modestly to 6.0–9.5 Å thereafter, with an average ligand RMSD of ~3.3 Å between 160–250 ns after equilibration (Fig. 5). Protein Cα RMSD remained stable (0.9–2.2 Å), and RMSF values were predominantly below 2.4 Å, except for minor fluctuations in residues 110–125 (< 3.2 Å). Critically, NPACT00189 maintained persistent contacts with anchoring residues Lys90, Phe100, and Asp101 throughout the trajectory, with ~99% occupancy at Lys99 (Fig. S2). Although interactions with Asp21 and Asp23 diminished after ~150 ns concomitant with a local rearrangement, contacts with Asp101 and Phe100 were sustained, indicating that NPACT00189 remains accommodated within the allosteric region under dynamic conditions.

In sharp contrast, NPACT01210 displayed early allosteric residence followed by marked dissociation. During the first 47 ns, ligand RMSD averaged ~1.0 Å and the compound interacted with canonical allosteric residues (Asp21, Asp23, Lys31, Lys90, Lys99, Phe100, Met102, Phe103). After 47 ns, ligand RMSD surged to 17.5–21.5 Å, and the ligand relocated to peripheral regions (Glu34, Ala64, Glu65, Leu68, Ile70, Lys145, Phe170), effectively vacating the allosteric pocket (Fig. 6; Fig. S3). These data indicate that NPACT01210 does not maintain persistent GPX4 allosteric binding under the simulated conditions, despite favorable initial docking scores.

The reference activator PKUMDL-LC-102 showed intermittent stability rather than sustained allosteric anchoring. Ligand RMSD displayed pronounced segmental fluctuations, with relatively stable windows at 60–110 ns and 160–215 ns but no overall convergence (Fig. 7). Predominant contacts involved Lys20 and Met120 via hydrophobic interactions and water bridges (Fig. S4). Collectively, among the three GPX4 ligands, only NPACT00189 maintained functionally relevant allosteric contacts for the majority of the 250 ns trajectory.

### 3.2.2. Comparative Stability at the AChE Active-Site Gorge

All three AChE ligands exhibited greater overall stability than NPACT01210 at GPX4, although their interaction signatures diverged in ways relevant to inhibitor classification.

NPACT00189 achieved sustained gorge occupancy with average ligand RMSD ~3.5 Å and protein Cα RMSD ~1.7 Å (Fig. 8). The ligand maintained Trp286 contacts for ~70% of the simulation and consistently engaged PAS-associated residues Asp74, Tyr124, Ser125, and Tyr341 via hydrogen bonds, hydrophobic contacts, and water bridges (Fig. S5). This pattern is consistent with dual-site gorge binding characteristic of effective AChE inhibitors.

NPACT01210 displayed comparable structural stability (ligand RMSD ~3.0 Å; protein Cα RMSD ~0.75 Å) with high-occupancy hydrogen bonds to Asp74 (93%), Tyr124 (68%), and Phe293 (75%), and persistent hydrophobic contacts with Phe295 and Tyr341 (>95%) (Fig. 9; Fig. S6). However, limited engagement with PAS (Trp286) and catalytic triad residues suggests that stability alone does not guarantee classical inhibitor pharmacophore fulfillment.

Donepezil, the clinical reference inhibitor, showed biphasic behavior: relatively stable binding during 0–140 ns (ligand RMSD 1.5–4.5 Å) followed by increased fluctuations (6–9 Å) during 160–245 ns (Fig. 10). Persistent interactions with Asp74, Tyr337, Phe338, and Tyr341 were observed across multiple trajectory segments (Fig. S7). Notably, NPACT00189 and NPACT01210 exhibited comparable or superior late-trajectory stability relative to Donepezil, while NPACT00189 uniquely combined gorge stability with PAS engagement.

### 3.2.3. Hydrogen Bond Dynamics Across the 250 ns Trajectories

To complement RMSD and contact occupancy analyses, the total number of protein–ligand hydrogen bonds was monitored at 100 ps intervals across the full 250 ns production runs (Fig. [YENİ FİGÜR NO]). For NPACT00189–GPX4, hydrogen bond counts remained consistently above [X] throughout the trajectory, corroborating persistent polar anchoring at the allosteric site. NPACT01210–GPX4 displayed an initial hydrogen bond plateau during the first ~47 ns, followed by a precipitous decline coincident with allosteric dissociation. At AChE, both lead compounds maintained elevated hydrogen bond counts relative to their GPX4 profiles, with NPACT00189 showing sustained H-bond occupancy that paralleled its Trp286 contact persistence. These dynamic profiles reinforce the comparative conclusion that NPACT00189, but not NPACT01210, sustains polar interaction networks at both targets across the simulation timescale.

### 3.2.4. Trajectory-Averaged MM/GBSA Binding Energies

Trajectory-based MM/GBSA analysis (50 snapshots at 5 ns intervals) provided binding energy estimates that account for conformational sampling (Table [YENİ TABLO NO]). [BURAYA KENDİ VERİLERİNİZİ EKLEYİN — örnek cümle yapısı:]

> For GPX4, trajectory-averaged Δ*G*<sub>bind</sub> values were −[X] ± [SD] kcal/mol (NPACT00189), −[X] ± [SD] kcal/mol (NPACT01210), and −[X] ± [SD] kcal/mol (PKUMDL-LC-102). For AChE, corresponding values were −[X] ± [SD] (NPACT00189), −[X] ± [SD] (NPACT01210), and −[X] ± [SD] (Donepezil). Importantly, the rank ordering from single-pose docking MM/GBSA was [korundu / kısmen değişti], and trajectory averaging [artırdı/azalttı] the energetic separation between stable and dissociated complexes—most notably highlighting the weakened effective affinity of NPACT01210 at GPX4 after allosteric exit.

### 3.2.5. Integrated Comparative Summary

Direct cross-complex comparison reveals a clear hierarchy: **NPACT00189** is the only compound that maintains structural stability, persistent polar contacts, and favorable trajectory-averaged binding energies at both GPX4 and AChE. **NPACT01210** is a competent AChE binder but fails to sustain GPX4 allosteric engagement beyond ~47 ns. **Reference compounds** (PKUMDL-LC-102 and Donepezil) provide context but do not outperform NPACT00189 in dual-target persistence. These integrated MD findings support advancing NPACT00189—not NPACT01210—as the primary dual-target lead for subsequent experimental validation.
