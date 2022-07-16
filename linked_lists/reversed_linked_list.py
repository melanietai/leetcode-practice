class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def reverse_list(self, head):
        if not head or head.next:
            return head

        prev = None
        cur = head
        
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        return prev