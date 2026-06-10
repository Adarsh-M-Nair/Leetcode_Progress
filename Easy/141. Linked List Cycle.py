def hasCycle(self, head: Optional[ListNode]) -> bool: # type: ignore
  #if the lsit is empty or has only one node, it can't have a cycle.
  if not head or not head.next:
    return False
  slow = head
  fast = head.next
  while fast and fast.next:
    if slow == fast:
      return True
    slow = slow.next
    fast = fast.next.next 
  return False