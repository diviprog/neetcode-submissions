# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        this = head
        while this:
            this = this.next
            count += 1
        if count == 1:
            return None
        to_remove = count-n
        this = head
        if to_remove==0:
            head = head.next
        for _ in range(1, to_remove):
            this = this.next
        
        this.next = this.next.next
        return head