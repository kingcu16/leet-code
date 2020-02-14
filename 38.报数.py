#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#
# https://leetcode-cn.com/problems/count-and-say/description/
#
# algorithms
# Easy (51.63%)
# Likes:    277
# Dislikes: 0
# Total Accepted:    40.9K
# Total Submissions: 79.3K
# Testcase Example:  '1'
#
# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
# 
# 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
# 
# 注意：整数顺序将表示为一个字符串。
# 
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "1"
# 
# 
# 示例 2:
# 
# 输入: 4
# 输出: "1211"
# 
# 
#
class Solution:

    a = [
        '1', #1
        '11', #2
        '21', #3
        '1211', #4
        '111221', #5
        '312211', #6
        '13112221', #7
        '1113213211', #8
        '31131211131221', #9
        '13211311123113112211', #10
        '11131221133112132113212221', #11
    ]
    def produceNext(self, s: str) -> str:
        start = 0
        count = 0
        curr = 0
        new_s = ''
        while True:
            if curr >= len(s):
                break

            if s[curr] == s[start]:
                count += 1
                curr += 1
            else:
                new_s += str(count) + s[start]
                start = curr
                count = 0
        return new_s + str(count) + s[-1]

    def countAndSay(self, n: int) -> str:
        
        if n <= 11:
            return self.a[n-1]
        s = self.a[10]

        for _ in range(n-11):
            s = self.produceNext(s)
        
        return s


