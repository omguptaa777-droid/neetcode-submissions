# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        node = dummy
        if not lists:
            return dummy.next
        l1 = lists[0]

        for i in range(1,len(lists)):
            if not lists[i]:
                continue
            l2 = lists[i]

            while l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            
            if not l1:
                node.next = l2
            else:
                node.next = l1
            
            l1 = dummy.next
            node = dummy
        
        return dummy.next