class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        strs_idx = [str(sorted(x)) for x in strs]
        for i, str_ in enumerate(strs_idx):
            if str_ not in res:
                res[str_]=[strs[i]]
            else:
                res[str_]+=[strs[i]]
        return list(res.values())
