# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/159/
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
        self.test_method = Solution().findMin

    def test_solution(self):
        result = self.test_method([5, 7, 7, 8, 8, 10])
        self.assertEqual(result, 5)
        result = self.test_method([3, 4, 5, 8, 1, 2])
        self.assertEqual(result, 1)
        result = self.test_method([4, 5, 6, 7, 0, 1, 2])
        self.assertEqual(result, 0)
        result = self.test_method([8, 9, 1, 3, 5, 6])
        self.assertEqual(result, 1)

        result = self.test_method([])
        self.assertEqual(result, -float('inf'))
        result = self.test_method(None)
        self.assertEqual(result, -float('inf'))
