# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/521/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 19-Nov-2021  Wayne Shih              Initial create
# 21-Sep-2022  Wayne Shih              Add test for another solution by hash
# $HISTORY$
# =================================================================================================


import unittest

from .solution import Solution


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.test_method_1 = Solution().deduplication_by_ptrs
        self.test_method_2 = Solution().deduplication_by_hash

    def test_solution(self):
        # <Wayne Shih> 21-Sep-2022
        # Test deduplication_by_ptrs()
        result = self.test_method_1([4, 5, 1, 2, 3])
        self.assertEqual(result, 5)
        result = self.test_method_1([4, 1, 1, 2, 3])
        self.assertEqual(result, 4)
        result = self.test_method_1([4, 1, 1, 1, 1])
        self.assertEqual(result, 2)
        result = self.test_method_1([1, 1, 1, 1])
        self.assertEqual(result, 1)

        result = self.test_method_1([])
        self.assertEqual(result, 0)
        result = self.test_method_1(None)
        self.assertEqual(result, 0)

        # <Wayne Shih> 21-Sep-2022
        # Test deduplication_by_hash()
        result = self.test_method_2([4, 5, 1, 2, 3])
        self.assertEqual(result, 5)
        result = self.test_method_2([4, 1, 1, 2, 3])
        self.assertEqual(result, 4)
        result = self.test_method_2([4, 1, 1, 1, 1])
        self.assertEqual(result, 2)
        result = self.test_method_2([1, 1, 1, 1])
        self.assertEqual(result, 1)

        result = self.test_method_2([])
        self.assertEqual(result, 0)
        result = self.test_method_2(None)
        self.assertEqual(result, 0)

