# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 00:22:48 2018

@author: jikang

leetcode 19 删除链表中的节点

题目描述
给定一个单向链表，要求删除从结尾数第nn个结点，并返回修改后的表头。

样例
给定数组单向链表 1->2->3->4->5 ，以及 n = 2 ，修改后的链表为 1->2->3->5。

Note
nn总是合法的。
尝试使用一次遍历完成本题。
"""
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 定义2个指针 first second。当first走到末尾节点的时候，second指向的像一个节点需要删除。
        # 特殊的边界情况：如果要删除的节点是头节点的话，就意味着返回链表的头节点需要改变，所以要先单独处理。
        # 这种情况只要通过设置虚拟头节点dummy，让first和second的初始位置都指向dummy就可以解决。
        dummy = ListNode(-1)
        dummy.next = head
        first = dummy
        second = dummy
        # first指针先向后移动n个位置。
        for i in range(n):
            first = first.next
        # 然后两个指针一起向后移动，直到first的下一个指向None
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
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
    
    myn = 2
    mysol = Solution()
    myhead = mysol.removeNthFromEnd(head,myn)
    print('输出的链表如下：删掉从末位数第{0}个节点'.format(myn))
    print_linked_list(myhead)