# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def find_min(lists):
            least = float('inf')
            idx = -1
            node = None
            for i, head in enumerate(lists):
                if head and head.val < least:
                    least = head.val
                    idx = i
                    node = head
            return idx, node

        dummy = ListNode(0)
        tail = dummy

        while True:
            idx, node = find_min(lists)
            if idx == -1:
                break
            tail.next = node
            tail = tail.next
            lists[idx] = node.next
        return dummy.next