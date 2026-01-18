# 876. Middle of the Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # Мое решение состоит в том, чтобы посчитать сначала количество элементов, а потом вывести элемент, деленный на 2
        # O(n)
        # n = 1
        # cur = head
        # while cur:
        #     n += 1
        #     cur = cur.next
        # cur = head


        # ind = 1
        # n = n // 2 if n % 2 == 0 else n // 2 + 1
        # while cur:
        #     if ind == n:
        #         return cur
        #     cur = cur.next
        #     ind += 1
        # return cur


        # Решение лучше (  O(n)  ):
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
head = ListNode()
array = [ListNode(x) for x in [1,2,3,4,5]]
curr = head
for elem in array:
    curr.next = elem
    curr = curr.next
print(Solution().middleNode(head))