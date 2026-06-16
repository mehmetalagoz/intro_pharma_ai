# Revizyon 1 ve 2: Figür Kalitesi ve Eksen Etiketleri

## Genel Gereksinimler (MDPI / Pharmaceutics)

| Parametre | Minimum | Önerilen |
|-----------|---------|----------|
| Çözünürlük | 300 DPI | 600 DPI (line art) |
| Format | TIFF veya PNG | TIFF (lossless) |
| Genişlik | 17 cm (single column) veya 7 cm (panel) | — |
| Font | Arial veya Helvetica | 10–12 pt (eksen), 8–10 pt (panel label) |

---

## Schrödinger / Maestro Export Ayarları

### RMSD, RMSF, Contact, H-bond grafikleri için:

1. **Maestro → Simulation Interaction Diagram (SID)** veya ilgili plot penceresinde:
   - *Export → Image* veya *Copy to Clipboard*
   - Resolution: **minimum 300 DPI**
   - Width: **2000–2400 pixels** (single figure) veya **1200 px/panel** (multi-panel)

2. **Font büyütme (Revizyon 2):**
   - X-axis: "Time (ns)" — **12 pt bold**
   - Y-axis: "RMSD (Å)" / "RMSF (Å)" — **12 pt bold**
   - Tick labels (0, 50, 100, 150, 200, 250): **11 pt**
   - Legend: **10 pt**
   - Contact plot residue labels (Asp23, Lys90, vb.): **9–10 pt**, dikey etiketlerde rotasyon 90°

3. **Python/matplotlib ile yeniden çizim** (trajectory verisi varsa):
```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 14,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'legend.fontsize': 10,
    'figure.dpi': 300,
    'savefig.dpi': 300,
})

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(time_ns, rmsd_protein, label='Protein Cα', linewidth=1.5)
ax.plot(time_ns, rmsd_ligand, label='Ligand', linewidth=1.5)
ax.set_xlabel('Time (ns)', fontweight='bold')
ax.set_ylabel('RMSD (Å)', fontweight='bold')
ax.legend()
plt.tight_layout()
plt.savefig('Figure5_NPACT00189_GPX4.tiff', dpi=300, bbox_inches='tight')
```

---

## Yeni Figür: H-bond Evolution (Revizyon 4)

**Önerilen düzen:** 2×2 panel veya 1×2 panel

| Panel | İçerik |
|-------|--------|
| A | NPACT00189–GPX4: H-bond count vs. time |
| B | NPACT01210–GPX4: H-bond count vs. time |
| C | NPACT00189–AChE: H-bond count vs. time |
| D | NPACT01210–AChE: H-bond count vs. time |

**Caption örneği:**
> **Figure X.** Time evolution of protein–ligand hydrogen bond counts during 250 ns MD simulations. (A,B) GPX4 allosteric complexes with NPACT00189 and NPACT01210, respectively. (C,D) AChE active-site complexes with NPACT00189 and NPACT01210, respectively. Hydrogen bonds were defined using a distance cutoff of 3.0 Å and an angle cutoff of 120°. The vertical dashed line in (B) marks the ~47 ns allosteric dissociation event for NPACT01210.

---

## Kontrol Listesi (tüm figürler)

- [ ] Fig. 5–10: 300+ DPI, eksen fontları büyütüldü
- [ ] Fig. 3–4: 2D interaction diagrams — residue labels okunabilir
- [ ] Fig. 1–2: BioRender/workflow — vektör veya yüksek çözünürlük
- [ ] Yeni H-bond figürü eklendi
- [ ] Denklem görüntüleri (Section 2.3) kaldırıldı, editable text eklendi
- [ ] Tüm figürler TIFF olarak submission system'e yüklendi
