class Solution:
    def numDecodings(self, s: str) -> int:
        # A string starting with '0' cannot be decoded
        if not s or s[0] == '0':
            return 0
        
        # prev2 corresponds to dp[i-2], prev1 corresponds to dp[i-1]
        prev2 = 1  # Empty prefix
        prev1 = 1  # Prefix of length 1 (since s[0] != '0')
        
        for i in range(2, len(s) + 1):
            curr = 0
            
            # Check single digit: s[i-1]
            if s[i - 1] != '0':
                curr += prev1
                
            # Check two digits: s[i-2:i]
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                curr += prev2
                
            # Advance variables
            prev2 = prev1
            prev1 = curr
            
        return prev1