from unittest import TestCase

from travel_times import travel_time_per_mode


class Test(TestCase):
    def test_travel_time_per_mode_half(self):
        travel_times = travel_time_per_mode(.5)
        self.assertEqual(travel_times["Walk"], 8)
        self.assertAlmostEqual(travel_times["Bike"], 8.6666666666666666)
        self.assertAlmostEqual(travel_times["Bus"], 16.857142857142858)

    def test_travel_time_per_mode_whole(self):
        travel_times = travel_time_per_mode(1)
        self.assertEqual(travel_times["Walk"], 14)
        self.assertAlmostEqual(travel_times["Bike"], 10.333333333333332)
        self.assertAlmostEqual(travel_times["Bus"], 17.714285714285715)

    def test_travel_time_per_mode_ten(self):
        travel_times = travel_time_per_mode(10)
        self.assertEqual(travel_times["Walk"], 122)
        self.assertAlmostEqual(travel_times["Bike"], 40.333333333333336)
        self.assertAlmostEqual(travel_times["Bus"], 33.14285714285714)
