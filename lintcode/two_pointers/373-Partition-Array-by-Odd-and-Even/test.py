# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/373/
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
        nums = [3, 2, 2, 1]
        self.test_method(nums)
        self.assertCountEqual(nums[:2], [1, 3])
        self.assertCountEqual(nums[2:], [2, 2])

        nums = [3, 2, 1]
        self.test_method(nums)
        self.assertCountEqual(nums[:2], [1, 3])
        self.assertCountEqual(nums[2:], [2])

        nums = [1, 2, 3, 4]
        self.test_method(nums)
        self.assertCountEqual(nums[:2], [1, 3])
        self.assertCountEqual(nums[2:], [2, 4])

        nums = [1, 1, 1, 1]
        self.test_method(nums)
        self.assertEqual(nums, [1, 1, 1, 1])

        nums = [1, 4, 2, 3, 5, 6]
        self.test_method(nums)
        self.assertCountEqual(nums[:3], [1, 3, 5])
        self.assertCountEqual(nums[3:], [2, 4, 6])

        nums = [2]
        self.test_method(nums)
        self.assertEqual(nums, [2])

        nums = [2, 2]
        self.test_method(nums)
        self.assertEqual(nums, [2, 2])

        nums = []
        self.test_method(nums)
        self.assertEqual(nums, [])

        nums = None
        self.test_method(nums)
        self.assertEqual(nums, None)
