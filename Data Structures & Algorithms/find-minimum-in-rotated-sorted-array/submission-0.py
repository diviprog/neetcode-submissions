class Solution:
    def findMin(self, nums: List[int]) -> int:
        end = nums[-1]
        l, r = 0, len(nums)-1

        while l <= r:
            m = (r+l)//2
            if nums[m]>end:
                l = m+1
            else:
                r = m-1
        return nums[l]