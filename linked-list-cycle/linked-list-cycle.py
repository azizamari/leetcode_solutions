# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None: return False
        cur=head
        while cur:
            if cur.val=="x": return True
            cur.val="x"
            cur=cur.next
        return False