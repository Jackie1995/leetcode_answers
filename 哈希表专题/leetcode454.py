"""
leetcode454

目前的版本：在leetcode提交：时间超限。
题目描述
给定四个整型数组 A、B、C和D，计算有多少四元组 (i, j, k, l) 使得 A[i] + B[j] + C[k] + D[l] 等于0。

为了使问题简单一些，A、B、C和D长度相同且为N，0≤N≤5000≤N≤500。所有的整数在−228−228到228−1228−1内，答案个数保证不超过231−1231−1。

样例
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2
"""

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hash_sum_freq = {}
        ans = 0
        for a in A:
            for b in B:
                if a+b in hash_sum_freq:
                    hash_sum_freq[a+b] += 1
                else:
                    hash_sum_freq[a+b] = 1
        # 上面n2的时间复杂度
        for c in C:
            for d in D:
                if (-c-d) in hash_sum_freq:
                    ans += hash_sum_freq[-c-d]
        return ans

if __name__ == '__main__':
    mysol = Solution()
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(mysol.fourSumCount(A,B,C,D))