# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = mid = head
        prev = None

        # Search for midpoint while reversing the first half
        while fast and fast.next:
            fast = fast.next.next
            curr, mid = mid, mid.next
            curr.next, prev = prev, curr

        # If there are odd elements, ignore the midpoint
        if fast:
            mid = mid.next

        # Compare the first half and the second half
        while mid and curr:
            if mid.val != curr.val:
                return False
            mid, curr = mid.next, curr.next
        
        return True
