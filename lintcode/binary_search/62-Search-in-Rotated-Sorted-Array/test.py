# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/62/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 17-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


import unittest

from .solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_method = Solution().search

    def test_solution(self):
        result = self.test_method([4, 5, 1, 2, 3], 5)
        self.assertEqual(result, 1)
        result = self.test_method([4, 5, 1, 2, 3], 1)
        self.assertEqual(result, 2)
        result = self.test_method([4, 5, 1, 2, 3], 0)
        self.assertEqual(result, -1)
        result = self.test_method([1, 3, 5, 6, 8], 6)
        self.assertEqual(result, 3)
        result = self.test_method([1, 3, 5, 6, 8], 9)
        self.assertEqual(result, -1)

        result = self.test_method([], 2)
        self.assertEqual(result, -1)
        result = self.test_method(None, 26)
        self.assertEqual(result, -1)
