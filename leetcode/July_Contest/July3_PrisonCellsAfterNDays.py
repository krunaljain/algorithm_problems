# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/544/week-1-july-1st-july-7th/3379/
class Solution:
    def prisonAfterNDays(self, cells: list[int], N: int) -> list[int]:
        temp = cells.copy()
        for i in range((N - 1)%14 + 1):
            for j in range(len(temp)):
                if j == 0 or j == len(temp) - 1 or cells[j - 1] != cells[j + 1]:
                    temp[j] = 0
                else:
                    temp[j] = 1
            cells = temp.copy()
        return cells