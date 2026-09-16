class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l, r = 1, max(piles)
        if n == h:
            return r
        
        while l <= r:
            k = (r+l)//2
            proposed_h = sum((x+k-1)//k for x in piles)
            if proposed_h <= h:
                r = k-1
            else:
                l = k+1
        return l