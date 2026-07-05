# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = num2 = 0

        temp = l1
        i = 0
        while temp:
            num1 += (pow(10,i) * temp.val)
            i += 1
            temp = temp.next
        
        temp = l2
        i = 0
        while temp:
            num2 += (pow(10,i) * temp.val)
            i += 1
            temp = temp.next
        
        res = num1 + num2

        if res == 0:
            return ListNode(0,None)

        head = ListNode(res%10,None)
        node = head
        res //= 10
        while res:
            node.next = ListNode(res%10,None)
            node = node.next
            res //= 10
        
        return head
        
        