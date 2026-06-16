# Makale Revizyonu — Uygulama Rehberi (Türkçe)

**Dergi:** Pharmaceutics (MDPI)  
**Karar:** Accept after minor revision  
**Manuscript ID:** pharmaceutics-4363480

---

## Hızlı Kontrol Listesi

| # | Editör İsteği | Durum | Dosya |
|---|---------------|-------|-------|
| 1 | Figürler ≥300 DPI | Sizde: Maestro'dan yeniden export | `05_figure_guidelines.md` |
| 2 | Eksen/residue font büyütme | Sizde: export ayarları | `05_figure_guidelines.md` |
| 3 | Denklemler → editable text | Hazır metin | `01_equations_word_latex.md` |
| 4 | H-bond evolution plot | MD yaptınız → figür + caption | `03_section_3_2` §3.2.3 |
| 5 | Trajectory MM/GBSA | MD yaptınız → tabloya yazın | `02_methods_updates.md` |
| 6 | Bölüm 3.2 birleştirme | Hazır metin (İngilizce) | `03_section_3_2_consolidated.md` |
| 7 | Discussion yeniden yazım | Hazır metin (İngilizce) | `04_section_4_discussion_reframed.md` |
| — | Editör yanıt mektubu | Hazır taslak | `06_response_to_editor.md` |

---

## Sizin Yapmanız Gerekenler (MD verileriyle)

### A. MM/GBSA trajectory sonuçlarını tabloya aktarın

`02_methods_updates.md` içindeki tabloyu doldurun. Schrödinger Prime'da:
- Simulation → Extract frames every 5 ns
- Prime → MM-GBSA → batch mode
- Mean ± SD hesaplayın (Excel/Python)

**Table 1'i güncelleyin:** Eski tek-poz değerleri kaldırın, trajectory-averaged değerleri yazın.

### B. H-bond plot'unu ekleyin

SID modülünden veya `.nc` trajectory'den:
- X: time (ns), 0–250
- Y: total H-bond count
- 4 complex için panel figür

Placeholder'ları `03_section_3_2_consolidated.md` §3.2.3'te `[X]` ve `[YENİ FİGÜR NO]` ile değiştirin.

### C. Figürleri yeniden export edin

`05_figure_guidelines.md` — özellikle Fig. 5–10 ve contact timeline'lar (S2–S7).

### D. Word dosyasına metinleri yapıştırın

1. **Bölüm 2.3:** Denklem görüntülerini sil → `01_equations` metnini yapıştır
2. **Bölüm 2.4 sonu:** H-bond methods paragrafı ekle
3. **Bölüm 2.5:** Tamamen değiştir (`02_methods_updates`)
4. **Bölüm 3.2:** 3.2.1–3.2.6 sil → `03_section_3_2` metnini yapıştır
5. **Bölüm 4:** Eski discussion'ı sil → `04_section_4` metnini yapıştır
6. **Limitations:** Eski "single docking-derived conformations" cümlesini trajectory MM/GBSA ile uyumlu hale getirin

### E. Response letter'ı submission sistemine yükleyin

`06_response_to_editor.md` — MM/GBSA ve H-bond değerlerinizi ekledikten sonra gönderin.

---

## Önemli Bilimsel Noktalar (editörün beklediği mesaj)

1. **NPACT00189** = tek gerçek dual-target aday (her iki hedefte de 250 ns boyunca stabil)
2. **NPACT01210** = AChE'de iyi, GPX4'te ~47 ns sonra allosterik bölgeden ayrılıyor → dual-target değil
3. **Trajectory MM/GBSA** statik docking MM/GBSA'dan daha güvenilir; NPACT01210–GPX4 ayrımını netleştirir
4. **BBB:** MW 598, TPSA 157 → pasif BBB geçişi zayıf; bunu Discussion'da açıkça eleştirin (4.4)
5. **Benchmark:** Thonningianin A (GPX4 aktivatör), huperzine A (AChE), forsythoside A ile karşılaştırın

---

## Bana İletirseniz Tamamlayabileceğim Şeyler

Aşağıdaki verileri paylaşırsanız placeholder'ları doldurup final metni üretebilirim:

```
NPACT00189-GPX4:  MM/GBSA mean = ?, SD = ?
NPACT01210-GPX4:  MM/GBSA mean = ?, SD = ?
PKUMDL-GPX4:      MM/GBSA mean = ?, SD = ?
NPACT00189-AChE:  MM/GBSA mean = ?, SD = ?
NPACT01210-AChE:  MM/GBSA mean = ?, SD = ?
Donepezil-AChE:   MM/GBSA mean = ?, SD = ?

H-bond (ortalama veya aralık):
NPACT00189-GPX4:  ? H-bonds
NPACT01210-GPX4:  ? (0-47 ns) → ? (47-250 ns)
...
```

Ayrıca trajectory CSV/log dosyalarını yüklerseniz H-bond figürünü Python ile çizebilirim.
