# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 23:20:07 2018

@author: jikang

leetcode236： 二叉树的最近公共祖先

题目描述
给定一课二叉树，找到其中指定两个点的最近公共祖先 (LCA)。

根据Wikipedia中LCA的定义 ：“最近公共祖先定义为两个结点 p 和 q 之间，树中最低的结点同时拥有 p 和 q 作为后代(这里允许一个结点的后代为它本身)。

注意
树中每个结点的权值都是唯一的。
p 和 q是两个不同的结点，且其值必定在二叉树中出现。
样例
Given the following binary search tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4


Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
解释: 结点 5 和 1 的最近公共祖先是 3。


Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: 结点 5 和 4 的最近公共祖先是 5, 因为根据后代结点的定义，一个结点的后代允许为它本身。

作者：wzc1995
链接：https://www.acwing.com/solution/leetcode/content/282/
来源：AcWing
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.path = []
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 这里注意一个点：p和q都是树节点的形式
        # 先找到从根节点到当前节点的路径
        self.find_path(root,p)
        path_p = self.path #这里是否需要深拷贝存疑
        self.path = []
        self.find_path(root,q)
        path_q = self.path
        # 下一步：比较path_p和path_q:从末尾开始比较
        i = 1
        while i <= min(len(path_p),len(path_q)):
            if path_p[-i] == path_q[-i]:
                i += 1
            else:
                break
        return path_p[-i+1]
        
        
    def find_path(self,root,des):
        if not root:
            return False
        if root == des: #这里：树节点之间可以直接比较
            self.path.append(root) #列表之中存放的也是树节点的引用。
            return True
        if self.find_path(root.left,des):
            self.path.append(root)
            return True
        if  self.find_path(root.right,des):
            self.path.append(root)
            return True
        return False
        