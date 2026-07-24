# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
             
            if slow == fast:
            # when there is a found then the 
            # head to cycle start &
            #meeting point (i.e slow == fast) to cycle start length is equal
            # proven using the algrebic formulation the intitutin is should remember 
            #sujal always remember the intiution
                ptr = head 
                while ptr!= slow:
                    ptr = ptr.next
                    slow = slow.next

                return ptr
        return None
        