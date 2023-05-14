# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        
        # Find the middle
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the second half
        prev, curr = None, slow.next
        while curr:
            nextp = curr.next
            curr.next = prev
            prev, curr = curr, nextp

        slow.next = None

        # Merge two lists
        head1, head2 = head, prev
        while head2:
            nextp = head1.next
            head1.next = head2
            head1, head2 = head2, nextp