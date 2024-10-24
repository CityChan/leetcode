class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            key = []
            for c in s:
                key.append(c)
            key.sort(key = lambda x: ord(x))
            key = "".join(key)
            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]
        return list(hashmap.values())
            
