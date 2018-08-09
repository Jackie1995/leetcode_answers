# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 00:01:18 2018

@author: jikang

股票问题2

题目描述
假设你有一个数组，其中第i个元素表示第i天某个股票的价格。

设计一种算法以找到最大利润，可以完成任意多次交易，但必须先购买股票再出售股票，不能同时多次交易。

样例
Example 1:

输入: [7,1,5,3,6,4]
输出: 7
解释: 第二天买(price = 1)，第三天卖(price=5)，利润为4;
第四天买(price = 3)，第五天卖(price=6)，利润为3。

Example 2:

输入: [1,2,3,4,5]
输出: 4
解释: 第一天买(price = 1)，第五天卖(price=5)，利润为4。

Example 3:

输入: [7,6,4,3,1]
输出: 0
解释: 这个例子中没有完成交易。
"""
#方法1：贪心算法。只要后一个状态的股价比当前高，就买入今天，卖出明天。

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)==1:
            return 0
        #price只要包含两天的股价
        max_price = 0
        for i in range(len(prices)-1):#注意，这里有个减1的操作，不能遍历到最后一天
            if prices[i+1] > prices[i]:
                max_price += prices[i+1] - prices[i]
        return max_price

#方法2：动态规划方法：定义第i天的状态：f[i]表示：第i天不持有股票的最大收益金额；g[i]表示第i天持有股票的最大收益金额。
        #状态转移方程时：f[i] = max(f[i-1],g[i-1]+prices[i])
#                     g[i] = max(g[i-1],f[i-1]-prices[i])
# 最终的决策问题：返回f[n-1]
        
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)==1:
            return 0
        # 初始化两个状态变量
        f = [0]*len(prices)
        g = [0]*len(prices)
        f[0] = 0
        g[0] = -prices[0]
        for i in range(1,len(prices)):#注意这里跳过了第一个
            #更新状态
            f[i] = max(f[i-1],g[i-1]+prices[i])
            g[i] = max(g[i-1],f[i-1]-prices[i])
        return f[-1]
    
myprices = [7,1,5,3,6,4]
mysol = Solution2()
print(mysol.maxProfit(myprices))
