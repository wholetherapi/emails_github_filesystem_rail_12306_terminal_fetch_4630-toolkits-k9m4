import unittest

from src.pipeline import min_distance_m, select_sites


class SelectSitesTest(unittest.TestCase):
    def test_single_site(self):
        sites = [{"site_id": "a", "lat": 0.0, "lon": 0.0, "weight": 1}]
        self.assertEqual(len(select_sites(sites, min_spacing_m=0)), 1)

    def test_spacing_filters_neighbours(self):
        sites = [
            {"site_id": "a", "lat": 0.0, "lon": 0.0, "weight": 3},
            {"site_id": "b", "lat": 0.0001, "lon": 0.0001, "weight": 2},
            {"site_id": "c", "lat": 0.01, "lon": 0.01, "weight": 1},
        ]
        self.assertEqual(len(select_sites(sites, min_spacing_m=250)), 2)

    def test_distance_symmetry(self):
        self.assertAlmostEqual(min_distance_m((0, 0), (0.01, 0)), min_distance_m((0.01, 0), (0, 0)))


if __name__ == "__main__":
    unittest.main()
