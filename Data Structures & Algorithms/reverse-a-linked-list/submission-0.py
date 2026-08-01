# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        old = None        
        if head != None:
            x = head.next
        atual = head
        valores = []

        if atual != None:
            while atual.next != None:
                atual.next = old
                old = atual
                atual = x
                x = atual.next
        
            atual.next = old

        return atual
            
            
        
            
                