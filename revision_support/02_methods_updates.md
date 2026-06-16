# Revizyon 4 ve 5: Yöntem Bölümü Güncellemeleri

## 2.4. Molecular Dynamics Simulations (MD) — EK PARAGRAF

Aşağıdaki paragrafı mevcut MD bölümünün sonuna ekleyin:

> Hydrogen bond analysis was performed throughout the 250 ns production trajectories using Schrödinger's Simulation Interaction Diagram (SID) module. Protein–ligand hydrogen bonds were defined using a distance cutoff of 3.0 Å and an angle cutoff of 120°. The total number of hydrogen bonds formed between each ligand and its respective protein target was calculated at 100 ps intervals and plotted as a function of simulation time to assess interaction persistence and dynamic stability across the entire trajectory.

---

## 2.5. MM/GBSA Calculations — TAMAMEN DEĞİŞTİRİN

Mevcut 2.5 bölümünü (tek statik docking pozu) aşağıdaki metinle değiştirin:

### 2.5. Trajectory-Based MM/GBSA Calculations

Binding free energies were estimated using the MM/GBSA (Molecular Mechanics/Generalized Born Surface Area) method implemented in Schrödinger's Prime module. Unlike single-pose estimates derived from static docking conformations, trajectory-based MM/GBSA calculations were performed to capture conformational sampling and binding stability over the production MD simulations.

Structural snapshots were extracted from the 250 ns production trajectories at 5 ns intervals (50 frames per complex), yielding a temporally distributed ensemble that reflects ligand–protein conformational dynamics. For each snapshot, the binding free energy (Δ*G*<sub>bind</sub>) was calculated according to Equation (3) [denklem numarasını makalenize göre ayarlayın]:

> Δ*G*<sub>bind</sub> = Δ*E*<sub>MM</sub> + Δ*G*<sub>solv</sub> + Δ*G*<sub>SA</sub>

where Δ*E*<sub>MM</sub> represents the molecular mechanics energy, Δ*G*<sub>solv</sub> denotes the Generalized Born solvation free energy, and Δ*G*<sub>SA</sub> corresponds to the surface area–dependent nonpolar solvation contribution. Entropy terms were not included; therefore, the reported values represent approximate binding free energies in kcal/mol.

For each protein–ligand complex, the mean Δ*G*<sub>bind</sub> (± standard deviation) across all extracted frames was computed and reported. This trajectory-averaged approach provides a statistically more robust estimate of binding affinity than single-pose calculations and is consistent with established practices for evaluating MD-derived protein–ligand complexes. Complexes analyzed included NPACT00189, NPACT01210, PKUMDL-LC-102, and Donepezil bound to GPX4 and/or AChE, as appropriate.

---

## Notlar (sizin MD verilerinizle doldurun)

| Complex | Mean ΔG_bind (kcal/mol) | SD | N frames |
|---------|-------------------------|-----|----------|
| NPACT00189–GPX4 | [SİZİN DEĞER] | [SD] | 50 |
| NPACT01210–GPX4 | [SİZİN DEĞER] | [SD] | 50 |
| PKUMDL-LC-102–GPX4 | [SİZİN DEĞER] | [SD] | 50 |
| NPACT00189–AChE | [SİZİN DEĞER] | [SD] | 50 |
| NPACT01210–AChE | [SİZİN DEĞER] | [SD] | 50 |
| Donepezil–AChE | [SİZİN DEĞER] | [SD] | 50 |

**Table 1 güncellemesi:** Docking-temelli tek poz MM/GBSA değerlerini trajectory-averaged değerlerle değiştirin. Eski statik değerleri Supplementary Table olarak taşıyabilir veya tamamen kaldırabilirsiniz.
