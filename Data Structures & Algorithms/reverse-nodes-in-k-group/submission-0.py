# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_list(node):
            prev = None
            cur = node

            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev


        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        dummy = ListNode(0,head)
        leftPrev = dummy
        

        while length >= k:
            right = leftPrev
            for _ in range(k):
                right = right.next 
                
            rightNext = right.next
            right.next = None
            tail = leftPrev.next
            newhead = reverse_list(tail)
            tail.next = rightNext
            leftPrev.next = newhead
            leftPrev = tail
            length -= k

        
        return dummy.next
            