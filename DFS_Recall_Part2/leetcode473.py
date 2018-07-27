# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 22:44:32 2018

@author: jikang

leetcode 473 

题目描述
给定一些整数，代表火柴棍的长度。求这些火柴棍是否可以组成一个正方形。火柴棍不可以拆分，但是可以拼接。

样例
Input: [1,1,2,2,2]
Output: true

"""
# 注意这道题用python来写很容易TLE。
# 修正这个bug，主要修改的是：if side_length != side and side_length+nums[-1]>side:就是这里！

class Solution:
    def __init__(self):
        self.subsum = [] #这个状态变量是放置当前方案下 正方形4条边的长度。

        
    def dfs(self,side,nums,ch):
        """
        参数说明：
        side：如果正方形存在的话，正方形的边长。在递归全程不变。
        nums：用来枚举（遍历的）火柴棒长度序列。在递归全程不变。
        ch：火柴棒序列的指针。即指示遍历的深度。
        """
        # 边界条件：四条边当中，如果有一条边的长度超过合法边长side，这个方案就不是一个正确答案。
        for side_length in self.subsum:
            if side_length != side and side_length+nums[-1]>side: #注意这个条件的精妙之处！有效剪枝，提前看到结果无望，避免做无用的递归。
                #break 傻孩子 这里的break是多余的啊，执行了break就没有办法再return了呀
                return 
        # 如果通过了第一个边界条件，说明目前方案中的边长都是小于等于合法边长的。
        flag = 0
        for side_length in self.subsum:
            if side_length == side:
                flag += 1
        if flag >=3 :
            return True
        # 第三个条件：
        # if ch == len(nums):
        #    return True#感觉这里如果仅仅是返回上一个状态的话，还是会继续遍历其他的方案，造成不必要的计算。
        for i in range(4): #将每个数字放在不同的边上。
            self.subsum[i] += nums[ch]
            if self.dfs(side,nums,ch+1):
                return True #注意这里回溯的时候，都往调用它的上一层函数传递一个是否已经很找到答案的状态，如果已经找到答案，就可以不需要遍历其他方案，直接递归返回返回值到最外层即可。
            self.subsum[i] -= nums[ch]
        return False  
     
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 第一步：先判断火柴棒的数目是不是小于4根？
        if len(nums) <4:
            return False
        # 第二步：先判断所有火柴棒的长度之和是不是可以被4整除。如果不可以的话。就返回False：
        if sum(nums)%4 != 0:
            return False
        # 如果可以整除的话，再进行接下来的操作：
        nums.sort(reverse = True)
        side = sum(nums)/4 #求出边长。
        self.subsum = [0]*4
        return self.dfs(side,nums,0)
    
if __name__ == "__main__":
    mynums = [3,3,3,3,4]
    mysol = Solution()
    print(mysol.makesquare(mynums))