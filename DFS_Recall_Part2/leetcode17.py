# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 08:20:41 2018

@author: jikang

leetcode17:乘法原理

题目描述
给定一个数字串，返回由该数字串能代表的所有字母组合。
每个数字能代表一些字母，和九宫格键盘上一样。
样例
给定数字串 "23" ，
返回所有字母组合 ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

"""

class Solution:
    def __init__(self):
        # 初始化两个全局变量。
        self.res = []
        self.digit = {2:['a','b','c'],
                      3:['d','e','f'],
                      4:['g','h','i'],
                      5:['j','k','l'],
                      6:['m','n','o'],
                      7:['p','q','r','s'],
                      8:['t','u','v'],
                      9:['w','x','y','z']}
    def dfs(self,digits,d,cur):
        """
        :type digits: str
        :type d: int
        :type cur :str
        :rtype: void
        """
        if d == len(digits):#先判断是不是已经遍历到数字串的结尾。（达到最深的深度）
            # 如果已经到达字符串的末尾，就说明可以得到一个答案了，
            self.res.append(cur) #在全局变量res后面append上自己的答案。
            return #然后将控制返回调用自己的子例程。
        #如果还没有到达字符串的结尾,就找到该层的光标数字：cur_num
        cur_num = int(digits[d])
        #遍历光标数字可以代表的全部字母：
        for char in self.digit[cur_num]:
            #char就是当前选择的字母。
            #选择了一个字母之后，自然要将d = d+1,cur = cur+char，然后开始下一步的搜索，直到有答案了。
            self.dfs(digits,d+1,cur+char)
            
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return self.res
        self.dfs(digits,0,"")
        return self.res

if __name__ == "__main__":
    mydigits = '23'
    mysol = Solution()
    print(mysol.letterCombinations(mydigits))

