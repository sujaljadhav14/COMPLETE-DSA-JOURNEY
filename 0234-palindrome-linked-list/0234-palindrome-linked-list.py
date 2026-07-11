# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            #Take slow as middle
        #reverse the 2nd half
        prev=None
        curr=slow
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        #compare the 2 LL value not nodes
        while prev:
            if(head.val!=prev.val):
                return False
            head = head.next
            prev = prev.next
        return True

