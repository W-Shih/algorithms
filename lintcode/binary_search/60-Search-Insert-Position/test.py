# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#           https://www.lintcode.com/problem/60/
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
        self.searchInsert = Solution().searchInsert

    def test_solution(self):
        result = self.searchInsert([1, 3, 5, 6], 5)
        self.assertEqual(result, 2)
        result = self.searchInsert([1, 3, 5, 6], 2)
        self.assertEqual(result, 1)
        result = self.searchInsert([1, 3, 5, 6], 7)
        self.assertEqual(result, 4)
        result = self.searchInsert([1, 3, 5, 6], 0)
        self.assertEqual(result, 0)
        result = self.searchInsert([1, 2, 3, 3, 5], 1)
        self.assertEqual(result, 0)
        result = self.searchInsert([1, 2, 3, 3, 5], 5)
        self.assertEqual(result, 4)

        result = self.searchInsert([], 6)
        self.assertEqual(result, 0)
        result = self.searchInsert(None, 2)
        self.assertEqual(result, 0)
