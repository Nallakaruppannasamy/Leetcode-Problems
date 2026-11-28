class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        prev = [0] * (k + 1)
        prev[0] = 1
        
        for i in range(1, n + 1):
            curr = [0] * (k + 1)
            curr[0] = 1
            for j in range(1, k + 1):
                val = (curr[j - 1] + prev[j]) % MOD
                if j >= i:
                    val = (val - prev[j - i]) % MOD
                curr[j] = val
            prev = curr
            
        return prev[k]