# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/31/
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
        self.test_method = Solution().partitionArray

    def test_solution(self):
        result = self.test_method([3, 2, 2, 1], 2)
        self.assertEqual(result, 1)
        result = self.test_method([3, 2, 1], 1)
        self.assertEqual(result, 0)
        result = self.test_method([3, 2, 1], 2)
        self.assertEqual(result, 1)
        result = self.test_method([1, 1, 1, 1], 1)
        self.assertEqual(result, 0)
        result = self.test_method([1, 1, 1, 1], 2)
        self.assertEqual(result, 4)
        result = self.test_method([5], 3)
        self.assertEqual(result, 0)
        result = self.test_method([5], 6)
        self.assertEqual(result, 1)

        result = self.test_method([], 9)
        self.assertEqual(result, 0)
        result = self.test_method(None, 9)
        self.assertEqual(result, 0)
