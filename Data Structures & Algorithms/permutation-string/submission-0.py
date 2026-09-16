class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        idx = lambda c: ord(c) - ord('a')
        need = [0]*26
        have = [0]*26
        for ch in s1:
            need[idx(ch)] += 1
        for i, ch in enumerate(s2):
            have[idx(ch)] += 1
            if i >= n1:
                have[idx(s2[i-n1])] -= 1
            if have == need:
                return True
        return False