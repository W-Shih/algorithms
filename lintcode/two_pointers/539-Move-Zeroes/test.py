# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/539/
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
        self.test_method = Solution().moveZeroes

    def test_solution(self):
        nums = [0, 1, 0, 3, 12]
        self.test_method(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

        nums = [0, 0, 0, 3, 1]
        self.test_method(nums)
        self.assertEqual(nums, [3, 1, 0, 0, 0])

        nums = [0, 0, 0]
        self.test_method(nums)
        self.assertEqual(nums, [0, 0, 0])

        nums = []
        self.test_method([])
        self.assertEqual(nums, [])

        nums = None
        self.test_method(nums)
        self.assertEqual(nums, None)
