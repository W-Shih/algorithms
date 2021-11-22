# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/49/
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
        self.test_method = Solution().sortLetters

    def test_solution(self):
        chars = ['a', 'b', 'A', 'c', 'D']
        self.test_method(chars)
        self.assertCountEqual(chars[:3], ['a', 'b', 'c'])
        self.assertCountEqual(chars[3:], ['A', 'D'])

        chars = ['A', 'B', 'C']
        self.test_method(chars)
        self.assertCountEqual(chars, ['A', 'B', 'C'])

        chars = ['a', 'b', 'c']
        self.test_method(chars)
        self.assertCountEqual(chars, ['a', 'b', 'c'])

        chars = ['a', 'b', 'A', 'c', 'D', 'e']
        self.test_method(chars)
        self.assertCountEqual(chars[:4], ['a', 'b', 'c', 'e'])
        self.assertCountEqual(chars[4:], ['A', 'D'])

        chars = ['a']
        self.test_method(chars)
        self.assertEqual(chars, ['a'])

        chars = []
        self.test_method(chars)
        self.assertEqual(chars, [])

        chars = None
        self.test_method(chars)
        self.assertEqual(chars, None)
