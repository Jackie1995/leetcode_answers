# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 21:05:25 2018

@author: jikang

leetcode300: 最长递增子序列的长度

题目描述
给出一个未排序的整数数组，找出最长递增子序列的长度。

样例
输入： [10,9,2,5,3,7,101,18]
输出：4
说明：最长递增子序列为[2,3,7,101]，长度为4，可能有多个可能的最长递增子序列，此题只需要返回长度即可。
"""

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        dp = [0]*len(nums)
        dp[0] = 1
        for i in range(1,len(nums)):
            tmp = [1]
            for j in range(i):
                if nums[i] > nums[j]:
                    tmp.append(dp[j]+1)
                else:
                    continue
            dp[i] = max(tmp)
        return max(dp)
    
class Solution2: #用二分查找好难啊
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        dp = [0]*len(nums)
        dp[0] = 1
        help_array = [nums[0]]
        for i in range(1,len(nums)):
            m = nums[i]
            # 然后对help数组进行二分查找。找到其中m可以放入的位置。
            l = 0
            r = len(help_array)
            while l < r:
                median = (l+r)//2
                if m <= help_array[median]:
                    if m>help_array[median-1]:
                        help_array[median] = m
                        break
                    else:
                        r = median -1
                else:
                    if m <= help_array[median+1]:
                        help_array[median+1] = m
                        break
                    else:
                        l = median+1
                
            
mynums = [10,9,2,5,3,7,101,18]
mysol = Solution()          
print(mysol.lengthOfLIS(mynums))