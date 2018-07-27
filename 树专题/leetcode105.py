# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 22:05:22 2018

@author: jikang

leetcode 105 : 根据数的前序遍历和中序遍历的顺序重构二叉树。

题目描述
给定一棵二叉树的前序遍历和中序遍历，请复原出整棵二叉树。

注意：二叉树中没有值相同的节点。

样例
给定：

前序遍历是：[3,9,20,15,7]
中序遍历时：[9,3,15,20,7]
返回的二叉树如下所示：

    3
   / \
  9  20
    /  \
   15   7

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 首先统计这棵树一共有多少节点。一共有n个节点。
        n = len(preorder)
        # 然后把中序遍历序列的【值和位置】的对应关系放到一个字典中：
        pos = {}
        for i in range(n):
            pos[inorder[i]] = i
        return self.dfs(preorder,inorder,pos,0,n-1,0,n-1) #注意：pos这个值，必须作为一个入参进入到递归过程，否则后面的函数看不到它。
    
            
    def dfs(self,prelist,inlist,pos,pl,pr,il,ir):
        if pl > pr: #这种情况说明，接下里遍历的部分已经不是有效的子树了，就是一个空的概念。
            return None
        # 这个时候的根节点就是以prelist[pl]作为val的节点。
        root = TreeNode(prelist[pl])
        # 求出此时的root的左子树包含的节点个数：k
        k = pos[prelist[pl]]-il #这里有个问题：pos这个字典变量的作用范围是怎样的？
        root.left = self.dfs(prelist,inlist,pos,pl+1,pl+k,il,il+k-1)
        root.right = self.dfs(prelist,inlist,pos,pl+k+1,pr,il+k+1,ir)
        return root