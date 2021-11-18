# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/75/
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
        self.test_method = Solution().findPeak

    def test_solution(self):
        result = self.test_method([1, 2, 4, 8, 6, 3])
        self.assertEqual(result, 3)
        result = self.test_method([1, 2, 1, 3, 4, 5, 7, 6])
        self.assertIn(result, {1, 6})
        result = self.test_method([1, 2, 3, 4, 1])
        self.assertEqual(result, 3)
        result = self.test_method([1, 3, 1, 3, 1])
        self.assertIn(result, {1, 3})
        result = self.test_method([8, 10, 9])
        self.assertEqual(result, 1)

        result = self.test_method([])
        self.assertEqual(result, -1)
        result = self.test_method(None)
        self.assertEqual(result, -1)
