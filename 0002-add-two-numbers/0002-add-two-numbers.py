# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy
        carry = 0
        # so no digit is leave
        while (list1 or list2 or carry):
            a = list1.val if list1 else 0
            b = list2.val if list2 else 0
            total = a + b + carry
            # use tisng to separate the digit ad carry
            digit = total%10
            carry = total//10
            #attach new node to the tail
            newnode = ListNode(digit)
            tail.next= newnode
            tail = newnode
            #move both list
            if list1:
                list1 = list1.next
            if list2:
                list2 = list2.next
        return dummy.next

