#!/usr/bin/env python3
"""Extract isotropic NMR shieldings from Jaguar nmrcphf output."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def parse_jaguar_shieldings(log_path: Path) -> dict[str, float]:
    text = log_path.read_text(encoding="utf-8", errors="replace")
    pattern = re.compile(
        r"NMR Properties for atom (\w+)\s+"
        r"=+\s+"
        r".*?"
        r"Isotropic shielding:\s+([-\d.]+)",
        re.DOTALL,
    )
    out: dict[str, float] = {}
    for atom, val in pattern.findall(text):
        out[atom] = float(val)
    if not out:
        raise ValueError(
            f"No shieldings found in {log_path}. "
            "Use the full Jaguar .log (not the Maestro job wrapper)."
        )
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("logs", nargs="+", help="Jaguar SPE .log files")
    ap.add_argument(
        "-o",
        "--output",
        default="shieldings_summary.tsv",
        help="Output TSV path",
    )
    args = ap.parse_args()

    rows: list[str] = ["atom\t" + "\t".join(Path(p).stem for p in args.logs)]
    all_atoms: set[str] = set()
    data: dict[str, dict[str, float]] = {}
    for p in args.logs:
        path = Path(p)
        data[path.stem] = parse_jaguar_shieldings(path)
        all_atoms.update(data[path.stem])

    for atom in sorted(all_atoms, key=lambda a: (a[0], int(re.search(r"\d+", a).group()))):
        line = [atom]
        for p in args.logs:
            stem = Path(p).stem
            line.append(f"{data[stem].get(atom, float('nan')):.4f}")
        rows.append("\t".join(line))

    out = Path(args.output)
    out.write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(f"Wrote {out} ({len(all_atoms)} atoms)")
    for stem, d in data.items():
        carbons = {k: v for k, v in d.items() if k.startswith("C")}
        print(f"  {stem}: {len(d)} atoms, {len(carbons)} carbons")


if __name__ == "__main__":
    main()
