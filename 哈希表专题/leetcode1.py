""""
leetcode1

题目描述
给定一个整型数组，要求返回两个数的下标，使得两数之和等于给定的目标值，要求同一个下标不能使用两次。
数据保证有且仅有一组解。

样例
给定数组 nums = [2, 7, 11, 15]，以及目标值 target = 9，由于 nums[0] + nums[1] = 2 + 7 = 9, 所以 return [0, 1].

"""

class Solution():
    def twoSum(self,nums,target):
        """

        :param nums: list[int]
        :param target: int
        :return: [int,int]
        """
        hash_num_pos = {}
        n = len(nums)
        for i in range(n):
            if target-nums[i] in hash_num_pos.keys():
                return [hash_num_pos[target-nums[i]],i]
            else:
                hash_num_pos[nums[i]] = i

if __name__ == '__main__':
    mysol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(mysol.twoSum(nums,target))

