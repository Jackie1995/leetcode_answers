# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 22:37:51 2018

@author: jikang

leetcode 331: Verify Preorder Serialization of a Binary Tree 

题目描述
一种把二叉树序列化的方式是使用前序遍历。当我们遇到非空节点时，直接记录它的值；当我们遇到空节点时，记录#。

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
例如，上述二叉树可以被序列化成"9,3,4,#,#,1,#,#,2,#,6,#,#"，#表示空节点。

给定一个用逗号隔开的序列，请判断它是不是一个合法的二叉树前序遍历。请不要将二叉树重建出来。

被逗号隔开的值要么是整数，要么是#。

给定的序列一定是合法的。例如，不会出现两个连续逗号的情况：1,,3。

样例1
输入："9,3,4,#,#,1,#,#,2,#,6,#,#"
输出：true
样例2
输入："1,#"
输出：false
样例3
输入："9,#,#,1"
输出：false

"""
# 整体思路类似于栈：全部弹出之后，是不是树的遍历已经全部完成？
class Solution:
    def __init__(self):
        self.ans = True
        self.u = 0
    
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # 这里先将preorder序列后面加一个逗号
        preorder += ',' #思考：这后面为什么要多加上一个逗号呢？
        self.dfs(preorder)
        if self.ans and self.u == len(preorder): #只有这两个条件全部满足才是一个正确的序列。
            return True
        return False
        
        
    def dfs(self,preorder):
        # preorder:前序遍历的序列
        # u: 指向preorder中各项的指针。
        # 思路：由前序数列生成二叉树，如果发现生不成二叉树，就返回False
        if self.u == len(preorder): #出现这种情况说明：u指针已经遍历超过了前序数组的范围。
            self.ans = False #如果有这种情况发生，就把这个序列否定了，这个序列不可能生成树。
            return #返回控制给被调函数
        if preorder[self.u] == '#': #如果当前u指向的位置是‘#’，那么就把指针移动到下一个整数或者‘#’
            self.u += 2 #思考这里的u是全局变量（整个类内的所有函数都看得到）吗？
            return #返回控制给被调函数
        # 如果函数可以执行到这一步：说明当前指针u指向的数字，只可能是整数或者‘,’
        while preorder[self.u] != ',': #如果u指向的数字是整数，就进入这个循环
            self.u +=1 #如果u是整数，就让指针再往下走一个，此时的u指向的一定是‘,’
        self.u += 1  #这个时候让指针从','再往下面走一个，就走到了有效符号 整数or‘#’处。
        self.dfs(preorder)
        # 等到这个调用返回的时候，说明之前输入的u的左子树已经遍历完成了，u也已经往后移动了很多。
        # 这时候再次进行判断：
        if self.u == len(preorder): 
            self.ans = False
        # 如果这个时候，u指针还是没有遍历到前序数列末尾的话
        self.dfs(preorder) #就要再遍历右子树
        
            
        
        
