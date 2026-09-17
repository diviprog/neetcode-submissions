class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post, ans = [1]*len(nums), [1]*len(nums), [1]*len(nums)

        for i in range(1,len(nums)):
            pre[i] = nums[i-1]*pre[i-1]
        for i in range(len(nums)-2, -1, -1):
            post[i] = nums[i+1]*post[i+1]
        
        for i in range(len(nums)):
            ans[i] = post[i]*pre[i]
        
        return ans