from collections import Counter
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        freq = Counter(f for f, _ in items)
        max_f = max(freq)
        
        divisible_count = {}
        for f in freq:
            total = 0
            for mult in range(f, max_f + 1, f):
                if mult in freq:
                    total += freq[mult]
            divisible_count[f] = total - 1
            
        min_price = min(price for _, price in items)
        
        items_sorted = sorted(items, key=lambda x: x[1])
        
        total_items = 0
        rem_budget = budget
        
        for f, price in items_sorted:
            if price >= 2 * min_price or rem_budget < price:
                break
                
            can_buy = min(divisible_count[f], rem_budget // price)
            total_items += can_buy * 2
            rem_budget -= can_buy * price

        total_items += rem_budget // min_price
        
        return total_items