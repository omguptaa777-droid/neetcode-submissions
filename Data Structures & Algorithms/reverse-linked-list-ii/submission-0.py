# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy

        for _ in range(left-1):
            prev = prev.next
        
        sublist_head = prev.next
        sublist_tail = sublist_head

        for _ in range(right-left):
            sublist_tail = sublist_tail.next
        
        nextNode = sublist_tail.next
        sublist_tail.next = None
        reversed_list = self.reversed_linkedlist(sublist_head)
        prev.next = reversed_list
        sublist_head.next = nextNode

        return dummy.next
    
    def reversed_linkedlist(self,node):
        prev = None
        curr = node

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
        

        