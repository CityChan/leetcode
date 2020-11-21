class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        for num in sorted(arr):
            if num not in rank:
                rank[num] = len(rank)+1
        return map(lambda a : rank[a], arr)
