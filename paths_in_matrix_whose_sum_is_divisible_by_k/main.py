from typing import List

MOD = 1_000_000_007

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                v = grid[i][j] % k

                if i == 0 and j == 0:
                    dp[i][j][v] = 1
                
                if i > 0:
                    for prev_r in range(k):
                        new_r = (v + prev_r) % k
                        dp[i][j][new_r] += dp[i-1][j][prev_r]
                
                if j > 0:
                    for prev_r in range(k):
                        new_r = (v + prev_r) % k
                        dp[i][j][new_r] += dp[i][j - 1][prev_r]

        return dp[m-1][n-1][0] % MOD
