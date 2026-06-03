#!/usr/bin/env python3
"""Build reviewer-ready DP4+ Excel (data + computed probabilities)."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils.dataframe import dataframe_to_rows

from build_dp4_excel import EXP_C, EXP_H, _avg, build_sarotti_table, run_dp4plus
from parse_jaguar_nmr import parse_jaguar_shieldings

DIR = Path(__file__).parent
HDR = Font(bold=True, color="FFFFFF")
HDR_FILL = PatternFill("solid", fgColor="366092")
TITLE = Font(bold=True, size=14)


def _style_header(ws, row: int, ncol: int) -> None:
    for c in range(1, ncol + 1):
        cell = ws.cell(row=row, column=c)
        cell.font = HDR
        cell.fill = HDR_FILL
        cell.alignment = Alignment(horizontal="center", wrap_text=True)


def main() -> None:
    shield_e = parse_jaguar_shieldings(DIR / "jag_G5_E_spe.log")
    shield_z = parse_jaguar_shieldings(DIR / "jag_G1_spe.log")
    table = build_sarotti_table(shield_e, shield_z)
    probs = run_dp4plus(shield_e, shield_z)

    out = DIR / "DP4_PLUS_HAKEME_DOLDURULMUS.xlsx"
    wb = Workbook()

    # --- Main ---
    ws = wb.active
    ws.title = "Main"
    ws["A1"] = "DP4+ — Oxime ether E / Z (hakem paketi)"
    ws["A1"].font = TITLE

    r = 3
    ws.cell(r, 1, "ZONE A — Ayarlar (Sarotti şablonuyla aynı seçimler)")
    ws.cell(r, 1).font = Font(bold=True)
    r += 1
    for label, val in [
        ("Functional", "B3LYP"),
        ("Solvent?", "PCM"),
        ("Basis set", "6-31G**"),
        ("Type of data", "Shielding Tensors (σ)"),
        ("Isomer 1", "E (jag_G5_E)"),
        ("Isomer 2", "Z (jag_G1)"),
        ("Teori (Jaguar)", "B3LYP-D3 / 6-31G** / PCM / CHCl3"),
    ]:
        ws.cell(r, 1, label)
        ws.cell(r, 2, val)
        r += 1

    r += 1
    ws.cell(r, 1, "ZONE B — Deneysel + hesaplanan kalkan sabitleri (σ)")
    ws.cell(r, 1).font = Font(bold=True)
    r += 1
    start_b = r
    headers = [
        "Nuclei",
        "sp2 (x)",
        "Experimental (ppm)",
        "Assignment",
        "Isomer 1 E — σ",
        "Isomer 2 Z — σ",
        "E atoms",
        "Z atoms",
    ]
    for c, h in enumerate(headers, 1):
        ws.cell(r, c, h)
    _style_header(ws, r, len(headers))
    r += 1
    for _, row in table.iterrows():
        ws.cell(r, 1, row["Nuclei"])
        ws.cell(r, 2, row["sp2 (x if sp2)"])
        ws.cell(r, 3, row["Experimental (ppm)"])
        ws.cell(r, 4, row["Assignment"])
        ws.cell(r, 5, round(row["sigma E (shielding)"], 4))
        ws.cell(r, 6, round(row["sigma Z (shielding)"], 4))
        ws.cell(r, 7, row["E atom(s)"])
        ws.cell(r, 8, row["Z atom(s)"])
        r += 1

    r += 2
    ws.cell(r, 1, "ZONE C — DP4+ olasılıkları (%, B3LYP/6-31G(d,p)/PCM parametreleri)")
    ws.cell(r, 1).font = Font(bold=True)
    r += 1
    ws.cell(r, 1, "Metric")
    ws.cell(r, 2, "E (%)")
    ws.cell(r, 3, "Z (%)")
    _style_header(ws, r, 3)
    r += 1
    for idx in probs.index:
        ws.cell(r, 1, idx)
        ws.cell(r, 2, round(float(probs.loc[idx, "E"]), 2))
        ws.cell(r, 3, round(float(probs.loc[idx, "Z"]), 2))
        r += 1

    ws.column_dimensions["A"].width = 22
    ws.column_dimensions["D"].width = 22
    for col in "BCEFGH":
        ws.column_dimensions[col].width = 14

    # --- Detailed Results ---
    ws2 = wb.create_sheet("Detailed Results")
    ws2.append(["DP4+ probabilities (0–1 scale; ×100 for %)"])
    ws2.append([])
    ws2.append(["Metric", "E", "Z"])
    for idx in probs.index:
        ws2.append([idx, float(probs.loc[idx, "E"]), float(probs.loc[idx, "Z"])])

    # --- Sarotti paste (minimal) ---
    ws3 = wb.create_sheet("Sarotti_yapistir")
    ws3["A1"] = "Resmi Sarotti dp4_plus.xlsx Zone B'ye yapıştırın (A–E sütunları)"
    ws3["A3"] = "Nuclei"
    ws3["B3"] = "sp2?"
    ws3["C3"] = "Experimental"
    ws3["D3"] = "Isomer 1 (E)"
    ws3["E3"] = "Isomer 2 (Z)"
    _style_header(ws3, 3, 5)
    row = 4
    for exp, _role, sp2, le, lz in EXP_H:
        ws3.cell(row, 1, "H")
        ws3.cell(row, 2, "x" if sp2 else "")
        ws3.cell(row, 3, exp)
        ws3.cell(row, 4, round(_avg(shield_e, le), 4))
        ws3.cell(row, 5, round(_avg(shield_z, lz), 4))
        row += 1
    for exp, _role, sp2, le, lz in EXP_C:
        ws3.cell(row, 1, "C")
        ws3.cell(row, 2, "x" if sp2 else "")
        ws3.cell(row, 3, exp)
        ws3.cell(row, 4, round(shield_e[le], 4))
        ws3.cell(row, 5, round(shield_z[lz], 4))
        row += 1

    # --- README ---
    ws4 = wb.create_sheet("OKUINUZ")
    notes = [
        "Bu dosya Sarotti DP4+ mantığıyla doldurulmuş hakem paketidir.",
        "Resmi şablon (dp4_plus.xlsx) şifrelidir; JOC 2015 SI veya açılış şifresi ile açın.",
        "Alternatif: 'Sarotti_yapistir' sayfasından 17 satırı kopyalayıp resmi Main/Zone B'ye yapıştırın.",
        "Ana kanıt: 1H DP4+ → P(E) ≈ 100%. Birleşik 1H+13C → P(E) ≈ 94% (CH2 13C GIAO sapması).",
        "Bileşik: 1-(4-clorofenil)-2-(4-metil-1H-pirazol-1-il)etan-1-on O-metil oksim.",
    ]
    for i, line in enumerate(notes, 1):
        ws4.cell(i, 1, line)

    wb.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
