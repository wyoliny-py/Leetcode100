# 141. Linked List Cycle
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Мое решение (не эффективно) (1)
        # d = set()
        # curr = head
        # while curr:
        #     if curr.val not in d:
        #         curr = curr.next
        #         d.add(curr.val)
        #     else:
        #         return True
        # return False

        # Мое решение (не эффективно) (1)
        # curr = head
        # while curr:
        #     if curr.val != -10 ** 5 - 1:
        #         curr.val = -10 ** 5 - 1
        #         curr = curr.next
        #     else:
        #         return True
        # return False

        dum = ListNode()
        dum.next = head
        slow = fast = dum
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False
head1 = ListNode()
array = [ListNode(x) for x in [3, 2, 0, -4]]
curr = head1
for elem in array:
    curr.next = elem
    curr = curr.next

head2 = ListNode()
array = [ListNode(x) for x in [1, 3, 4]]
curr = head2
for elem in array:
    curr.next = elem
    curr = curr.next