"""
leetocode 153
题目描述
现有一个有序数组，假设从某个数开始将它后面的数按顺序放到了数组前面。
(即 [0,1,2,4,5,6,7] 可能变成 [4,5,6,7,0,1,2])。

请找出数组中的最小元素。

数组中不包含重复元素。

样例1
输入：[3,4,5,1,2]
输出：1
"""

## 我这个题目做的比题解要好！！
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
            """
        length = len(nums)
        if length < 5:
            return min(nums)
        left = 0
        right = length-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid+1
        return nums[left]
if __name__ == '__main__':
    mysol = Solution()
    nums = [3,4,5,1,2]
    print(mysol.findMin(nums))

