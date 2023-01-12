from unittest import TestCase

from travel_times import fastest_travel_mode


class Test(TestCase):
    def test_fastest_mode_half(self):
        mode, time = fastest_travel_mode(.5)
        self.assertEqual(mode, "Walk")
        self.assertEqual(time, 8)

    def test_fastest_mode_whole(self):
        mode, time = fastest_travel_mode(1)
        self.assertEqual(mode, "Bike")
        self.assertAlmostEqual(time, 10.333333333333332)

    def test_fastest_mode_ten(self):
        mode, time = fastest_travel_mode(10)
        self.assertEqual(mode, "Bus")
        self.assertAlmostEqual(time, 33.14285714285714)
