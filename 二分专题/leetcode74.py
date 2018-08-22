"""
leetcode 74: Search a 2D Matrix
题目描述
写一个高效算法，在矩阵中查找一个数是否存在。矩阵有如下特点：

矩阵中每行的数，从左到右单调递增；
每行行首的数大于上一行行尾的数；
样例1
输入：
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出： true
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
        left = 0
        right = length-1
        while left <= right:
            mid = (left+right)//2
            i = mid//ncol
            j = mid%ncol
            if matrix[i][j] < target:
                left = mid + 1
            elif matrix[i][j] > target:
                right = mid -1
            else:
                return True
        return False

if __name__ == '__main__':
    mysol = Solution()
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 3
    print(mysol.searchMatrix(matrix,target))
