# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 20:56:34 2018

@author: jikang

leetcode143: reorder list [交错链表]
题目描述
给定一个链表 L:L0→L1→…→Ln−1→Ln
将它变成 L0→Ln→L1→Ln−1→L2→Ln−2→…
你不能改变节点的值，只能改变节点的指针。
样例1（链表长度为偶数）
边界情况：1->2 变成 1-2
给定 1->2->3->4, 变成 1->4->2->3。
    观察链表长度为偶数的时候，只有4的指针做了反向操作。3的指针指向None.
继续推进:
    1->2->3->4->5->6 变成 1->6->2->5->3->4
    6,5的指针做了反向操作。4的指针指向None
当链表长度为n时：
    若n是偶数：（这个偶数指的是大于等于4的偶数）
    则：链表的后（n/2-1)个节点的指针反向，从尾部数，第（n/2）个节点位于末尾。并且指针指向None.
样例2（链表长度为奇数）
给定 1->2->3,变成 1->3->2
    3的指针做了反向操作，2的指针指向None
给定 1->2->3->4->5, 变成 1->5->2->4->3。
   5,4的指针做了反向操作，3的指针指向None
给定 1->2->3->4->5->6->7, 变成 1->7->2->6->3->5->4。
    7,6,5的指针做了反向操作，4的指针指向None.
当链表长度为n时：
    若n是奇数：（这个奇数指的是大于等于3的奇数）
    则，链表的后（n/2-1/2）从尾部数，第（n/2+1/2)个节点位于末尾，并且指针指向None.
无论是奇数还是偶数：
小于等于（n/2+1/2）的最大整数i,就是中间的位置
对应的循环条件应该写成： while i <= (n+1)/2
    
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
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        思路：
        边界情况1：链表长度为：0，1，2的链表，原链表不需要发生操作。
        第一次遍历：求出链表的长度（length）
        第二次遍历：找到中间节点的位置i,并反转中间位置之后的节点指针。
        第三次遍历：重新组织节点间的连接。使得节点交错。
        """
        #第一次遍历：
        length = 0
        p = head
        while(p):
            p = p.next
            length +=1
        # 处理边界情况1    
        if length in [0,1,2]:
            return    
        #****************  
        #第二次遍历：               
        p = head
        pos = 1
        while(pos < (length+1)/2): #这个循环条件正确，下面的循环条件错误。
        #while(pos <= (length-1)/2):这个循环条件怎么写是个难点：到底有没有等于号？
            p = p.next
            pos +=1
        # 当循环停止的时候，指针p已经到达了中间节点的位置。
        # 下面的节点就要进行指针的反转了。
        second = p
        first = second.next #可以证明：first始终合法。
        second.next = None #这个语句合理吗？
        while(first):
            tmp = first
            first = first.next
            tmp.next = second
            second = tmp
        # 循环结束后，second指针达到链表的尾节点。
        # 第三次遍历：
        head_p = head
        tail_p = second
        while(tail_p.next): #这里只需要判断 tail_p.next 这个就好，不需要再重复判断 head_p，next
            head_tmp = head_p
            head_p = head_p.next #条件：head_p
            head_tmp.next = tail_p
            
            tail_tmp = tail_p
            tail_p = tail_p.next #条件：tail_p
            tail_tmp.next = head_p
        return 
        #return head 仔细阅读leetcode上面的要求，它不需要有返回值。所以不需要return。
            
if __name__ == "__main__":
    mydummy = getDummyNode([1,2,3,4])
    printValueOfList(mydummy.next)
    mysol = Solution()
    myhead = mysol.reorderList(mydummy.next)
    printValueOfList(myhead)
