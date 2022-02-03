# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.val(l1)
        b = self.val(l2)
        sum = str(a + b)
        
        node = None
        for i in sum:
            v = int(i)
            node = ListNode(v, node)
            
        return node
    
    def val(self, node):
        r = 0
        d = 1
        while node is not None:
            r += node.val * d
            d *= 10
            node = node.next
        return r
