class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        res = []
        dq = deque()
        for i, num in enumerate(nums):
            while dq and dq[0] <= i-k:
                dq.popleft()
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                res.append(nums[dq[0]])
        return res