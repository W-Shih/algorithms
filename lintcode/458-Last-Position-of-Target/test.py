# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#           https://www.lintcode.com/problem/458/
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
        self.lastPosition = Solution().lastPosition

    def test_solution(self):
        result = self.lastPosition([2, 3, 3, 4, 5], 2)
        self.assertEqual(result, 0)
        result = self.lastPosition([1, 2, 2, 4, 5], 2)
        self.assertEqual(result, 2)
        result = self.lastPosition([1, 2, 2, 2, 5], 2)
        self.assertEqual(result, 3)
        result = self.lastPosition([1, 2, 2, 2, 2], 2)
        self.assertEqual(result, 4)

        result = self.lastPosition([1, 2, 3, 4, 5], 6)
        self.assertEqual(result, -1)
        result = self.lastPosition([1, 2, 3, 3, 5], 4)
        self.assertEqual(result, -1)
        result = self.lastPosition([], 2)
        self.assertEqual(result, -1)
        result = self.lastPosition(None, 2)
        self.assertEqual(result, -1)
