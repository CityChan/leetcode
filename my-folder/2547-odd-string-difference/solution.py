class Solution:
    def oddString(self, words: List[str]) -> str:
        d = defaultdict(list)
        for s in words:
            t = tuple(ord(b) - ord(a) for a, b in pairwise(s))
            d[t].append(s)
        d_list = list(d.values())
        for l in d_list:
            if len(l) == 1:
                return l[0]
