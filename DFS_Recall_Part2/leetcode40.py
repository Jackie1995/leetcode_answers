# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 00:10:22 2018

@author: jikang

leetcode 40 组合方案数2 每个数字只可以用一次

题目描述
给定一个数字的集合，和一个目标值。返回所有不同的数字组合，使得每组数字的和等于目标值。
同一个数字最多可以使用一次。
所有数组都是正整数，结果不得含有重复的组合，组合中数字的顺序无关。
样例
Input: candidates = [10,1,2,7,6,1,5], target = 8,
Output:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Input: candidates = [2,5,2,1,2], target = 5,
Output:
[
  [1,2,2],
  [5]
]
"""
import copy
class Solution:
    def __init__(self):
        self.path = []
        self.ans = []
        # 不需要st这种与candidates等长的数组吧？
    def dfs(self,candidates,target,ch,sum_val):
        """
        ch:记录candicates中的数字的位置。边界条件的判断之一。
        sum_val：每一步的状态变量，显示这一步没有选值时（即这一层之前）的数字和。
        没有返回值。
        """
        if sum_val == target:
            self.ans.append(copy.deepcopy(self.path))
            return
        if ch == len(candidates):#说明此时指针已经走出了整型数组的范围。
            return
        if sum_val + candidates[ch] > target:
            return
        for i in [0,1]:
            if i == 0: # 意思是这个位置（当前层）的数字不选。
                # 这个时候指针就不是向下都直接指向下一层（ch+1）了，要看一下到什么位置，才会走到一个新的数字？
                # 新开辟一个变量 next_ch 来保存下一步应该指向的位置。
                next_ch = ch+1
                while next_ch < len(candidates) and candidates[next_ch] == candidates[ch]:
                # 这里要注意：两个条件用且来连接的。这种模式还挺常用的。不要再用 while + 内层if判断来写了。
                    next_ch +=1
                # self.path 不发生任何改变
                self.dfs(candidates,target,next_ch,sum_val)
            if i == 1:
                self.path.append(candidates[ch])
                self.dfs(candidates,target,ch+1,sum_val+candidates[ch])
                self.path.pop()
        
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort() #先从小到达排下序,这道题依然需要排序，目的是防止重复。这是本题需要重点体会的地方。
        self.dfs(candidates,target,0,0)
        return self.ans
    
if __name__ == "__main__":
    # mycandidates = [10,1,2,7,6,1,5]
    mycandidates = [2,2,2]
    # mytarget = 8
    mytarget = 2
    mysol = Solution()
    print(mysol.combinationSum2(mycandidates,mytarget))
    