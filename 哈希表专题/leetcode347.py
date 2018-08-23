"""
leetocode 347
题目描述
给定一个非空整数数组，请返回出现次数最多的 k 个数。

注意：

你可以假定 k一定是合法的，即 1≤k≤ 数组中不同元素的个数，且排名在第 k 位和排名在第 k+1 位的数，出现次数不同；
你的算法一定要比 O(nlogn) 快；
样例
给定 [1,1,1,2,2,3] 并且 k = 2,
返回 [1,2].
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 第一步：先用哈希表记录每个数字出现的次数：
        hash_table = {} #记录每个数字出现的次数
        n = len(nums)
        for num in nums:
            hash_table[num] = hash_table.get(num,0)+1

        # 第二步：计数排序，求出现次数排在第k的出现次数是多少？得到border的值
        s = [0]*(n+1)
        for num_val in hash_table.values():
            s[num_val] += 1
        # 从后往前找border
        t = s[n] # t是初始化累计计数值
        j = n
        while t < k:  #当跳出这个循环，也就是 t=k 时，认为找到了合适的border值。
            t = t + s[j-1]
            j -= 1
        border = j

        # 第三步：找出 value>border 的所有key值
        ans = []
        for (num,count) in hash_table.items():
            if count >= border:
                ans.append(num)
        return ans

if __name__ == '__main__':
    mysol = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(mysol.topKFrequent(nums,k))




