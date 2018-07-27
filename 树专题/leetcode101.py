# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 21:30:30 2018

@author: jikang

leetcode 101

题目描述
给定一个二叉树，判断它是否是自己的“镜像”（是否以中心竖线为轴左右对称）。

注意:如果同时给出递归和迭代方法，会获得加分。

样例1
如下二叉树 [1,2,2,3,4,4,3] 是自己的“镜像”：

    1
   / \
  2   2
 / \ / \
3  4 4  3
"""
import copy
from math import log
 # Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.dfs(root.left,root.right)

    def dfs(self,left_node,right_node):
        # 如果；left_node 和 right_node 中有至少一个节点为空。就不应该进入下面的判断
        if not left_node or not right_node:
            return not left_node and not right_node #都是空，树才是对称的；否则树不是对称的。
        
        if left_node.val != right_node.val:
            return False
        if self.dfs(left_node.left,right_node.right) and self.dfs(left_node.right,right_node.left):
        #如果当前的左右节点都是合法的树节点，就要分别判断左节点的左子树与右节点的右子树是否一致。左节点的右子树和右节点的左子树是否一致。
            return True
        return False
    
def create_btree(lyst):
    # 从层序遍历的结果重构一棵二叉树 这个目前写不出来。
    #lyst_copy = copy.deepcopy(lyst) #深拷贝前后，两个数组不会因为对方的改变而改变。
    # 一开始是第0层；共包含2**0个节点。
    n  = len(lyst)
    if n==1:
        return lyst[0]
    max_level = int(log(n+1,2))-1
    level = 0
    pointer = 2**level-1
    active_level = []
    for node_pointer in range(pointer,pointer+2**level):
        active_level.append(TreeNode(lyst[node_pointer]))
    next_level = []
    for node_pointer in range(pointer,pointer+2**(level+1)):
        next_level.append(TreeNode(lyst[node_pointer]))
    #然后把层序遍历下一层的值，都关联到上一层的节点上面。
    for i in range(2**(level)):
        active_level[i].left = next_level[2*i]
        active_level[i].right = next_level[2*i+1]
        
    while level < max_level:
        active_level = next_level
        level += 1
        pointer =  2**(level+1)-1
        next_level = []
        for node_pointer in range(pointer,pointer+2**(level+1)):
            next_level.append(TreeNode(lyst[node_pointer]))    
        for i in range(2**(level)):
            active_level[i].left = next_level[2*i]
            active_level[i].right = next_level[2*i+1]        