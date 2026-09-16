class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [1]*n
        right_prod = [1]*n

        for i in range(1,n):
            left_prod[i] = nums[i-1]*left_prod[i-1]
        for i in range(n-2, -1, -1):
            right_prod[i] = nums[i+1]*right_prod[i+1]
        ans = [left_prod[i]*right_prod[i] for i in range(n)]
        return ans