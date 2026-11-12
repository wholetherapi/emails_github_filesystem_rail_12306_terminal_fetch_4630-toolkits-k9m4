"""Atlas field-sampling pipeline entry point."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from .io_utils import read_sites, write_manifest


def min_distance_m(a, b):
    """Approximate planar distance between two (lat, lon) points in metres."""
    dx = (a[0] - b[0]) * 111_320.0
    dy = (a[1] - b[1]) * 111_320.0 * 0.78
    return (dx * dx + dy * dy) ** 0.5


def select_sites(sites, max_sites=40, min_spacing_m=250.0):
    """Greedy stratified selection with a minimum spacing constraint."""
    if not sites:
        return []
    ordered = sorted(sites, key=lambda s: (-float(s["weight"]), s["site_id"]))
    chosen = []
    for site in ordered:
        point = (float(site["lat"]), float(site["lon"]))
        if all(min_distance_m(point, other) >= min_spacing_m for other in chosen):
            chosen.append(point)
            if len(chosen) >= max_sites:
                break
    return chosen


def run(input_path: Path, output_path: Path, max_sites: int, min_spacing_m: float):
    sites = read_sites(input_path)
    chosen = select_sites(sites, max_sites=max_sites, min_spacing_m=min_spacing_m)
    write_manifest(output_path, chosen)
    return len(chosen)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Atlas sampling pipeline")
    parser.add_argument("--sites", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--max-sites", type=int, default=40)
    parser.add_argument("--min-spacing-m", type=float, default=250.0)
    args = parser.parse_args(argv)
    count = run(args.sites, args.out, args.max_sites, args.min_spacing_m)
    print(f"selected {count} sites")


if __name__ == "__main__":
    main()
