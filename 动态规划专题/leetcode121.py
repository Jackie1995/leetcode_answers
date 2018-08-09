# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 23:52:36 2018

@author: jikang

leetcode 121: 股票问题1

题目描述
假设你有一个数组，其中第i个元素表示第i天某个股票的价格。

如果您只允许完成至多一笔交易（即买入一只股票并卖出一只股票），则设计一种算法以找到最大利润。

必须先购买股票再出售股票。

样例
Example 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第二天买(price = 1) ，在第五天卖 (price = 6), 利润 = 6-1 = 5.

Example 2:

输入: [7,6,4,3,1]
输出: 0
解释: 这个例子中没有完成交易。
"""

# 贪心算法
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        low = prices[0] #初始化最低价
        max_profit = 0
        # 状态f【i】:第i天卖出股票时的最大利润
        for i in range(len(prices)):
            low = min(low,prices[i]) #low指的是当前最小值。
            max_profit = max(max_profit,prices[i]-low)
        return max_profit
    
myprices = [7,6,4,3,1]
mysol = Solution()
print(mysol.maxProfit(myprices))
