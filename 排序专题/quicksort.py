"""
quicksort
"""
# 这个题目要注意的一个地方是：python的函数参数并不全都是：传值调用，对于可变的数据类型来说，都是传引用调用。
class Solution():

    def quicksort(self,nums):
        """
        :param nums: list[int]
        :return: list[int]
        """
        self.quicksort2(nums,0,len(nums)-1)
        return nums

    def quicksort2(self,nums,l,r):
        """

        :param nums:list[int]
        :param l: int
        :param r: int
        :return: void
        """
        if l < r:
            pivot_pos = self.partation(nums,l,r)
            self.quicksort2(nums,l,pivot_pos-1)
            self.quicksort2(nums,pivot_pos+1,r)

    def partation(self,nums,l,r):
        """
        :param nums: list[int]
        :param l: int
        :param r: int
        :return: int
        """
        pivot = nums[l] #先找到基准点
        i = l
        j = r
        while i < j:
            while nums[i] <= pivot:
                i += 1
            while nums[j] > pivot:
                j -= 1
            if i < j:
                nums[i] ,nums[j] = nums[j],nums[i]

        nums[l] = nums[j]
        nums[j] = pivot

        return j

if __name__ == '__main__':
    mysol = Solution()
    import random
    a = list(range(30))
    random.shuffle(a)
    print(mysol.quicksort(a))
