# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/521/
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
        self.test_method = Solution().deduplication

    def test_solution(self):
        result = self.test_method([4, 5, 1, 2, 3])
        self.assertEqual(result, 5)
        result = self.test_method([4, 1, 1, 2, 3])
        self.assertEqual(result, 4)
        result = self.test_method([4, 1, 1, 1, 1])
        self.assertEqual(result, 2)
        result = self.test_method([1, 1, 1, 1])
        self.assertEqual(result, 1)

        result = self.test_method([])
        self.assertEqual(result, 0)
        result = self.test_method(None)
        self.assertEqual(result, 0)
