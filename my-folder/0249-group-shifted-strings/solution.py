class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        ans = []
        hashmap = {}
        for s in strings:
            new_s = ""
            diff = ord(s[0]) - ord('a')
            for c in s:
                new_s += chr(ord(c) - diff if ord(c) - diff >= ord('a') else ord(c) - diff + 26)
            if new_s in hashmap:
                hashmap[new_s].append(s)
            else:
                hashmap[new_s] = [s]
        return list(hashmap.values())
