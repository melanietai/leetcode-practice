class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def remove_sorted_array(array):
        pass

    def delete_duplicate(self, head):
        cur = head 
        dup_vals = {}

        while cur:
            dup_vals[cur.val] = dup_vals.get(cur.val, 0) + 1
        
        dummy = ListNode(next=head)
        cur = head
        prev = dummy

        while cur:
            if dup_vals[cur.val] > 1:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        ind_to_remove = length - n
        
        cur = head
        dummy = ListNode(next=head)
        prev = dummy
        cur_ind = 0
        while cur:
            if cur_ind == ind_to_remove:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
            cur_ind += 1

        return dummy.next
        
