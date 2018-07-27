# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 21:50:32 2018

@author: jikang

leetcode 22: 括号序列问题。

题目描述
给定括号对数nn，生成出所有合法的括号序列。

样例

输入：n = 3
输出：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

算法思路：
生成合法的括号序列的思路是：
一个位置是否是否可以防止左括号的判断标准是：左括号的数目不超过n个。
一个位置是否是否可以防止右括号的判断标准是：右括号的数目不超过左括号的数目个。
"""

class Solution:
    def __init__(self):
        self.path = [] #使用的是cur指针来确定cur中的位置。
        self.ans = []
        
    def dfs(self,n,l,r,cur):
        """
        参数解释： n：可以用来组合的括号的对数。由顶层函数传入，递归过程不会改变。
        l：这一步之前，一共用过的左括号的数目。
        r：这一步之前，一共用过的右括号的数目。
        cur：path中当前活跃的位置指针。我们在当前这个层需要判断，这个位置是否可以放左括号？
            是否可以放右括号？有最多两种方案可以来选择。
        """
        #先写边界条件：当path填满最后一个位置的时候，就将path（我们枚举出来的path一定都是合法的），append到ans的后面。
        if cur == 2*n:
            result_path = ''.join(self.path)
            self.ans.append(result_path)
            return
        #当前位置的选择有 放置左括号和放置右括号这两种选择：
        for choice in ['left','right']:
            if choice == 'left' and l < n:#当选择要放左括时候，还判断左括号是不是还有未使用的名额。
                self.path[cur] = '('
                self.dfs(n,l+1,r,cur+1)
            if choice == "right" and r < l:                
                self.path[cur] = ')'
                self.dfs(n,l,r+1,cur+1)
                    
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.path = [0]*2*n
        self.dfs(n,0,0,0)
        return self.ans

if __name__ == '__main__':
    myn = 3
    mysol = Solution()
    print(mysol.generateParenthesis(myn))