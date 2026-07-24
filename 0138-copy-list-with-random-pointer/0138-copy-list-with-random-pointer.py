"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmp = {}
        curr = head

        """if not head:
            return None 
        To handle the starting edge case else last la lilyache me 
            """
        # hashmap banavla for deep cpy
        while curr:
            newnode = Node(curr.val)
            hashmp[curr] = newnode
            curr =curr.next
        # join the random and next to connect the node
        curr = head
        while curr:
            copy = hashmp[curr]
            
            if curr.next:
                copy.next =  hashmp[curr.next]
            else:
                copy.next = None
            #copy.next = hashmp[curr.next] if curr.next else None
            if curr.random:
                copy.random =  hashmp[curr.random]
            else:
                copy.random = None
            curr = curr.next
            #copy.random = hashmp[curr.random] if curr.random else None
        # return head    
        return hashmp[head] if head != None else None
        