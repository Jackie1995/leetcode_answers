"""
leetcode 350
题目描述
给定两个数组，请写一个函数计算它们的交集。

注意：

每个数在结果中出现的次数，需要和它在两个数组中出现的次数相同；
结果可以以任意顺序输出；
思考题：

如果给定的数组已经排好序，你可以怎样优化你的算法？
如果数组nums1的长度小于数组nums2的长度，哪种算法更好？
如果数组nums2存储在硬盘上，然而内存是有限的，你不能将整个数组都读入内存，该怎么做？
样例
给定 nums1 = [1, 2, 2, 1], nums2 = [2, 2],
返回 [2, 2].
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 第一步：对nums1生成计数哈希表
        hash_table = {} #这个哈希表里面存的是：nums1里面出现的数字（key），及其出现的次数（value）
        for num in nums1:
            hash_table[num] = hash_table.get(num,0) + 1
        # 第二步：依照nums2中的数字，对哈希表进行调整。
        ans = []
        for num in nums2:
            if num in hash_table:
               ans.append(num)
               hash_table[num] -= 1
               if hash_table[num] == 0:
                   del hash_table[num] #注意删除字典中某个键值对的语法。
        return ans

if __name__ == '__main__':
    mysol = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(mysol.intersect(nums1,nums2))

