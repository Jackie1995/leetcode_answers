# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 21:46:53 2018

@author: jikang

leetcode 145 :返回二叉树后序遍历的结果
Binary Tree Postorder Traversa

题目描述
给定一个二叉树，返回后序遍历的结果。

样例
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]

总感觉树的问题，python和c++的写法差距很大。
"""

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.postpath = []
        
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.dfs(root)
        return self.postpath
    
    def dfs(self,root):
        if not root:
            return 
        left_node = self.dfs(root.left)
        if left_node:
            self.postpath.append(left_node.val)
        right_node = self.dfs(root.right)
        if right_node:
            self.postpath.append(right_node.val)
        self.postpath.append(root.val)
        
