# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 00:28:27 2018

@author: jikang

leetcode78: 组合数
题目描述
给定一个集合，包含互不相同的数，返回它的所有子集（幂集）。

注意；结果不能包含相同子集。

样例
输入：nums = [1,2,3]
输出：
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res_f = list(range(2**n))
        res = []
        for int_val in res_f:
            tmp = []
            bin_val = bin(int_val)[2:]
            m = len(bin_val)-1
            for index, bit_val in enumerate(bin_val):
                if bit_val == '1':
                    tmp.append(nums[m-index])
            res.append(tmp)                    
        return res
if __name__=="__main__":
    mynums = [1,2,3]
    mysol = Solution()
    print(mysol.subsets(mynums))                    
            

