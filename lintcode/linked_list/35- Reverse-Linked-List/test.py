# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#           https://www.lintcode.com/problem/35/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 20-Sep-2022  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


import unittest

from .solution import Solution
from utils.linked_list_serializer import SerializerForLinkedList


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.reverse_1 = Solution().reverse_1
        self.reverse_2 = Solution().reverse_2

    def test_solution(self):
        head = SerializerForLinkedList.deserialize('null')
        result = self.reverse_1(head)
        self.assertEqual(SerializerForLinkedList.serialize(result), 'null')
        result = self.reverse_2(head)
        self.assertEqual(SerializerForLinkedList.serialize(result), 'null')

        head = SerializerForLinkedList.deserialize('1->null')
        result = self.reverse_1(head)
        self.assertEqual(SerializerForLinkedList.serialize(result), '1->null')
        result = self.reverse_2(head)
        self.assertEqual(SerializerForLinkedList.serialize(result), '1->null')

        head = SerializerForLinkedList.deserialize('1->2->3->null')
        result = self.reverse_1(head)
        self.assertEqual(SerializerForLinkedList.serialize(result), '3->2->1->null')
        result = self.reverse_2(result)
        self.assertEqual(SerializerForLinkedList.serialize(result), '1->2->3->null')

        head = SerializerForLinkedList.deserialize('1->2->3->4')
        result = self.reverse_1(head)
        self.assertEqual(SerializerForLinkedList.serialize(result), '4->3->2->1->null')
        result = self.reverse_2(result)
        self.assertEqual(SerializerForLinkedList.serialize(result), '1->2->3->4->null')
