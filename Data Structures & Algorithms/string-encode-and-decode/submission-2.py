class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for word in strs:
            ans += "#" + str(len(word)) + "#" + word
        return ans

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s):
            i += 1
            j = 0
            while s[i].isdigit():
                j = j*10 + int(s[i])
                i += 1
            i+=1
            ans.append(s[i:i+j])
            i+=j
        return ans