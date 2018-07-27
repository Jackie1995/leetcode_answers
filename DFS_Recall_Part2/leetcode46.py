# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 22:14:54 2018

@author: jikang

permutations: 全排列

题目描述
给出一列互不相同的整数，返回其全排列。

样例
输入：

[1,2,3]
输出：
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
"""
笔记：递归过程中：一定要注意变量的作用域。
"""
import copy #加载copy模块
class Solution:
    def __init__(self):
        self.ans = []
        self.st = []
        self.path = []


    def dfs(self,nums,u):
        """
        :type nums: List[int]
        :type u: int
        :rtype: void
        """
        # 边界的判断：最后一层节点：将此时的path（其中一个答案），append到ans当中。
        if u==len(nums):
            self.ans.append(copy.deepcopy(self.path)) #正确的
            #self.ans.append(self.path) #错误的。错误原因详见acwing问答。
            return 
        #**********************
        for i in range(len(nums)):
            if not self.st[i]:# 遍历原始整数数组，只选择标记为“未被使用的”数字
                self.st[i] = True #注意：path和st[i]是联动的，是否被使用 等价于 是否包含在path中。
                self.path.append(nums[i]) #将选择的这个数字append进入path中。
                self.dfs(nums,u+1)
                self.st[i] =  False#当递归返回时，要将上一步设置为“已使用状态”的数字，再重新设置为“未被使用的状态”。
                self.path.pop() #当然，st一旦发生变化，临时答案path也要发生变化。

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """    
        self.st = [False]*len(nums)
        self.dfs(nums,0)
        return self.ans
    
if __name__ == "__main__":
    mynums = [1,2,3]
    mysol = Solution()
    print(mysol.permute(mynums))