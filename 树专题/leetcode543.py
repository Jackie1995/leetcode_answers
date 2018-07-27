# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 22:36:44 2018

@author: jikang

leetcode 543 求二叉树的最大直径。
题目描述
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径穿过或者不穿过根结点。

样例
给定二叉树

          1
         / \
        2   3
       / \     
      4   5    

返回 3, 它是路径 [4,2,1,3] 或者 [5,2,1,3] 的长度。
"""
#因为这种求最大直径的问题的路径起点不一定是根节点，所以要遍历求出以树中的每一个节点为割点（注意割点的定义）的最大路径。
#确定了割点，求割点的最长路径 = 割点左侧最长路径 + 割点右侧最长路径
#                        = 割点左孩子为顶点的最长路径 + 割点右孩子为顶点的最长路径 + 2
#所以：递推关系明确了：以父节点为顶点的最长路径 = 以其左子节点为顶点的最长路径 + 以其右子节点为顶点的最长路径 +2
#中途还需要维护以当前节点为割点的最长路径
#递推函数的参数：割点 返回值：最长路径的长度

class Solution:
    def __init__(self):
        self.max_path = 0
        
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.max_path
        
        
    def dfs(self,root):
        #边界条件：如果是遍历到空节点的话，返回的最长路径长度是-1，因为叶子节点作为顶点的最长路径长度是0嘛
        if not root:
            return -1
        left_path = self.dfs(root.left)+1
        right_path = self.dfs(root.right)+1
        self.max_path = max(self.max_path,left_path + right_path)
        return max(left_path,right_path)
        
        
        
        