# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        elif not head.next:
            return head

        odd, even = head, head.next
        even_start = even
        
        while odd and odd.next and even and even.next:
            next_odd, next_even = odd.next.next, even.next.next
            odd.next, even.next = next_odd, next_even
            odd, even = next_odd, next_even

        odd.next = even_start

        return head
