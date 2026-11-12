# Atlas Sampling Kit

Reference implementation of the Atlas field-sampling pipeline: stratified site
selection, sample labelling and a reproducible export path for field teams.

## Availability

**Public release — v1.2.0.** The source is available and the release notes are
published under Releases. Install from `requirements.txt` and run
`python -m src.pipeline --sites sites.csv --out results/`.

## Layout

- `src/pipeline.py` — orchestration entry point
- `src/io_utils.py` — CSV ingest and manifest writing
- `tests/test_pipeline.py` — unit tests
- `results/sample_run.csv` — a small sample export
