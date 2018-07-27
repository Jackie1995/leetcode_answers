# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 00:15:07 2018

@author: jikang

题目描述
给定一个无重复数字的集合，和一个目标值。返回所有不同的数字组合，使得每组数字的和等于目标值。
同一个数字可以使用无穷多次。
所有数组都是正整数，结果不得含有重复的组合，组合中数字的顺序无关。

样例
Input: candidates = [2,3,6,7], target = 7,
Output:
[
  [7],
  [2,2,3]
]

Input: candidates = [2,3,5], target = 8,
Output:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
import copy
class Solution:

    
    def __init__(self):
        self.ans = []
        self.path = []
        
    def dfs(self, candidates,sum_val,target,ch):
        """
        candidates:就是一直都不变化的整形数组。
        target:一直不变的目标和值。
        sum_val:是一个状态变量，需要将最后一层的这个值与目标值比较。不懂这个状态变量为什么要入参呢？作为类的数据成员不行吗？
        ch：记录枚举的数字的个数（即 dfs调用的层数）
        """
        if sum_val == target:
            self.ans.append(copy.deepcopy(self.path))
            return
        if ch >= len(candidates):
            return
        if sum_val + candidates[ch] > target:
        # 这个判断条件判断的是：当前的数字加一个进去，就会超过目标值，所以该条path不符合条件，不加入到ans中，只是将控制返回上个状态（上一个层）
            return
        # 既然当前的数字加一次到sum_val中不会超标（即超过目标值），那么加几次就超标了呢？需要计算一下。
        max_i = (target - sum_val)//candidates[ch] #除法向下取值的运算符：//
        new_sum = sum_val
        self.dfs(candidates,new_sum,target,ch+1)
        for i in range(1,max_i+1):
            new_sum += candidates[ch] 
            self.path.append(candidates[ch])
            self.dfs(candidates,new_sum,target,ch+1)
        for i in range(1,max_i+1):
            self.path.pop()
            
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 先对这个不含有重复数的整数数组进行排序。以方便后续剪枝。
        candidates.sort()
        self.dfs(candidates,0,target,0)
        return self.ans
    
if __name__=="__main__":
    mycandidates = [2,3,5]
    mytarget = 8
    mysol = Solution()
    print(mysol.combinationSum(mycandidates,mytarget))          
        