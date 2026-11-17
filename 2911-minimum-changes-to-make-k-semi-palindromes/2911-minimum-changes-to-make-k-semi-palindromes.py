class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        divisors = [[] for _ in range(n + 1)]
        for L in range(2, n + 1):
            for d in range(1, L):
                if L % d == 0:
                    divisors[L].append(d)
                    
        INF = float('inf')
        cost = [[INF] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):
                L = j - i + 1
                min_changes = INF
                for d in divisors[L]:
                    changes = 0
                    for start in range(d):
                        left = i + start
                        right = j - (d - 1 - start)
                        while left < right:
                            if s[left] != s[right]:
                                changes += 1
                            left += d
                            right -= d
                    if changes < min_changes:
                        min_changes = changes
                cost[i][j] = min_changes
                
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        
        for p in range(1, k + 1):
            for j in range(2 * p, n + 1):
                for i in range(2 * (p - 1), j - 1):
                    if dp[p - 1][i] + cost[i][j - 1] < dp[p][j]:
                        dp[p][j] = dp[p - 1][i] + cost[i][j - 1]
                        
        return dp[k][n]