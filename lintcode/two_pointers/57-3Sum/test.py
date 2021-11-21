# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/57/
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
        self.test_method = Solution().threeSum

    def test_solution(self):
        result = self.test_method([-1, 2, -1, -4])
        self.assertCountEqual(result, [[-1, -1, 2]])
        result = self.test_method([-1, -1, -1, -4])
        self.assertCountEqual(result, [])
        result = self.test_method([1, 1, 1, 1, -2])
        self.assertCountEqual(result, [[-2, 1, 1]])
        result = self.test_method([1, 3, 5, 7, 10, 2, 8, 2, -10])
        self.assertCountEqual(result, [[-10, 2, 8], [-10, 3, 7]])
        result = self.test_method([-1, 0, 1, 2, -1, -4])
        self.assertCountEqual(result, [[-1, 0, 1], [-1, -1, 2]])
        result = self.test_method([-5, -5, 2, 3, 2, 3, 3])
        self.assertCountEqual(result, [[-5, 2, 3]])

        result = self.test_method([])
        self.assertCountEqual(result, [])
        result = self.test_method([5])
        self.assertCountEqual(result, [])
        result = self.test_method(None)
        self.assertCountEqual(result, [])
