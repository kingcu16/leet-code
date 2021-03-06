#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#
# https://leetcode-cn.com/problems/implement-strstr/description/
#
# algorithms
# Easy (38.69%)
# Likes:    240
# Dislikes: 0
# Total Accepted:    70.1K
# Total Submissions: 181.4K
# Testcase Example:  '"hello"\n"ll"'
#
# 实现 strStr() 函数。
# 
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置
# (从0开始)。如果不存在，则返回  -1。
# 
# 示例 1:
# 
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 
# 
# 说明:
# 
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
# 
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        if len(needle) == 0:
            return 0
        if haystack == needle:
            return 0
        
        if len(haystack) == len(needle):
            return -1
        
        head_match_list = []

        for i in range(len(haystack)-len(needle)+1):
            if haystack[i] == needle[0] and haystack[i+len(needle)-1] == needle[-1]:
                head_match_list.append(i)
        
        if len(head_match_list) == 0:
            return -1
        if len(needle) == 1 or len(needle) == 2:
            return head_match_list[0]

        find = -1

        for start in head_match_list:
            for i in range(start, start+len(needle)):
                if haystack[i] != needle[i-start]:
                    break
                else:
                    find = i
            if find - start == len(needle) - 1:
                find = start
                break
            find  = -1

        return find

