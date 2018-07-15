# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 22:40:58 2018

@author: jikang
"""

class ListNode(object):
    def __init__(self, val,next_node = None):
        self.val = val
        self.next = next_node
    def add_next_node(self,next_node_val):
        self.next = ListNode(next_node_val)
        

node_list = [4,2,1,3]
dummy = ListNode(-1)
p = dummy
for val in node_list:
    newnode = ListNode(val)
    p.next  = newnode
    p = p.next    
    
dummy
current_node = dummy.next
while current_node:
    print(current_node.val)
    current_node = current_node.next
    
class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        while(head):
            next_node = head.next
            p = dummy
            while(p.next and p.next.val <= head.val):
                p = p.next
            head.next = p.next
            p.next = head
            head = next_node
        return dummy.next            
        
sol = Solution()
returned = sol.insertionSortList(head = dummy.next)

head = returned
head = current_node
while head:
    print(head.val)
    head = head.next
    
    