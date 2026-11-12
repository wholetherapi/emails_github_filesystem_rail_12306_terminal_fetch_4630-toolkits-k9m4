import unittest

from src.pipeline import correct_series, datum_offset


class DepthCorrectionTest(unittest.TestCase):
    def test_datum_offset_scales_linearly(self):
        self.assertAlmostEqual(datum_offset([10.0])[0], 6.2)

    def test_correction_is_monotonic(self):
        rows = [
            {"station_id": "s1", "timestamp": "2026-01-01T00:00", "depth_m": "10.0"},
            {"station_id": "s1", "timestamp": "2026-01-01T01:00", "depth_m": "12.0"},
        ]
        corrected = correct_series(rows)
        self.assertLess(corrected[0]["depth_m"], corrected[1]["depth_m"])


if __name__ == "__main__":
    unittest.main()
