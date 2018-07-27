# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 23:27:24 2018

@author: jikang

leetcode47:带有重复数的组合问题
题目描述
给定一堆整数，可能包含相同数，返回其所有不同的全排列。

样例
输入：

[1,1,2]
输出：

[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
import copy
class Solution:
    def __init__(self):
        self.ans = []
        self.st = []
        self.path = []
    
    def dfs(self,nums,u,start):
        """
        :type nums: List[int]
        :type u: int
        :type start: int
        :rtype: void
        """
        if u == len(nums)-1:# 最后一层几点（边界条件）：path临时答案ready了。可以append进ans中了。
            self.ans.append(copy.deepcopy(self.path)) #这是是不是也还是要 deepcopy()path一下？
            return
        
        for i in range(start,len(self.path)):# i这里遍历的是位置
            if not self.st[i]: #如果该位置没有被占用的话
                self.path[i] = nums[u]
                self.st[i] = True
                # 注意：下面在递归的时候有个条件选择：
#                if u+1==len(nums):
#                    self.dfs(nums,u+1,0)
#                    break
                if nums[u+1]!=nums[u]:
                    self.dfs(nums,u+1,0)
                else:
                    self.dfs(nums,u+1,i+1)
                #回溯后记得要还原位置状态。
                self.st[i] = False
                
        
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() #调用python中list数据类型的sort方法来排序。
        nums.append(0) #这里为了防止数组越界，我在后面append了一个数。
        self.path = [0]*(len(nums)-1) #因为之后要用到path的位置，所以path数组的元素个数要提前准备好。
        self.st = [False]*(len(nums)-1)#和nums数组同样长度的状态变量，一开始全部初始化为false：即所有的位置都未被使用。
        self.dfs(nums,0,0)
        return self.ans
    
if __name__ == "__main__":
    mynums = [1,1,2]
    mysol = Solution()
    print(mysol.permuteUnique(mynums))    
    