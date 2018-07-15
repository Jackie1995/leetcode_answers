# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 23:32:30 2018

@author: jikang

leetcode92： 链表反转

题目描述
请将链表中第 nn 个节点和第 mm 个节点之间的部分翻转。
链表最多只能遍历一遍。
注意：1 ≤ m ≤ n ≤ 链表长度。
样例
输入：1->2->3->4->5->NULL, m = 2, n = 4
输出：1->4->3->2->5->NULL
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

# =============================================================================
# 答案如下：
# =============================================================================

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        思路：
        1。 隔离。对隔离点做好标记。
        2。 对中间的需要反转的部分，按照普通的链表反转进行反转。
        3. 小心设置一下隔离点前后的指针连接。
        指针的定义：
        1. 指向第(m-1)个节点的指针 start（反转部分之前的那个节点）
        2. 指向第（n+1）个节点的指针 end（反转部分之后的那个节点）
        3. 指向第m个节点的指针 head_part (反转部分的头节点)
        4. 指向第n个节点的指针 tail_part (反转部分的尾指针)
    
        边界情况1：m==n反转的部分只包含一个节点.(已处理)
        边界情况2：（可以兼容）反转的部分从head开始？并且反转部分包含的节点数>=2个；
                这意味着：头节点将发生改变！！(设立虚拟保护节点，可以有效兼容情况2)
        边界情况3：（可以兼容） 反转的部分包含尾节点？ 程序可以兼容。               
        一般情况：
        """
        # 处理边界情况1：反转部分的长度==1
        if m == n:
            return head
        #***************
        # 一般情况：反转部分的长度>1
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        pos = 0
        while pos < m-1:
            cur = cur.next
            pos += 1
        # 循环结束后，光标指针cur到了第m-1个节点的位置。用start指针保存下这个节点的位置。
        start = cur
        # 光标指针继续向下移动一个节点，就到达了反转部分的头节点。
        cur = cur.next
        pos += 1
        head_part = cur
        # 以反转部分的头节点作为普通的头节点，开始迭代修改每个节点的next指针方向。
        cur = cur.next
        pos += 1
        origin = head_part
        head_part.next = None
        while pos <= n:
            tmp = cur
            cur = cur.next
            pos += 1
            tmp.next = origin
            origin = tmp
        # 迭代结束后，cur指针指向的节点就是：end指针指向的节点；
        #           origin指针之乡的皆否就是：tail_part指针指向的节点
        # 考虑边界情况：如果n==length的话，cur = None; origin = tail.可以兼容。
        end = cur
        tail_part = origin
        # 重现设置隔离点附近的指针情况
        start.next = tail_part
        head_part.next = end
        return dummy.next

if __name__ == "__main__":
    mydummy = getDummyNode([1,2,3,4,5])
    printValueOfList(mydummy.next)
    mysol = Solution()
    myhead = mysol.reverseBetween(mydummy.next,m=2,n=4)
    printValueOfList(myhead)            
        
        
        

