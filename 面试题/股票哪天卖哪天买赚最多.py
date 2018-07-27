# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 00:18:48 2018

@author: jikang
"""

#时间复杂度分析：组合数Cn2.效率更高的方法？
class Solution():
    
    def get_max_stock_profit(self,stock_list):
        """
        注意题目要求：想要返回的是什么。
        """
        max_profit = 0
        proper_buy_sell_days = [0,0]
        for buy_day in range(len(stock_list)-1):#为什么要减1呢？因为最后一天一定不买入股票
            buy_money = stock_list[buy_day]
            for sell_day in range(buy_day+1,len(stock_list)):
                sell_money = stock_list[sell_day]
                if sell_money-buy_money > max_profit:
                    max_profit = sell_money-buy_money
                    proper_buy_sell_days = [buy_day,sell_day]
        return proper_buy_sell_days
    
mystock_prices = [2,7,1,3,4,6,5]
mysol = Solution()
print(mysol.get_max_stock_profit(mystock_prices))
    