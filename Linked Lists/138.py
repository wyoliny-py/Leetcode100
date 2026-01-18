# 138. Copy List with Random Pointer
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        hash = {}
        cur = head
        while cur:
            hash[cur] = Node(x=cur.val)
            cur = cur.next

        curr = head
        while curr:
            hash[curr].next = hash[curr.next] if curr.next else None
            hash[curr].random = hash[curr.random] if curr.random else None
            curr = curr.next
        return hash[head]