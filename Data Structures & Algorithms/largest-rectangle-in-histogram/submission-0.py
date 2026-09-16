class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def longest(threshold):
            curr = 0
            best = 0
            for height in heights:
                if height >= threshold:
                    curr += 1
                    best = max(best, curr)
                else:
                    curr = 0
            return best
        best = 0
        for i in range(max(heights)+1):
            best = max(best, i*longest(i))
        return best