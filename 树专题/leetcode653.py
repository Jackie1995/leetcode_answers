# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 23:06:55 2018

@author: jikang

leetcode 653
题目描述
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
给定一个二叉搜索树和一个目标数，检查二叉搜索树中是否存在两个元素使其和等于给定的目标数。

样例
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

"""
# 因为题目给的是一个BST（二叉搜索树），所以可以通过中序遍历的方式，生成一个排序的数组。
# 然后再通过排序的数组，来做选择。
class Solution:
    def __init__(self):
        self.node_val_list = []
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        sorted_array = self.inorder(root)
        left = 0
        right = len(sorted_array)-1
        while left < right:
            if sorted_array[left] + sorted_array[right] == k:
                return True
            elif sorted_array[left] + sorted_array[right] < k:
                left += 1
            else:
                right -= 1
        return False
    
    def inorder(self,root):
        """
        root: TreeNode
        rtype: List[int](全局变量)
        """
        if not root:
            return
        self.inorder(root.left)
        self.node_val_list.append(root.val)
        self.inorder(root.right)
        return self.node_val_list
