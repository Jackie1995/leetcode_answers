"""
leetcode 525

题目描述
给定一个二进制数组, 找到含有相同数量的 0 和 1 的最长连续子数组。

样例
输入: [0,1]
输出: 2
解释: [0, 1] 是具有相同数量0和1的最长连续子数组。
输入: [0,1,0]
输出: 2
解释: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
"""

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        hash_table = {} # key: 前缀和（int）；value：最前面的位置索引
        hash_table[0] = -1  # 初始化记录 前缀和-最早出现位置 哈希表
        tol = 0 #初始化前缀和
        ans = 0 #初始化答案
        for i in range(n):
            if nums[i] == 1:
                tol += 1
            else:
                tol -= 1
            if tol in hash_table:
                ans = max(ans,i -hash_table[tol]) #注意：这里需不需要在前缀和相减的位置再加1？
            else:
                hash_table[tol] = i
        return ans

if __name__ == '__main__':
    mysol = Solution()
    nums = [0,1,0]
    print(mysol.findMaxLength(nums))

