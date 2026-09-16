class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contains(need, have):
            for i in range(len(need)):
                if need[i] > have[i]:
                    return False
            return True
        
        need = [0]*52
        have = [0]*52
        
        def idx(char):
            if char >= 'a' and char <= 'z':
                return ord(char) - ord('a')
            elif char >= 'A' and char <= 'Z':
                return 26 + ord(char) - ord('A')

        for char in t:
            need[idx(char)] += 1
        
        min_str = ""
        min_length = float('inf')
        l = 0
        for r, char in enumerate(s):
            have[idx(char)] += 1
            while contains(need, have):
                if r-l+1 < min_length:
                    min_str = s[l:r+1]
                    min_length = r-l+1
                have[idx(s[l])] -= 1
                l += 1
        return min_str
            