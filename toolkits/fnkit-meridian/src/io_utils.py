"""Readers and writers for the Meridian toolkit."""

from __future__ import annotations

import csv
from pathlib import Path


def read_depth_series(path: Path):
    with Path(path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_depth_series(path: Path, rows):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fields = ["station_id", "timestamp", "depth_m"]
    with Path(path).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row[field] for field in fields})
