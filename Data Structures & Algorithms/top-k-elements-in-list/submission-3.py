class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        seen = defaultdict(int)

        for num in nums:
            seen[num] += 1
        
        bucket_list = [[] for i in range(len(nums)+1)]

        for key, val in seen.items():
            bucket_list[val].append(key)
        
        result = []
        for bucket in bucket_list[::-1]:
            for num in bucket:
                result.append(num)

                if len(result) == k:
                    return result

