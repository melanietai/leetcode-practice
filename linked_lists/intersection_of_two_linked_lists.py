# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         bset = set()
        
#         while headB:
#             bset.add(headB)
#             headB = headB.next
        
#         while headA:
#             if headA in bset:
#                 return headA
#             headA = headA.next
#         return None

        pA = headA
        pB = headB
        
        while pA != pB:
            if not pA:
                pA = headB
            else:
                pA = pA.next
            
            if not pB:
                pB = headA
            else:
                pB = pB.next
        
        return pA