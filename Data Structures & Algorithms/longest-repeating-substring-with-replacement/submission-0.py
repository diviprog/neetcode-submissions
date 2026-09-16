class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        
        count = defaultdict(int)
        best = 0
        l = 0
        max_count = 0

        for r, ch in enumerate(s):
            count[ch] += 1
            max_count = max(max_count, count[ch])

            while (r - l + 1) - max_count > k:
                count[s[l]] -= 1
                l += 1
            best = max(best, r-l+1)
        return best