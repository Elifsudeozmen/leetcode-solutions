# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        temp_head = ListNode(0)
        current = temp_head
        carry = 0  

        
        while l1 is not None or l2 is not None or carry > 0:
            
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            
            toplam = val1 + val2 + carry
            carry = toplam // 10         
            yeni_rakam = toplam % 10    

           
            current.next = ListNode(yeni_rakam)
            current = current.next

            
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next

        
        return temp_head.next
