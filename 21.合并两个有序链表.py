#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (56.17%)
# Likes:    549
# Dislikes: 0
# Total Accepted:    92.1K
# Total Submissions: 164K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        if l1.val > l2.val:
            new_list = ListNode(l2.val)
            l1_node = l1
            l2_node = l2.next
        else:
            new_list = ListNode(l1.val)
            l1_node = l1.next
            l2_node = l2
        new_node = new_list
        while (l1_node is not None) and (l2_node is not None):
            if l1_node.val > l2_node.val:
                new_node.next = l2_node
                l2_node = l2_node.next
                new_node = new_node.next
            else:
                new_node.next = l1_node
                new_node = new_node.next
                l1_node = l1_node.next

        if l1_node:
            new_node.next = l1_node
        elif l2_node:
            new_node.next = l2_node
        
        return new_list


