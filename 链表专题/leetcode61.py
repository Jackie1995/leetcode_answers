# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 00:10:00 2018

@author: jikang

leetcode61: 链表平移

题目描述
给定一个链表，将链表向右循环移动 kk 次，kk 是非负整数。

样例1
输入：1->2->3->4->5->NULL, k = 2
输出：4->5->1->2->3->NULL
解释：
向右移动1步后：5->1->2->3->4->NULL
向右移动2步后：4->5->1->2->3->NULL
样例2
输入：0->1->2->NULL, k = 4
输出：2->0->1->NULL
解释：
向右移动1步：2->0->1->NULL
向右移动2步：1->2->0->NULL
向右移动3步：0->1->2->NULL
向右移动4步：2->0->1->NULL
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cursor = head
        length = 0
        while cursor:
            cursor = cursor.next
            length += 1
        k = k%length
        if k == 0:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        second = dummy
        pos = 0
        cursor = dummy
        while pos < k:
            pos += 1
            cursor = cursor.next
        first = cursor
        while first.next:
            first = first.next
            second = second.next
        new_end = second
        new_head = second.next
        middle = first
        dummy.next = new_head
        middle.next = head
        new_end.next = None
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
    myhead = mysol.rotateRight(head,k=2)
    print('输出的链表如下,反转之后的链表是：')
    print_linked_list(myhead)     
        
    

