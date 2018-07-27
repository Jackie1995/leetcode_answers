# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 23:24:00 2018

@author: jikang

leetcode 102  Binary Tree Level Order Traversal 

题目描述
给定一棵二叉树，返回它的层序遍历。（即从上到下，从左到右，一层一层地遍历）

样例
给定二叉树 [3,9,20,null,null,15,7]：

    3
   / \
  9  20
    /  \
   15   7
它的层序遍历结果是：

[
  [3],
  [9,20],
  [15,7]
]
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.level_ans = []
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = [root]
        self.bfs(level)
        return self.level_ans
    
    def bfs(self,level):
        """
        :level: List[TreeNode]
        rtype: None
        """
        if not level:
            return
        new_level = []
        level_containder = []
        for treenode in level:
            # 之前要保证level当中都是TreeNode,没有None值。
            # 先在层序遍历的答案里面append进去这个节点的值。
            level_containder.append(treenode.val)
            if treenode.left: #如果左节点不为空的话：
                new_level.append(treenode.left)
            if treenode.right:
                new_level.append(treenode.right)
        self.level_ans.append(level_containder)
        # 原来的level遍历结束后，所有的节点值都append到level_ans中，同时产生了新的new_level
        self.bfs(new_level)