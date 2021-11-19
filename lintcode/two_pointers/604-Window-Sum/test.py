# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/604/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 21-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


import unittest

from .solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_method = Solution().winSum

    def test_solution(self):
        result = self.test_method([4, 5, 1, 2, 3], 5)
        self.assertEqual(result, [15])
        result = self.test_method([4, 5, 1, 2, 3], 1)
        self.assertEqual(result, [4, 5, 1, 2, 3])
        result = self.test_method([4, 5, 1, 2, 3], 0)
        self.assertEqual(result, [])
        result = self.test_method([1, 3, 5, 6, 8], 6)
        self.assertEqual(result, [])
        result = self.test_method([1, 2, 7, 8, 5], 3)
        self.assertEqual(result, [10, 17, 20])

        result = self.test_method([], 2)
        self.assertEqual(result, [])
        result = self.test_method(None, 3)
        self.assertEqual(result, [])
