# Meridian Depth Kit

Depth-correction toolkit for the Meridian programme: CSV and REST ingest, tidal
datum normalisation, and a small command-line interface for survey teams.

## Availability

**Public release — v0.9.3.** Source and release notes are public; see Releases for
the changelog. Install from `requirements.txt` and run
`python -m src.pipeline --input depth.csv --out corrected.csv`.

## Layout

- `src/pipeline.py` — correction pipeline
- `src/io_utils.py` — readers and writers
- `tests/test_pipeline.py` — unit tests
- `results/sample_run.csv` — a small corrected series
