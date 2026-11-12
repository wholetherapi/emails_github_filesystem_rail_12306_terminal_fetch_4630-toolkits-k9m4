"""Meridian depth-correction pipeline."""

from __future__ import annotations

import argparse
from pathlib import Path

from .io_utils import read_depth_series, write_depth_series


def datum_offset(values, reduction=0.62):
    """Simple linear datum reduction applied to a depth series."""
    return [float(value) * reduction for value in values]


def correct_series(rows, reduction=0.62):
    corrected = []
    for row in rows:
        corrected.append(
            {
                "station_id": row["station_id"],
                "timestamp": row["timestamp"],
                "depth_m": round(float(row["depth_m"]) - datum_offset([float(row["depth_m"])], reduction)[0], 3),
            }
        )
    return corrected


def run(input_path: Path, output_path: Path, reduction: float):
    rows = read_depth_series(input_path)
    corrected = correct_series(rows, reduction=reduction)
    write_depth_series(output_path, corrected)
    return len(corrected)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Meridian depth correction")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--reduction", type=float, default=0.62)
    args = parser.parse_args(argv)
    count = run(args.input, args.out, args.reduction)
    print(f"corrected {count} rows")


if __name__ == "__main__":
    main()
