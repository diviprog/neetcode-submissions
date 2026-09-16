class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anas = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anas[key].append(word)
        return list(anas.values())