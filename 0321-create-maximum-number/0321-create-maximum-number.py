class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def max_subsequence(nums: list[int], length: int) -> list[int]:
            drop = len(nums) - length
            stack = []
            for num in nums:
                while drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:length]

        def merge(sub1: list[int], sub2: list[int]) -> list[int]:
            res = []
            i, j = 0, 0
            while i < len(sub1) or j < len(sub2):
                if sub1[i:] > sub2[j:]:
                    res.append(sub1[i])
                    i += 1
                else:
                    res.append(sub2[j])
                    j += 1
            return res

        m, n = len(nums1), len(nums2)
        best = []
        
        for i in range(max(0, k - n), min(k, m) + 1):
            sub1 = max_subsequence(nums1, i)
            sub2 = max_subsequence(nums2, k - i)
            candidate = merge(sub1, sub2)
            if candidate > best:
                best = candidate
                
        return best