# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3380/
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        two = 0
        three = 0
        five = 0
        dp = [1]
        while len(dp) < n:
            val = min([2 * dp[two], 3 * dp[three], 5 * dp[five]])
            if val == 2 * dp[two]:
                two += 1
            if val == 3 * dp[three]:
                three += 1
            if val == 5 * dp[five]:
                five += 1
            dp.append(val)
        return dp[-1]
if __name__ == '__main__':
    x = [1,2,3,4]
    print(''.join(str(x)))