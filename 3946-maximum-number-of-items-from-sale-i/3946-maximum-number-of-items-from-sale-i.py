from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        
        bonus = [0] * n
        for i in range(n):
            f_i = items[i][0]
            for j in range(n):
                if i != j and items[j][0] % f_i == 0:
                    bonus[i] += 1
                    
        dp = [0] * (budget + 1)
        
        for i in range(n):
            price = items[i][1]
            if price > budget:
                continue
                
            first_copy_gain = 1 + bonus[i]
            
            for c in range(budget, price - 1, -1):
                if dp[c - price] + first_copy_gain > dp[c]:
                    dp[c] = dp[c - price] + first_copy_gain
                    
            for c in range(price, budget + 1):
                if dp[c - price] + 1 > dp[c]:
                    dp[c] = dp[c - price] + 1
                    
        return dp[budget]