# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr: ListNode = ListNode()
        head: ListNode = curr
        carry: int = 0

        while l1 or l2 or carry:
            naive_sum: int = \
                (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = naive_sum // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr.next = ListNode(naive_sum % 10)
            curr = curr.next

        return head.next