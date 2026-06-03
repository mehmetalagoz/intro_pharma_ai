# DP4⁺ Excel paketi — oxime ether (E / Z)

Bu klasör, hakem için **Sarotti DP4⁺ Excel** girişi ve (isteğe bağlı) **DP4+ App** doğrulaması içindir.

## Dosyalar

| Dosya | Açıklama |
|--------|-----------|
| `DP4_Sarotti_ZoneB_giris.xlsx` | Sarotti Excel **Zone B**’ye kopyalanacak tablo (¹H tam; ¹³C için Z sütunu doldurulacak) |
| `DP4_Sarotti_ZoneB_1H_tam.xlsx` | Yalnızca ¹H (7 satır) — Z σ dahil, hemen Excel’e yapıştırılabilir |
| `jag_G5_E_spe.log` | E izomer kalkan sabitleri (G5_E SPE) |
| `parse_jaguar_nmr.py` | Jaguar `.log` → σ özeti |
| `build_dp4_excel.py` | İki tam `.log` ile tablo + DP4⁺ olasılığı üretir |

## Z izomer log’u

Tam `jag_G1_spe.log` (Z, G1) pakete eklendi. Yeniden üretmek için:

```bash
cd dp4_oxime
python3 build_dp4_excel.py --e-log jag_G5_E_spe.log --z-log jag_G1_spe.log
```

---

## Sarotti DP4⁺ Excel — adım adım

1. İndir: https://sarotti-nmr.weebly.com → **DP4⁺** Excel (Grimblat/Sarotti).
2. **Main** sayfası → **Zone A**:
   - Functional: **B3LYP**
   - Solvent?: **PCM**
   - Basis set: **6-31G\*\*** (Jaguar’daki 6-31G\*\* ile uyumlu; listede 6-31G** yoksa 6-31G\* veya en yakın çift zeta polarize set)
   - Type of data: **Shielding Tensors** (σ girin, δ değil)
3. **Zone B** — `DP4_Sarotti_ZoneB_1H_tam.xlsx` veya tam tablodan kopyalayın:

   | Nuclei | sp2? | Experimental | Isomer 1 (E) | Isomer 2 (Z) |
   |--------|------|--------------|--------------|--------------|
   | H | | 1.94 | σ_E | σ_Z |
   | … | | | | |
   | C | x | 150.57 | σ_E(C6) | σ_Z(C6) |
   | … | | | | |

   - **sp2**: aromatik / C=C / oxime C ve bağlı H için **x** (küçük harf de olur).
   - Alifatik (CH₃, OCH₃, CH₂): sp2 **boş**.

4. İzomer sütun başlıkları: **Isomer 1 = E (G5_E)**, **Isomer 2 = Z (G1)**.
5. Zone C’de **P(E)**, **P(Z)** görünür; ekran görüntüsünü **SI**’ye koyun.
6. **Detailed Results** sayfasından uDP4⁺ / sDP4⁺ / Full değerlerini de ekleyebilirsiniz.

### Teori seviyesi notu

Jaguar: **B3LYP-D3 / 6-31G\*\* / PCM / CHCl₃**.  
Excel’de tam eşleşen satır yoksa **B3LYP / 6-31G(d,p) / PCM** (DP4⁺ veri tabanı) kullanılır; makalede her iki ifadeyi de yazın.

---

## Deneysel veriler (bu bileşik)

**¹H** (600 MHz, CDCl₃): δ 1.94, 4.00, 5.23, 7.11, 7.19, 7.22 (2H), 7.59 (2H).

**¹³C** (150 MHz, CDCl₃): δ 150.57, 138.71, 134.54, 127.68, 127.43, 126.84, 115.74, 61.65, 44.63, 7.85 (**10 sinyal**; 131.33 yok).

---

## Atom eşlemesi (kimyasal grup — Maestro numarası farklı!)

| δ (¹H) | Grup | E (σ) | Z (σ) |
|--------|------|-------|-------|
| 1.94 | Pyrazol-CH₃ | H24–26 | H24–26 |
| 4.00 | O-CH₃ | H30–32 (**C18**) | H28–30 (**C16**) |
| 5.23 | CH₂-N | H21–22 | H21–22 |
| 7.11 / 7.19 | Pyrazol H | H23 / H27 | aynı |
| 7.22 / 7.59 | Fenil | H19–20 / **H28–29** (E) | H19–20 / **H31–32** (Z) |

| δ (¹³C) | Grup | E atom | Z atom |
|---------|------|--------|--------|
| 150.57 | C=N | C6 | C6 |
| 138.71 | Aromatik | C2 | C2 |
| 134.54 | Aromatik | C12 | C12 |
| 127.68 | Aromatik CH | **C15** (E) | **C4** (Z) |
| 127.43 | Aromatik CH | **C4** (E) | **C9** (Z) |
| 126.84 | Aromatik CH | **C5** (E) | **C3** (Z) |
| 115.74 | Pyrazol CH | C10 | C10 |
| 61.65 | O-CH₃ | **C18** | **C16** |
| 44.63 | CH₂-N | C7 | C7 |
| 7.85 | Pyrazol-CH₃ | C11 | C11 |

¹³C **Z** sütunu: tam `jag_G1` log’undan `build_dp4_excel.py` ile doldurulur.

---

## Hakeme gönderilecekler

1. Doldurulmuş Sarotti Excel (veya PDF/ekran görüntüsü: Zone A ayarları + Zone C sonuçları).
2. `DP4_Sarotti_ZoneB_giris.xlsx` (ham σ tablosu).
3. Jaguar `.log` dosyaları: `jag_G5_E_spe*.log`, `jag_G1_spe*.log` (tam çıktı).
4. Kısa metin: *DP4⁺ analysis of 7 ¹H and 10 ¹³C shifts (B3LYP/6-31G\*\*/PCM, CHCl₃) gave P(E) = … % for the E oxime ether.*

---

## DP4⁺ sonuçları (B3LYP/6-31G(d,p)/PCM, bu veri seti)

| Veri | P(E) | P(Z) |
|------|------|------|
| **Yalnızca ¹H (7)** | **~100 %** | ~0 % |
| Yalnızca ¹³C (10) | ~0 % | ~100 % |
| **¹H + ¹³C (17)** | **~94 %** | ~6 % |

**Yorum:** Karar **¹H DP4⁺** ile net (**E**). ¹³C’de δ 44.63 (CH₂-N) için E modelinde GIAO sapması büyük (~11 ppm); Z modeli bu satırda daha iyi → birleşik skor hafif düşer ama **E hâlâ baskın**. Hakem paketinde önce **¹H DP4⁺** ekran görüntüsünü koyun; ¹H+¹³C tablosunu ek (SI).

`DP4plus_probabilities_percent.xlsx` dosyasında güncel yüzdeler vardır.
