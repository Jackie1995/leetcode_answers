# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 10:22:26 2018

leetcode19题目：
给定一个单项链表，要求删除从结尾数第n个节点，并返回修改后的表头。
@author: jikang

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

   
class Solution:
    def removeNthFromEnd(self,head,n):
        """
        head: ListNode
        n : int
        returnType : ListNode
        第一个方法是采用了两次遍历：
        第一次遍历是求出链表的长度。
        第二次遍历是删除指定位置的节点。
        """ 
#       如果头节点为空的话，无论n取何值，都原样返回一个空的头节点。
        if not head:
            return head
#        第一次遍历：先求出链表的长度
        length = 0
        p = head
        while (p):# 注意这里求链表长度的时候，用的是while（p)而不是while(p.next).
            length += 1
            p = p.next
        # 执行到这里的时候，length就已经是链表的长度了。
        # 需要用if语句来单独处理的情况：就是 n == length 的情况，这种情况下，直接返回头节点的下一个节点。
        if n == length:
            return head.next
        p = head
        cur = 1
        while(cur < length-n):
            p = p.next
            cur += 1
        p.next = p.next.next
        return head
    
    def removeNthFromEnd2(self,head,n):
        """
        head: ListNode
        n : int
        returnType : ListNode
        思路：
        一次遍历，两个指针，间隔的节点数为n
        当快指针到达链表结尾的时候，慢指针指向的下一个节点需要从链表中删除
        难点：
        边界：当n== length的时候，也就是说要删除的节点是头节点的时候，需要单独讨论。
        一般的解决方法无法通过 删除节点为头节点的测试用例。
        """
        # 定义两个指针，first和second，它们最开始都指向头节点，两个指针的初始位置是指向头节点的虚拟结点指针。
        first = ListNode(-1,head)
        second = ListNode(-1,head)
        # first 指针先在链表上移动n个节点
        for _ in range(n):
            first  = first.next
        # 这里要先加一个特殊情况的检验，就是头节点发生改变的情况。直接返回头节点的下一个节点。
        if not first.next:
            return head.next
        # 然后first指针和second指针再一起向后移动。直到first指向链表末尾的节点为止。
        while(first.next):
            first = first.next
            second = second.next
        # 当first指针到达链表的末尾时，second指针指向的下一个节点就是要被删除的节点。
        second.next = second.next.next
        return head            
    
if __name__ == "__main__":
    dummy = getDummyNode(range(1,6))
    printValueOfList(dummy.next)     
    mysol = Solution()
    myhead = mysol.removeNthFromEnd2(dummy.next,2)
    printValueOfList(myhead)          