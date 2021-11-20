# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/533/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 20-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


import unittest

from .solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_method = Solution().twoSumClosest

    def test_solution(self):
        result = self.test_method([-1, 2, 1, -4], 4)
        self.assertEqual(result, 1)
        result = self.test_method([-1, -1, -1, -4], 4)
        self.assertEqual(result, 6)
        result = self.test_method([1, 1, 1, 1, 1], 2)
        self.assertEqual(result, 0)
        result = self.test_method([1, 3, 5, 7, 10, 2, 8, 3], 10)
        self.assertEqual(result, 0)
        result = self.test_method([1, 3, 5, 7, 10, 10, 2], 14)
        self.assertEqual(result, 1)

        result = self.test_method([], 3)
        self.assertEqual(result, float('inf'))
        result = self.test_method([5], 5)
        self.assertEqual(result, float('inf'))
        result = self.test_method(None, 5)
        self.assertEqual(result, float('inf'))
