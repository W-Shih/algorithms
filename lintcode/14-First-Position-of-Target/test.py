# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#           https://www.lintcode.com/problem/14/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 14-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


import unittest

from .solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.binarySearch = Solution().binarySearch

    def test_solution(self):
        result = self.binarySearch([2, 3, 3, 4, 5], 2)
        self.assertEqual(result, 0)
        result = self.binarySearch([1, 2, 2, 4, 5], 2)
        self.assertEqual(result, 1)
        result = self.binarySearch([1, 2, 2, 2, 5], 2)
        self.assertEqual(result, 1)
        result = self.binarySearch([1, 1, 1, 1, 2], 2)
        self.assertEqual(result, 4)

        result = self.binarySearch([1, 2, 3, 4, 5], 6)
        self.assertEqual(result, -1)
        result = self.binarySearch([1, 2, 3, 3, 5], 4)
        self.assertEqual(result, -1)
        result = self.binarySearch([], 2)
        self.assertEqual(result, -1)
        result = self.binarySearch(None, 2)
        self.assertEqual(result, -1)
        