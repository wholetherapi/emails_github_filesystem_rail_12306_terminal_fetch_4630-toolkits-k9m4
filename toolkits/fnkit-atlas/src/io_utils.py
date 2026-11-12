"""CSV ingest and manifest writing for the Atlas toolkit."""

from __future__ import annotations

import csv
from pathlib import Path

REQUIRED_COLUMNS = ("site_id", "lat", "lon", "weight")


def read_sites(path: Path):
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = [name for name in REQUIRED_COLUMNS if name not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"missing columns: {', '.join(missing)}")
        return [row for row in reader]


def write_manifest(path: Path, points):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with Path(path).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["lat", "lon"])
        for lat, lon in points:
            writer.writerow([f"{lat:.6f}", f"{lon:.6f}"])
