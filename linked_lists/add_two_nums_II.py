# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self, lst):
        prev = None
        cur = lst
        
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        return prev
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse_list(l1)
        l2 = self.reverse_list(l2)
        dummy = ListNode()
        cur = dummy
        carry = 0
        
        while l1 or l2 or carry:
            if not l1:
                x = 0
            else:
                x = l1.val
            if not l2:
                y = 0
            else:
                y = l2.val
            sum = x + y + carry
            carry = sum // 10
            cur.next = ListNode(val=sum % 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            cur = cur.next
            
        return self.reverse_list(dummy.next)
        