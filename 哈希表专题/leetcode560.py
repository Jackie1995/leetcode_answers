"""
leetcode 560
问题：时间超限--已在问答版面提问。
题目描述
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

样例
输入: nums = [1,1,1], k = 2
输出: 2
"""
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        hash_prefixsum_freq = {} # {int:int}
        hash_prefixsum_freq[0] = 1
        tol =0
        for num in nums:
            tol += num
            if tol-k in hash_prefixsum_freq:
                ans += hash_prefixsum_freq[tol-k]
            hash_prefixsum_freq[tol] = hash_prefixsum_freq.setdefault(tol,0)+1
        return ans

if __name__ == '__main__':
    mysol = Solution()
    nums = [1, 1, 1]
    k = 2
    print(mysol.subarraySum(nums,k))
