"""
LeetCode Problem: Min Cost Climbing Stairs
LeetCode Link: https://leetcode.com/problems/min-cost-climbing-stairs/

Problem Description:
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Solution:
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
    
    # Create a dp table to store the minimum cost to reach each step
        dp = [0] * n
        
        # Initialize the first two entries of the dp table
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        # Compute the minimum cost for each step starting from the third step
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        # Return the minimum cost to reach the top
        return min(dp[n-1] , dp[n-2])