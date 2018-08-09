# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 23:36:29 2018

@author: jikang

leetcode92:反转链表

题目描述
请将链表中第 nn 个节点和第 mm 个节点之间的部分翻转。
链表最多只能遍历一遍。

注意：1≤m≤n≤1 链表长度。

样例
输入：1->2->3->4->5->NULL, m = 2, n = 4
输出：1->4->3->2->5->NULL
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
         
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        dummy  = ListNode(-1)
        dummy.next = head
        cursor = dummy
        pos = 0
        while pos < m-1:
            cursor = cursor.next
            pos += 1
        node_m_before = cursor
        node_m = cursor.next
        second = cursor
        first = cursor.next
        while pos < n:
            next_node = first.next
            first.next = second
            second = first
            first = next_node
            pos += 1
        node_n = second
        node_n_next = first
        node_m_before.next = node_n
        node_m.next = node_n_next
        return dummy.next

# 自定义生成链表的函数：
def generate_linked_list(myval):
    mydummy = ListNode(-1)
    activenode = mydummy
    for val in myval:
        activenode.next = ListNode(val)
        activenode = activenode.next
    myhead = mydummy.next
    return myhead        

#自定义打印链表的函数：
def print_linked_list(head):
    active_node = head
    while active_node:
        print(active_node.val)
        active_node = active_node.next    
        
if __name__ == "__main__":
    myval = [1,2,3,4,5]
    head = generate_linked_list(myval)
    print('输入的链表如下：')
    print_linked_list(head)
    
    mysol = Solution()
    myhead = mysol.reverseBetween(head,m=2,n=4)
    print('输出的链表如下,反转之后的链表是：')
    print_linked_list(myhead)     
        
            
        
        
