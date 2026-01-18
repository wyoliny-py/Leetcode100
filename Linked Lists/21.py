# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        # Failed

        # if list1 and list2:
        #     head = ListNode()
        #     cur = head
        #     while list1 and list2:
        #         if list1.val <= list2.val:
        #             temp = ListNode(list1.val)
        #             cur.next = temp
        #             temp.next = ListNode(list2.val)
        #         else:
        #             temp = ListNode(list2.val)
        #             cur.next = temp
        #             temp.next = ListNode(list1.val)
        #         cur = temp.next
        #         list1 = list1.next
        #         list2 = list2.next
        # else:
        #     if list1:
        #         return list1
        #     else:
        #         return list2
        # return head.next


        d = ListNode()
        curr = d
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        
        curr.next = list1 if list1 else list2
        return d.next