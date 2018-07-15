# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 21:35:39 2018

@author: jikang

leetcode206 题目描述

翻转一个单链表。

进一步： 能否同时给出迭代算法和递归算法？
样例入戏
输入：1->2->3->4->5->NULL
输出：5->4->3->2->1->NULL
"""
class ListNode(object):
    def __init__(self,val,next_node = None):
        self.val = val
        self.next = next_node
        
def getDummyNode(node_val_list):
    """
    node_val_list: list or tuple
    returnType: ListNode
    """
    dummy = ListNode(-1)
    p = dummy
    for val in node_val_list:
        newnode = ListNode(val)
        p.next  = newnode
        p = p.next
    return dummy


def printValueOfList(head_of_list):        
    """
    head_of_list : ListNode
    returnType : int (the length of the linkedlist)
    """
    p = head_of_list
    leng = 0
    while(p):
        print(p.val)
        leng += 1
        p = p.next
    return leng        




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        迭代思路：
        两个指针 first(初始位置：head.next) second(初始位置：head)
        迭代（循环）条件：first到达链表末尾
            1. 设置中间指针：p.使得 p = first
            2. first 前进到它next指针的位置
            3. 调整p的next指针，将其指向second
            4. second 指向 p.
         返回值：first 
         边界情况1：头节点为空 或者 只有一个头节点 ---- 不满足，需单独处理
         易错点：
         一定要记得把头节点的后继节点蛇者为空（None)否则会再链表中出现无限循环的环！
        """
        # 先用一个判断语句来判断处理特殊的边界情况
        if not (head and head.next):
            return head
        first = head.next
        second  = head
        # ！！注意！！ 一开始把下面这句给忘了
        head.next = None
        while first.next:
            p = first
            first = first.next
            p.next = second
            second = p
        first.next = second            
        return first
    
    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        递归思路：
        思考 reverseList2()函数可以做什么？
        答：该函数可以翻转一个链表，并返回新链表的头节点，也就是原链表的尾节点。
        现在考虑每次递归指利用改该函数反转两个相邻的节点。
        递归具体的实现：
        反转函数（head）：
            反转函数（head.next)
            head.next.next = head
            head.next = None
            递归函数返回值： head.next
            （特别注意递归函数的返回值的分类：是不是被调用栈的上层用来赋值？这里没有这个功能，所以一下子就得到返回值）
        ！难点：
            关于递归调用栈的返回值问题，这里为什么一定要有返回值呢？       
            tail这个值十分关键！ 只有存在返回值才可能一直把最后一个调用的结果传递到最原始的调用栈上。
        边界情况1：头节点为空 或者 只有一个头节点 ---- 不满足，需单独处理
        易错点：
         一定要记得把头节点的后继节点蛇者为空（None)否则会再链表中出现无限循环的环！
        """
        if not head or not head.next:
            return head
        tail = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return tail
    
        

if __name__ == "__main__":
    mydummy = getDummyNode([1,2,3,4,5])
    printValueOfList(mydummy.next)
    mysol = Solution()
    myhead = mysol.reverseList2(mydummy.next)
    printValueOfList(myhead)
