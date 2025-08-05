import unittest
import math
import stats as statistics


class StatsTest(unittest.TestCase):
  def test_report_min_max_avg(self):
    computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):
    computedStats = statistics.calculateStats([])
    self.assertTrue(math.isnan(computedStats['avg']))
    self.assertTrue(math.isnan(computedStats['max']))
    self.assertTrue(math.isnan(computedStats['min']))
  
  def test_avg_ignore_nan_in_input(self):
    computedStats = statistics.calculateStats([1.5, float('nan'), 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 3.067, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 4.5, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

  def test_avg_nan_for_all_nan_input(self):
    computedStats = statistics.calculateStats([float('nan'), float('nan')])
    self.assertTrue(math.isnan(computedStats['avg']))
    self.assertTrue(math.isnan(computedStats['max']))
    self.assertTrue(math.isnan(computedStats['min']))

  def test_avg_nan_for_absurd_input(self):
    computedStats = statistics.calculateStats([1e10, -1, 9.2, 4.5, 1e5])
    self.assertTrue(math.isnan(computedStats['avg']))
    self.assertTrue(math.isnan(computedStats['max']))
    self.assertTrue(math.isnan(computedStats['min']))

if __name__ == "__main__":
  unittest.main()
