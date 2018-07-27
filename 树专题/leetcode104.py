# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 00:01:16 2018

@author: jikang

求出树的最大深度
题目描述
给定一课二叉树，求它的最大深度。
最大深度是指从根节点到叶节点的路径长度的最大值。

样例
给定一课二叉树 [3,9,20,null,null,15,7]：

    3
   / \
  9  20
    /  \
   15   7
它的深度是3。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
    
    
    
    