# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 23:50:33 2018

@author: jikang

leetcode206
题目描述
翻转一个单链表。

进一步： 能否同时给出迭代算法和递归算法？

样例
输入：1->2->3->4->5->NULL
输出：5->4->3->2->1->NULL

"""


# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution: #迭代的方法
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: #如果链表只包括0个或者1个头节点，不需要反转
            return head
        # 否则，需要反转
        second = head
        first = head.next  #first也是一个合法节点。
        while first: #迭代终止的条件
            tmp = first
            first = first.next
            tmp.next = second
            second = tmp #这里千万不要写成 second = second.next
        head.next = None
        return second
        
        
        
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
    myhead = mysol.reverseList(head)
    print('输出的链表如下,反转之后的链表是：')
    print_linked_list(myhead)     
        
        