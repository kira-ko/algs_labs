import unittest
from lab3.task4.src.task4 import count_segments_containing_points

class TestCountSegments(unittest.TestCase):
    def test_case_1(self):
        s = 2
        p = 3
        segments = [(0, 5), (7, 10)]
        points = [1, 6, 11]
        expected = [1, 0, 0]
        self.assertEqual(count_segments_containing_points(s, p, segments, points), expected)

    def test_case_2(self):
        s = 3
        p = 4
        segments = [(1, 4), (2, 6), (8, 10)]
        points = [1, 3, 5, 8]
        expected = [1, 2, 1, 1]
        self.assertEqual(count_segments_containing_points(s, p, segments, points), expected)

    def test_large_case(self):
        s = 1
        p = 5
        segments = [(-100000000, 100000000)]
        points = [-100000000, 0, 1, 99999999, 100000000]
        expected = [1, 1, 1, 1, 1]
        self.assertEqual(count_segments_containing_points(s, p, segments, points), expected)

    def test_no_overlap(self):
        s = 2
        p = 2
        segments = [(1, 2), (4, 5)]
        points = [3, 6]
        expected = [0, 0]
        self.assertEqual(count_segments_containing_points(s, p, segments, points), expected)

if __name__ == "__main__":
    unittest.main()