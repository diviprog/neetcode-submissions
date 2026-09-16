class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        while nums:
            min_num = min(nums)
            length = 1
            while min_num+1 in nums:
                nums.remove(min_num)
                min_num += 1
                length += 1
            max_len = max(max_len, length)
            nums.remove(min_num)
        return max_len