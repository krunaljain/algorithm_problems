# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3378/
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def levelOrderBottom(self, root):
        # bfs followed by reversing of output
        res = []
        if not root:
            return res
        temp = [root]
        while temp:
            res.append([x.val for x in temp])
            temp = [x for val in temp for x in [val.left, val.right] if x]
        res.reverse()
        return res