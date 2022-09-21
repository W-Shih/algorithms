# =================================================================================================
#                                  All Rights Reserved.
# =================================================================================================
# File description:
#       Serialize and deserialize a linked list
#
# =================================================================================================
#    Date      Name                    Description of Change
# 20-Sep-2022  Wayne Shih              Initial create
# $HISTORY$
# =================================================================================================


from data_types.types import (
    ListNode,
)


class SerializerForLinkedList(object):

    @classmethod
    def serialize(cls, head: ListNode) -> str:
        if head is None:
            return 'null'

        nodes_str_vals = []
        curt = head
        while curt is not None:
            nodes_str_vals.append(str(curt.val))
            curt = curt.next

        return '->'.join(nodes_str_vals) + '->null'

    @classmethod
    def deserialize(cls, data: str) -> ListNode:
        if data == 'null':
            return None

        data_list = data.split('->')
        if data_list[-1] != 'null':
            data_list.append('null')

        head, next_node = None, None
        for i in range(len(data_list) - 2, -1, -1):
            node = ListNode(int(data_list[i]), next_node)
            if i == 0:
                head = node
            next_node = node

        return head
