"""Number the compounds in an SDF file so they get a visible name.

When you open an SDF file in Maestro, the compound name that is shown comes
from the *title line* of each record (the very first line of every molecule
block). If that line is empty, Maestro shows no name.

This script writes a running number into that title line (1, 2, 3, ...), so
every compound gets a unique, visible name. Optionally the same number is also
stored as an extra SDF data field (e.g. <compound_id>).

The file is processed as plain text. Nothing else in the records is changed,
so it works for both V2000 and V3000 molblocks and keeps all existing data
fields and coordinates intact.

Usage examples
--------------
    # Write numbers 1..N into the title line, save next to the input file:
    python number_sdf.py molecules.sdf

    # Choose the output file explicitly:
    python number_sdf.py molecules.sdf -o molecules_numbered.sdf

    # Start counting from a different number and add a prefix:
    python number_sdf.py molecules.sdf --start 1 --prefix "CMPD-"

    # Also store the number as an SDF data field called compound_id:
    python number_sdf.py molecules.sdf --field compound_id

    # Only fill the name where it is currently empty (keep existing names):
    python number_sdf.py molecules.sdf --keep-existing
"""

import argparse
import os
import sys


def _line_ending(line):
    """Return the newline characters used by *line* (default '\\n')."""
    if line.endswith("\r\n"):
        return "\r\n"
    if line.endswith("\n"):
        return "\n"
    if line.endswith("\r"):
        return "\r"
    return "\n"


def number_sdf(in_path, out_path, start=1, prefix="", field=None,
               keep_existing=False):
    """Add running-number names to every record of an SDF file.

    Parameters
    ----------
    in_path : str
        Path to the input .sdf/.sd file.
    out_path : str
        Path of the file that is written.
    start : int
        First number to assign (default 1).
    prefix : str
        Text placed in front of every number (default "").
    field : str or None
        If given, the number is also stored as an SDF data field with this
        name (e.g. "compound_id").
    keep_existing : bool
        If True, the title line is only filled when it is currently empty.

    Returns
    -------
    int
        The number of compounds that were processed.
    """
    with open(in_path, "r", newline="") as handle:
        lines = handle.readlines()

    out_lines = []
    counter = start
    expect_title = True
    current_name = None
    n_records = 0

    for line in lines:
        if expect_title:
            ending = _line_ending(line)
            stripped = line.rstrip("\r\n")
            current_name = "{}{}".format(prefix, counter)
            if keep_existing and stripped.strip():
                # Keep the name that is already there.
                current_name = stripped
                out_lines.append(line if line.endswith(("\n", "\r"))
                                 else line + ending)
            else:
                out_lines.append(current_name + ending)
            counter += 1
            n_records += 1
            expect_title = False
            continue

        if line.rstrip("\r\n") == "$$$$":
            if field:
                out_lines.append(">  <{}>\n".format(field))
                out_lines.append(current_name + "\n")
                out_lines.append("\n")
            out_lines.append(line)
            expect_title = True
            continue

        out_lines.append(line)

    with open(out_path, "w", newline="") as handle:
        handle.writelines(out_lines)

    return n_records


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Give every compound in an SDF file a numbered name so it "
                    "is visible in Maestro.")
    parser.add_argument("input", help="Input SDF file.")
    parser.add_argument("-o", "--output", default=None,
                        help="Output SDF file (default: <input>_numbered.sdf).")
    parser.add_argument("--start", type=int, default=1,
                        help="Number to start counting from (default: 1).")
    parser.add_argument("--prefix", default="",
                        help="Text placed before each number (default: none).")
    parser.add_argument("--field", default=None,
                        help="Also store the number as this SDF data field.")
    parser.add_argument("--keep-existing", action="store_true",
                        help="Only fill the name where it is currently empty.")
    args = parser.parse_args(argv)

    if not os.path.isfile(args.input):
        parser.error("input file not found: {}".format(args.input))

    out_path = args.output
    if out_path is None:
        base, ext = os.path.splitext(args.input)
        out_path = "{}_numbered{}".format(base, ext or ".sdf")

    n = number_sdf(args.input, out_path, start=args.start, prefix=args.prefix,
                   field=args.field, keep_existing=args.keep_existing)

    print("Numbered {} compound(s).".format(n))
    print("Saved to: {}".format(out_path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
