# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 22:36:00 2018

@author: jikang

leetcode90: 含有重复数的组合数、

题目描述
给定一个整数数组，可能包含重复元素。请返回它的所有子集（幂集）。

注意；答案中不能包含相同子集。

样例
输入：[1,2,2]
输出：
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""
## 做这道题生发的一点关于深度优先搜索算法的感想：
# 调用这层的dfs函数时和这层的dfs返回时的需要维持不变的变量，是状态变量。比如：self.parh是典型的状态变量。
# 那如何才能保证状态变量在调用前和调用返回时的值维持不变呢？其实就是忽略dfs中递归的语句，看一下其他语句是不是对self.path做了变化但是又原样还原？
# 只要每一层的函数，都能做到原样返回全局变量 self,path，那么就要可以保证这个状态变量的可用性。
import copy
class Solution:
    def __init__(self):
        self.path = []#注意这里要思考，path的处理逻辑是append还是按位置占坑？
        self.ans = []
    
    def dfs(self,nums,u):
        """
        nums: 排好序的，在整个递归过程中不会改变的整数数组
        u: 保存在当前活动的数字在整数数组nums中的位置。
        
        """
        if u == len(nums): #注意这里是len(nums)而不是len(nums)-1，原因是遍历结束之后，一定会跳出索引的最后一个位置。
            self.ans.append(copy.deepcopy(self.path))
            return None
        # 这里首先要判断：指针u指向的数组 nums[u]后面有几个重复数字。用局部变量k来存储位置u后面第一个不重复的数所在的位置,
        k= u+1
        while k < len(nums) and nums[k] == nums[u]:
                k +=1

        #上面的循环结束之后的k的值,就是下一个不等于nums[u]的数字在整数数组中的位置。
        #所以，这个数字append进去path的次数 从0次到(k-u)次都可以算作是在原先状态下的一种方案。
        #这里的处理方式：没有在进入下一层之前对path做什么改动。这一点不同以往。
        self.dfs(nums,k)
        #这样递归的话，很快就一路到最后一层边界了。
        #第一次到达边界有返回值的时候，path还不包括任何值。
        #到达边界后，函数没有返回值，只是将控制返回到上一层。
        #将控制返回到上一层的意思其实是：重新调整上一个枚举数字在答案中出现的次数。
        for i in range(k-u):
            self.path.append(nums[u])
            self.dfs(nums,k)
            
        for _ in range(k-u):
            self.path.pop()
        
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        self.dfs(nums,0) 
        return self.ans
        
if __name__=="__main__":
    mynums = [1,1,2]
    mysol = Solution()
    print(mysol.subsetsWithDup(mynums))                    
                    
    
        
        