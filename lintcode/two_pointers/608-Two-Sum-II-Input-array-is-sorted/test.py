# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/608/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 19-Nov-2021  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


import unittest

from .solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_method = Solution().twoSum

    def test_solution(self):
        result = self.test_method([2, 7, 11, 15], 9)
        self.assertEqual(result, [1, 2])
        result = self.test_method([2, 3], 5)
        self.assertEqual(result, [1, 2])
        result = self.test_method([1, 3, 5, 7, 10], 10)
        self.assertEqual(result, [2, 4])
        result = self.test_method([1, 3, 5, 7, 10], 12)
        self.assertEqual(result, [3, 4])

        result = self.test_method([], 5)
        self.assertEqual(result, [])
        result = self.test_method(None, 5)
        self.assertEqual(result, [])
        result = self.test_method([1, 3, 5, 7, 9], 15)
        self.assertEqual(result, [])
