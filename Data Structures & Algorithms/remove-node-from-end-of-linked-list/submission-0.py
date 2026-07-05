# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        length = 0

        while temp:
            length += 1
            temp = temp.next
        
        dummy = ListNode(0,head)
        curr = dummy
        idx = length - n

        while idx:
            curr = curr.next
            idx -= 1
        
        curr.next = curr.next.next

        return dummy.next


