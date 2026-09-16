class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for word in strs:
            letters = ''.join(sorted(word))
            if letters in hashmap:
                hashmap[letters].append(word)
            else:
                hashmap[letters] = [word]
        
        answer = []
        for group in hashmap.values():
            answer.append(group)
        return answer