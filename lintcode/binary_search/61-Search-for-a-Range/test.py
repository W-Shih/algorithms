# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/61/
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
        self.test_method = Solution().searchRange

    def test_solution(self):
        result = self.test_method([5, 7, 7, 8, 8, 10], 8)
        self.assertEqual(result, [3, 4])
        result = self.test_method([3, 4, 5, 8], 4)
        self.assertEqual(result, [1, 1])
        result = self.test_method([1, 3, 5, 6], 4)
        self.assertEqual(result, [-1, -1])
        result = self.test_method([1, 3, 5, 6], 0)
        self.assertEqual(result, [-1, -1])
        result = self.test_method([1, 2, 3, 3, 5], 3)
        self.assertEqual(result, [2, 3])
        result = self.test_method([1, 1, 1, 1, 1], 1)
        self.assertEqual(result, [0, 4])

        result = self.test_method([], 9)
        self.assertEqual(result, [-1, -1])
        result = self.test_method(None, 2)
        self.assertEqual(result, [-1, -1])
