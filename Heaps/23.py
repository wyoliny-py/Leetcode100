# 23. Merge k Sorted Lists
# Definition for singly-linked list.
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        # O(n log n)
        heap = []
        counter = 0
        for lst in lists:
            cur = lst
            while cur:
                heapq.heappush(heap, (cur.val, counter, cur))
                cur = cur.next
                counter += 1

        if not heap:
            return None
        
        root = heapq.heappop(heap)[2]
        cur = root
        while heap:
            cur.next = heapq.heappop(heap)[2]
            cur = cur.next
        cur.next = None
    
        return root