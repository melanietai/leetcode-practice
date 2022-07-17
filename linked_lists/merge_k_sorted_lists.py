# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        # base case
        if not list1:
            return list2
        if not list2:
            return list1
    
        # recursive case
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        lst1, lst2 = lists[0], lists[1]
        lists = lists[2:]
        
        new_lst = self.mergeTwoLists(lst1, lst2)
        lists.append(new_lst)
        
        return self.mergeKLists(lists)
        
#     def mergeKLists(self, lists):
#         dummy = ListNode()
#         cur = dummy
        
#         lists = [list for list in lists if list]
#         while lists:
#             smallest = lists[0]
#             smallestIndex = 0
#             for i, lst in enumerate(lists):
#                 if lst.val < smallest.val: 
#                     smallest = lst
#                     smallestIndex = i


#             if not smallest.next:
#                 lists.pop(smallestIndex)
#             else:
#                 lists[smallestIndex] = smallest.next
#             cur.next = smallest
#             smallest.next = None
#             cur = cur.next
#         return dummy.next
        