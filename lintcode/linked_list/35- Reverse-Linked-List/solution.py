# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       https://www.lintcode.com/problem/35/
#
# =================================================================================================
#    Date      Name                    Description of Change
# 20-Sep-2022  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


from data_types.types import ListNode


class Solution:

    def reverse_1(self, head: ListNode) -> ListNode:
        """
        @param head: ListNode
        @return: The new head of reversed linked list.
        """
        if head is None:
            return head

        prev, curt = None, head
        while curt is not None:
            tmp = curt.next
            curt.next = prev
            prev = curt
            curt = tmp

        return prev

    def reverse_2(self, head: ListNode) -> ListNode:
        """
        @param head: ListNode
        @return: The new head of reversed linked list.
        """
        if head is None:
            return head

        dummy = ListNode(-1, head)
        prev, curt = dummy, dummy.next

        # d->1->2->n
        # p  c
        while curt is not None:
            tmp = curt.next
            curt.next = prev
            prev = curt
            curt = tmp

        # d<->1<-2  n
        #     h  p  c
        dummy.next = prev
        head.next = curt
        # d->2->1->n
        #    p  h  c

        return dummy.next
