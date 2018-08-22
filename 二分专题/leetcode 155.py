"""
leetcode 155

题目描述
请设计一个栈结构，支持 push、pop、top以及getMin操作，且每个操作的时间复杂度都是 O(1)O(1)。

push(x) – 向栈中压入元素 xx；
pop() – 删除栈顶元素；
top() – 返回栈顶元素；
getMin() – 返回栈中的最小元素；
样例
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.value = []
        self.stackmin = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stackmin:
            self.stackmin.append(x)
        else:
            if x <= self.stackmin[-1]: #注意这里如果压入的数字是小于等于单调栈栈顶元素；划重点！小于等于！不能能写小于。
                self.stackmin.append(x)
        self.value.append(x)

    def pop(self):
        """
        :rtype: void
        """
        pop_value = self.value.pop()
        if pop_value == self.stackmin[-1]:
            self.stackmin.pop()


    def top(self):
        """
        :rtype: int
        """
        if self.value:
            return self.value[-1]
        else:
            return None
    def getMin(self):
        """
        :rtype: int
        """
        if self.stackmin:
            return self.stackmin[-1]
        else:
            return None