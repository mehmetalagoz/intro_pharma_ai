#!/usr/bin/env python3
"""Build DP4+ Excel input tables from Jaguar SPE logs."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from parse_jaguar_nmr import parse_jaguar_shieldings

# (exp_ppm, role, sp2, E_labels, Z_labels)
EXP_H = [
    (1.94, "Pyrazole-CH3", 0, ["H24", "H25", "H26"], ["H24", "H25", "H26"]),
    (4.00, "O-CH3", 0, ["H30", "H31", "H32"], ["H28", "H29", "H30"]),
    (5.23, "CH2-N", 0, ["H21", "H22"], ["H21", "H22"]),
    (7.11, "Pyrazole-H", 1, ["H23"], ["H23"]),
    (7.19, "Pyrazole-H", 1, ["H27"], ["H27"]),
    (7.22, "Phenyl", 1, ["H19", "H20"], ["H19", "H20"]),
    (7.59, "Phenyl", 1, ["H28", "H29"], ["H28", "H29"]),
]

EXP_C = [
    (150.57, "C=N (oxime)", 1, "C6", "C6"),
    (138.71, "Aromatic quat.", 1, "C2", "C2"),
    (134.54, "Aromatic", 1, "C12", "C12"),
    (131.33, "Aromatic", 1, "C15", "C15"),
    (127.68, "Aromatic CH", 1, "C4", "C4"),
    (127.43, "Aromatic CH", 1, "C5", "C5"),
    (126.84, "Aromatic CH", 1, "C3", "C3"),
    (115.74, "Pyrazole CH", 1, "C10", "C10"),
    (61.65, "O-CH3", 0, "C18", "C16"),
    (44.63, "CH2-N", 0, "C7", "C7"),
    (7.85, "Pyrazole-CH3", 0, "C11", "C11"),
]


def _avg(shield: dict[str, float], labels: list[str] | str) -> float:
    if isinstance(labels, str):
        labels = [labels]
    return float(np.mean([shield[x] for x in labels]))


def build_sarotti_table(
    shield_e: dict[str, float], shield_z: dict[str, float]
) -> pd.DataFrame:
    rows = []
    for exp, role, sp2, le, lz in EXP_H:
        rows.append(
            {
                "Nuclei": "H",
                "sp2 (x if sp2)": "x" if sp2 else "",
                "Experimental (ppm)": exp,
                "Assignment": role,
                "E atom(s)": ", ".join(le),
                "sigma E (shielding)": _avg(shield_e, le),
                "Z atom(s)": ", ".join(lz),
                "sigma Z (shielding)": _avg(shield_z, lz),
            }
        )
    for exp, role, sp2, le, lz in EXP_C:
        rows.append(
            {
                "Nuclei": "C",
                "sp2 (x if sp2)": "x" if sp2 else "",
                "Experimental (ppm)": exp,
                "Assignment": role,
                "E atom(s)": le,
                "sigma E (shielding)": shield_e[le],
                "Z atom(s)": lz,
                "sigma Z (shielding)": shield_z.get(lz, np.nan),
            }
        )
    return pd.DataFrame(rows)


def run_dp4plus(shield_e: dict, shield_z: dict) -> pd.DataFrame:
    from dp4plus_app import dp4_module as dp4
    from dp4plus_app.correlation_module import selections

    exp_h = [x[0] for x in EXP_H]
    sp2_h = [x[2] for x in EXP_H]
    exp_c = [x[0] for x in EXP_C]
    sp2_c = [x[2] for x in EXP_C]

    exp_data = pd.DataFrame(
        {
            "index": list(range(1, len(exp_h) + len(exp_c) + 1)),
            "nuclei": ["H"] * len(exp_h) + ["C"] * len(exp_c),
            "sp2": sp2_h + sp2_c,
            "exchange": [np.nan] * (len(exp_h) + len(exp_c)),
            "exp_data": exp_h + exp_c,
        }
    )
    df_sel = selections(exp_data)

    tens_e, tens_z = [], []
    for exp, role, sp2, le, lz in EXP_H:
        tens_e.append(_avg(shield_e, le))
        tens_z.append(_avg(shield_z, lz))
    for exp, role, sp2, le, lz in EXP_C:
        tens_e.append(shield_e[le])
        tens_z.append(shield_z[lz])

    tens = np.array([tens_e, tens_z]).T
    standard = {"C": 191.893575, "H": 31.708175}
    params = pd.read_excel(
        "/home/ubuntu/.local/lib/python3.12/site-packages/dp4plus_app/parameters_bank/data_base_QM.xlsx",
        sheet_name="B3LYP.6-31G(d,p).PCM",
        index_col=0,
    )
    uns = dp4.get_uns_shifts(tens, df_sel, standard)
    sca = dp4.get_sca_shifts(uns, df_sel, exp_data)
    uns_e = dp4.calc_errors(uns, exp_data)
    sca_e = dp4.calc_errors(sca, exp_data)
    uns_p, sca_p = dp4.calc_prob_matr(uns_e, sca_e, df_sel, params)
    return dp4.calc_results(uns_p, sca_p, df_sel, ["E", "Z"]) * 100


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--e-log", type=Path, required=True, help="E isomer jag_G5 SPE log")
    ap.add_argument("--z-log", type=Path, required=True, help="Z isomer jag_G1 SPE log")
    ap.add_argument("-o", type=Path, default=Path(__file__).parent)
    args = ap.parse_args()

    shield_e = parse_jaguar_shieldings(args.e_log)
    shield_z = parse_jaguar_shieldings(args.z_log)

    missing_z = [lz for _, _, _, _, lz in EXP_C if lz not in shield_z]
    if missing_z:
        raise SystemExit(f"Z log missing carbons: {missing_z}")

    out = args.o
    out.mkdir(parents=True, exist_ok=True)

    sarotti = build_sarotti_table(shield_e, shield_z)
    sarotti.to_excel(out / "DP4_Sarotti_ZoneB_giris.xlsx", index=False)

    probs = run_dp4plus(shield_e, shield_z)
    probs.to_excel(out / "DP4plus_probabilities_percent.xlsx")

    print("DP4+ probabilities (%):\n", probs.round(2).to_string())
    print(f"\nWrote {out / 'DP4_Sarotti_ZoneB_giris.xlsx'}")


if __name__ == "__main__":
    main()
