# Revizyon 3: Denklem Formatları (Bölüm 2.3)

Word'deki bulanık görüntüleri silin ve aşağıdaki düzenlenebilir denklemleri ekleyin.

## Z-Score Normalizasyonu

**Word Equation Editor (Linear format):**
```
Z = (X - μ) / σ
```

**LaTeX (MDPI şablonu veya Overleaf için):**
```latex
Z = \frac{X - \mu}{\sigma}
```

**Açıklama metni (denklemin hemen altına):**
where *X* represents the raw docking score (kcal/mol) for a given compound–target pair; *μ* and *σ* denote the mean and standard deviation of docking scores calculated exclusively within the subset of 68 dual-target compounds for the respective protein (GPX4 or AChE), respectively (Table S2).

---

## Composite Binding Score (C-score)

**Word Equation Editor:**
```
C_score = Z_GPX4 + Z_AChE
```

**LaTeX:**
```latex
C_{\mathrm{score}} = Z_{\mathrm{GPX4}} + Z_{\mathrm{AChE}}
```

**Açıklama metni:**
where *Z*<sub>GPX4</sub> and *Z*<sub>AChE</sub> are the normalized Z-scores for GPX4 and AChE docking affinities, respectively. Compounds were ranked in descending order of *C*<sub>score</sub>, and the two highest-ranked candidates (NPACT00189 and NPACT01210) were advanced to molecular dynamics simulations.

---

## MM/GBSA Bağlanma Enerjisi (Bölüm 2.5 – güncellenmiş)

**Word Equation Editor:**
```
ΔG_bind = ΔE_MM + ΔG_solv + ΔG_SA
```

**LaTeX:**
```latex
\Delta G_{\mathrm{bind}} = \Delta E_{\mathrm{MM}} + \Delta G_{\mathrm{solv}} + \Delta G_{\mathrm{SA}}
```

**Açıklama metni:**
where Δ*E*<sub>MM</sub> is the molecular mechanics energy, Δ*G*<sub>solv</sub> is the solvation free energy (Generalized Born), and Δ*G*<sub>SA</sub> is the surface area–dependent nonpolar solvation term. Entropy contributions were not included; therefore, reported values represent approximate binding free energies. All values are reported in kcal/mol.
