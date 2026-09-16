class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        sorted_counter = sorted(counter.items(), key=lambda item:item[1], reverse=True)
        ans = [key for key, val in sorted_counter][:k]

        return ans