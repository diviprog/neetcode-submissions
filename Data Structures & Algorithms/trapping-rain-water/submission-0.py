class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n

        max_prefix = 0
        for i in range(n):
            max_prefix = max(max_prefix, height[i])
            prefix[i] = max_prefix
        max_suffix = 0
        for i in range(n-1, -1, -1):
            max_suffix = max(max_suffix, height[i])
            suffix[i] = max_suffix
        
        water = 0
        for i in range(n):
            water += min(prefix[i], suffix[i]) - height[i]
        
        return water