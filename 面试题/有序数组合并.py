# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 00:01:40 2018

@author: jikang
"""
# 时间复杂度分析： m+n

class Solution:
    def merge_two_sorted_array(self,lyst1,lyst2):
        ans = []
        i1 = 0
        i2 = 0
        while i1 < len(lyst1) and i2 <len(lyst2):
            if lyst1[i1] <= lyst2[i2]:
                ans.append(lyst1[i1])
                i1 += 1
            else:
                ans.append(lyst1[i1])
                i2 += 1
        if i1 == len(lyst1):
            ans.extend(lyst2[i2:])
        else:
            ans.extend(lyst2[i1:])
        return ans
    
mylyst1 = list(range(10)) 
mylyst2 = list(range(1,22,2))
mysol = Solution()
print(mysol.merge_two_sorted_array(mylyst1,mylyst2))