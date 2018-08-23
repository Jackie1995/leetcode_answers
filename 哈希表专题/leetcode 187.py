"""
leetcode187
题目描述
所有DNA序列都可以用 A，C，G，T 四个字母表示，比如 "ACGAATTCCG"，研究DNA序列时，有时识别重复子串是很有意义的。

请编写一个程序，找到所有长度为10的且出现次数多于1的子串。

样例
输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC", "CCCCCAAAAA"]
"""
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 这个题目比较简单的地方在于：子串的长度是已知的=10，所以就可以用哈希表
        n = len(s)
        hash_table = {}
        i = 0 #初始化索引
        ans = []
        while i+10<= n:
            subtring = s[i:i+10]
            hash_table[subtring] = hash_table.get(subtring,0)+1
            i += 1
        for (subtring,count) in hash_table.items():
            if count > 1:
                ans.append(subtring)
        return ans
if __name__ == '__main__':
    mysol = Solution()
    s = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
    print(mysol.findRepeatedDnaSequences(s))

