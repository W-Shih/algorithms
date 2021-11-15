# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#           https://www.lintcode.com/problem/457/
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
        self.find_position = Solution().find_position

    def test_solution(self):
        result = self.find_position([1, 2, 3, 4, 5], 2)
        self.assertEqual(result, 1)
        result = self.find_position([1, 2, 2, 4, 5], 2)
        self.assertIn(result, {1, 2})
        result = self.find_position([1, 2, 2, 4, 5], 1)
        self.assertEqual(result, 0)
        result = self.find_position([1, 2, 2, 4, 5], 5)
        self.assertEqual(result, 4)

        result = self.find_position([1, 2, 3, 4, 5], 6)
        self.assertEqual(result, -1)
        result = self.find_position([], 2)
        self.assertEqual(result, -1)
        result = self.find_position(None, 2)
        self.assertEqual(result, -1)
