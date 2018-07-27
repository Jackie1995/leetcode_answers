# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 00:53:35 2018

@author: jikang

leetcode83 删除有序链表中的重复元素

题目描述
给定一个有序链表，请删除其中的重复元素，使得原链表的元素仅出现一次。

样例1
输入：1->1->2
输出：1->2
样例2
输入：1->1->2->3->3
输出：1->2->3
"""
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 这种问题场景下，头节点不会发生改变。
        # 定义一个在链表上移动的指针。
        pos = head
        while pos:
            while pos.next and pos.next.val == pos.val:
                pos.next = pos.next.next
            pos = pos.next
        return head
    
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
    myval = [1,1,2,3,3]
    head = generate_linked_list(myval)
    print('输入的链表如下：')
    print_linked_list(head)
    
    mysol = Solution()
    myhead = mysol.deleteDuplicates(head)
    print('输出的链表如下,删除了其中的重复项之后的链表是：')
    print_linked_list(myhead)    
                