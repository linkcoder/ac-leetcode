# coding: utf-8


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    @staticmethod
    def addTwoNumbers(self,l1: ListNode, l2: ListNode) -> ListNode:
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """

        dump_head = ListNode(0)
        p = l1
        q = l2
        curr = dump_head

        carry = 0
        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            result = x + y + carry
            carry = int(result / 10)
            curr.next = ListNode(result % 10)
            curr = curr.next
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        # 99 + 1 = 100
        if carry > 0:
            curr.next = ListNode(carry)

        return dump_head.next


if __name__ == "__main__":
    n11 = ListNode(2)
    n12 = ListNode(4)
    n13 = ListNode(3)
    
    n11.next = n12
    n12.next = n13

    n21 = ListNode(5)
    n22 = ListNode(6)
    n23 = ListNode(4)

    n21.next = n22
    n22.next = n23

    result_list = Solution.addTwoNumbers(n11, n21)

    while result_list is not None:
        print(result_list.val)
        result_list = result_list.next
