# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 20:53:55 2018

@author: jikang

leetcode53: 最大子序列和

题目描述
给定一个整数数组nums，找到和最大的连续子序列（至少包含一个数字），返回该子序列的和。
样例
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
"""

class Solution:

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 声明状态向量
        f = [0]*len(nums)
        # 初始化状态向量
        f[0] = nums[0]
        # 一步步进行状态转移
        for i in range(1,len(nums)):
            f[i] = max(f[i-1]+nums[i],nums[i])
        return  max(f)  

mynums = [-2,1,-3,4,-1,2,1,-5,4]
mysol = Solution()          
print(mysol.maxSubArray(mynums))