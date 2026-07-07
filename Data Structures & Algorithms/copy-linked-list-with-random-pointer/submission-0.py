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
        temp = head
        dummy = Node(0)
        prev = dummy
        hashmap = {}
        while temp:
            newNode = Node(temp.val)
            prev.next = newNode
            prev = newNode
            if temp not in hashmap:
                hashmap[temp] = newNode
            temp = temp.next 
        
        cur = head
        copiedList_cur = dummy.next
        while cur:
            temp = head

            while temp and temp != cur.random:
                temp = temp.next
            

            copiedList_cur.random = hashmap[temp] if temp else None
            cur = cur.next 
            copiedList_cur = copiedList_cur.next
        
        return dummy.next

