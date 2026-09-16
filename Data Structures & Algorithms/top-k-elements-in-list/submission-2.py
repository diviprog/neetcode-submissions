class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        seen = defaultdict(int)

        for num in nums:
            seen[num] += 1
        
        ans = sorted(seen, key = lambda x:seen[x], reverse=True)
        return ans[:k]