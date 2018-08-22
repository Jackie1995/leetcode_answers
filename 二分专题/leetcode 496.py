"""
leetcode 496 Next Greater Element I

题目描述
给定两个没有重复元素的数组 nums1 和 nums2 ，其中 nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1。

样例
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于 nums1 中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于 nums1 中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于 nums1 中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。
"""


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 生成一个哈希表
        # 哈希表（字典）的key是：number, value是：右边第一个比number大的数的位置索引。
        # 哈希表与单调栈的关系是：从后往前遍历数组中的数字，该数字即为哈希表中的key，然后value要从此时的单调栈中得到。
        # 迭代到某一个数字的时候，怎么操作单调栈呢?比较栈顶元素与该目标数字的大小，如果栈顶元素小于等于该数字，就弹出栈顶元素，
        # 直到 栈顶元素 大于 目标数字。
        # 单调栈的元素是：数字
        pos_dict = {}
        for i,number in enumerate(nums2):
            pos_dict[number] = i

