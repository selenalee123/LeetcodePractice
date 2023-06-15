"""
LeetCode Problem: Climbing Stairs
LeetCode Link: https://leetcode.com/problems/climbing-stairs/

Problem Description:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Solution:
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n ==1:
            return 1
        dp = [0] * (n+1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
    
    # Return the number of distinct ways to reach the top
        return dp[n]
