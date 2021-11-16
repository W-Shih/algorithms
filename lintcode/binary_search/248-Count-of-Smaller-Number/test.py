# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#           https://www.lintcode.com/problem/248/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 15-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


import unittest

from .solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_method = Solution().countOfSmallerNumber

    def test_solution(self):
        result = self.test_method([1, 2, 7, 8, 5], [1, 8, 5])
        self.assertEqual(result, [0, 4, 2])
        result = self.test_method([3, 4, 5, 8], [2, 4])
        self.assertEqual(result, [0, 1])
        result = self.test_method([1, 3, 5, 6], [7])
        self.assertEqual(result, [4])
        result = self.test_method([1, 3, 5, 6], [0])
        self.assertEqual(result, [0])
        result = self.test_method([1, 2, 3, 3, 5], [1, 3])
        self.assertEqual(result, [0, 2])

        result = self.test_method([], [6])
        self.assertEqual(result, [0])
        result = self.test_method([], [1, 6])
        self.assertEqual(result, [0, 0])
        result = self.test_method(None, [2, 2])
        self.assertEqual(result, [0, 0])
