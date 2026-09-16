class Solution:

    def encode(self, strs: List[str]) -> str:
        concat = ""
        for piece in strs:
            length = len(piece)
            concat += str(length) + "#" + piece
        return concat

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            num = int(s[i:j])
            i = j + 1
            ans.append(s[i:i+num])
            i += num
        return ans