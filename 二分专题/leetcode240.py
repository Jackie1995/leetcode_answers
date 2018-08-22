"""
leetcode 240
题目描述
写一个高效的算法在 n x m 的矩阵中查找某个元素，矩阵具有有如下性质：

每一行的整数从左到右单调递增。
每一列的整数从上到下单调递增。
样例
考虑如下矩阵
matrix =
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5
给定 target = 5, 返回 true.

给定 target = 20, 返回 false.
"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        nrow = len(matrix)
        ncol = len(matrix[0])
        length = nrow*ncol
#         初始化起始点的位置
        i = 0
        j = ncol-1
        while i < nrow and j >=0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j = j-1
            else:
                i = i+1
        return False

if __name__ == '__main__':
    mysol = Solution()
    matrix =[
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    # target = 5
    target = 20
    print(mysol.searchMatrix(matrix,target))
