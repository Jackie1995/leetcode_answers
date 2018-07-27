# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 11:14:14 2018

@author: jikang

leetcode 216：组合方案数3：方案中不包含相同数。

题目描述
给定数字1到9，从中选 k 个数，不考虑顺序，使得它们的和等于 n，
返回所有方案。要求方案中不包含相同数字，且答案中不包含相同的方案。

样例1
输入：k = 3, n = 7
输出：[[1,2,4]]
样例2
输入：k = 3, n = 9
输出：[[1,2,6], [1,3,5], [2,3,4]]
"""
import copy
class Solution:
    def __init__(self):
        self.path = []
        self.ans = []
        
    def dfs(self,remain_k,n,ch):
        """
        remain_k: 递归到每一层的时候，剩余的数字个数。
        # 不需要这个参数了。因为没有必要在中间的每一步都维护一个这样的状态量】acumn_sum: 递归到每一层的时候，已经累计的和的数目。
        n:常数值，外层combinationSum3（）函数传入，在递归过程中不变化。
        ch：递归的层数；1-9中的9个数递归到哪一个了。
        """
        # 终止递归的基本条件1：path中已经存在k个数字了。
        if remain_k == 0:
            # 这时候再判断，这k个选出来的数字之和是不是=n
            if sum(self.path) == n: #如果数字之和等于target，才把这样的path添加到最终答案里。
                self.ans.append(copy.deepcopy(self.path))
            return
        # 因为remain_k是递减的，当减小到0的时候就返回，所以remain_k不可能小于0。
        # 终止递归的基本条件2：已经遍历完了9个数字，但是选择出来的数字个数不足k个，这些方案都是不ok的。
        if ch == 10:
            return
        for i in [0,1]: #对于当前数有：选择或者不选择，两个方案
            if i==0: #表示不选择当前数
                self.dfs(remain_k,n,ch+1)
            if i==1: #表示选择当前数
                self.path.append(ch)
                self.dfs(remain_k-1,n,ch+1)
                self.path.pop()
            
        #对于每一层的数字来说：
        
    def combinationSum3(self, k, n):
        """
        :type k: int 从9个数中选k个。
        :type n: int target_sum = n
        :rtype: List[List[int]]
        """
        # 思考k=0的时候，也就是说只准使用0个数字，会不会是边界情况？
        self.dfs(remain_k=k,n=n,ch=1)
        return self.ans

if __name__ == "__main__":
    myk = 3
    myn = 9
    mysol = Solution()
    print(mysol.combinationSum3(myk,myn))