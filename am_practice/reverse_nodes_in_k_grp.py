"""
25. Reverse Nodes in k-Group
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        pt = head
        while count < k and pt:
            pt = pt.next
            count += 1
        if count == k:
            reversed_head = self.reverse_ll(head, k)
            head.next = self.reverseKGroup(pt, k)
            return reversed_head
        return head
            
    
    
    def reverse_ll(self, head, k):
        new_head = None
        pt = head
        while k:
            next_node = pt.next
            pt.next = new_head
            new_head = pt
            pt = next_node
            k -= 1
        return new_head
    