# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 21:08:09 2018

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

# leetcode上面的题干如下面所示：

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        思路：
        一次遍历：指针从头节点处遍历
        循环条件：指针到达链表末尾。
            每次判断指针处的值和下一节点的值是否相同？
            如果相同：删除下一个节点。
            如果不同：指针移动的下一个节点。
         边界情况1：只有一个头节点---通过   
         边界情况2（会存在吗？会的）：头节点并不是节点类，而是为空。直接返回原来的空节点。
        """
        p = head
        if not p:
            return head
        while(p.next):
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
                
            
        
if __name__ == "__main__":
    mydummy = getDummyNode([1,1,2,3,3])
    printValueOfList(mydummy.next)
    mysol = Solution()
    myhead = mysol.deleteDuplicates(mydummy.next)
    printValueOfList(myhead)
    