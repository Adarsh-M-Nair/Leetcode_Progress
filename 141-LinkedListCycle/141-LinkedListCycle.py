# Last updated: 7/18/2026, 8:32:23 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # If the list is empty or has only one node, there can't be a cycle.
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        # If the loop finishes, it means the fast pointer reached the end of the list.
        return False