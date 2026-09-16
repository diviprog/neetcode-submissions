# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_kth(node):
            for _ in range(k):
                if not node.next:
                    return None
                node = node.next
            return node
        
        def reverse(head, end):
            prev = end
            curr = head

            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = get_kth(group_prev)
            if not kth:
                break
            
            group_next = kth.next
            start = group_prev.next

            new_head = reverse(start, group_next)

            group_prev.next = new_head
            start.next = group_next

            group_prev = start
        
        return dummy.next