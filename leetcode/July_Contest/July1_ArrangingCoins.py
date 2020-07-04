# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3377/
import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # solve the equation n*(n+1)/2 = no. of points to get the solution
        return (int(math.sqrt(8*n + 1)) - 1)//2