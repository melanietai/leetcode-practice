# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        d_cur = dummy
        cur1 = l1
        cur2 = l2
        carry = 0
        
        while cur1 or cur2 or carry != 0:
            if cur1:
                x = cur1.val
            else:
                x = 0
            if cur2:
                y = cur2.val
            else:
                y = 0
            
            sum = x + y + carry
            carry = sum // 10
            d_cur.next = ListNode(sum % 10)
            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
            d_cur = d_cur.next
        
        return dummy.next
        