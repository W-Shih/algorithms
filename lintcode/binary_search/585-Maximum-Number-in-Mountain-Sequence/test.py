# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/585/
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
        self.test_method = Solution().mountainSequence

    def test_solution(self):
        result = self.test_method([1, 2, 4, 8, 6, 3])
        self.assertEqual(result, 8)
        result = self.test_method([10, 9, 8, 7])
        self.assertEqual(result, 10)
        result = self.test_method([4, 5, 6, 7])
        self.assertEqual(result, 7)
        result = self.test_method([1, 3, 5, 6, 4])
        self.assertEqual(result, 6)
        result = self.test_method([10, 9])
        self.assertEqual(result, 10)
        result = self.test_method([9, 10])
        self.assertEqual(result, 10)
        result = self.test_method([10])
        self.assertEqual(result, 10)

        result = self.test_method([])
        self.assertEqual(result, float('inf'))
        result = self.test_method(None)
        self.assertEqual(result, float('inf'))
