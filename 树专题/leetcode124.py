# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 23:04:44 2018

@author: jikang

leetcode124: 二叉树最大路径权值和

题目描述
给定一个非空二叉树，找到路径权值和的最大值。
在这道题目中，路径是指从树中某个节点开始，沿着树中的边走，走到某个节点为止，路过的所有节点的集合。
路径的权值和是指路径中所有节点的权值的总和。

样例1
输入：[1,2,3]

       1
      / \
     2   3

输出：6
样例2
输入：[-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出：42
"""

#思路 遍历树中的每一个节点为割点 
#递推思路：以root节点为割点的路径最大权值之和 = root.val + 以root.left为顶点的路径最大权值之和 + 以root.right为顶点的路径最大权值之和
#递推函数：参数（树节点root）函数求的是这个以节点root为顶点的路径最大权值之和，函数返回值是int类型
#递推函数的每一步更新维护：全局的路径最大权值之和（每一步地推可以计算当前节点为割点的值）

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = 0
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = root.val
        self.dfs(root)
        return self.ans
        
    def dfs(self,root):
        if not root:
            return 0
        left_sum = max(self.dfs(root.left),0) #这里的max函数！重要！理由：如果比0小，那就不如不加。
        right_sum = max(self.dfs(root.right),0) 
        self.ans = max(self.ans,left_sum+right_sum+root.val)
        return max(left_sum,right_sum)+root.val
