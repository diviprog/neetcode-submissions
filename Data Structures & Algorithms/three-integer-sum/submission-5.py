class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sols = list()
        nums.sort()

        for i in range(n-2):
            if nums[i] > 0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]
            l, r = i+1, n-1
            while l < r:
                if nums[l] + nums[r] == target:
                    sols.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else :
                    r -= 1
        return sols