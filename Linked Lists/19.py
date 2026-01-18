# 19. Remove Nth Node From End of List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        ind = length - n
        if ind == 0:
            return head.next
        
        cur = head
        for _ in range(ind - 1):
            cur = cur.next
        
        if cur.next:
            cur.next = cur.next.next
        return head
        
head = ListNode()
array = [ListNode(x) for x in [1, 2]]
curr = head
for elem in array:
    curr.next = elem
    curr = curr.next
print(Solution().removeNthFromEnd(head, 1))