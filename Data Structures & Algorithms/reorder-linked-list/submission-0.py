# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        dummy = ListNode(-1)
        tail = dummy
        l1 = head
        l2 = prev

        while l1 and l2:
            tail.next = l1
            l1 = l1.next
            tail = tail.next
            tail.next = l2
            l2 = l2.next
            tail = tail.next
        tail.next = l1 if l1 else l2