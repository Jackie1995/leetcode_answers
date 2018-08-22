"""
leetcode 162

题目描述
峰值定义为比左右相邻元素大的元素。

给定一个数组 nums，保证 nums[i] ≠ nums[i+1]，请找出该数组的峰值，并返回峰值的下标。

数组中可能包含多个峰值，只需返回任意一个即可。

假定 nums[-1] = nums[n] = -∞。

样例1
输入：nums = [1,2,3,1]
输出：2
解释：3是一个峰值，3的下标是2。
"""

## 感觉二分法的题目的处理方式都是：确定可以用二分法之后，重点在于取左边还是取右边的条件语句的判断。

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        left = 0
        right = length-1
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid +1
        return left

if __name__ == '__main__':
    mysol = Solution()
    nums = [1, 2, 3, 1]
    print(mysol.findPeakElement(nums))

