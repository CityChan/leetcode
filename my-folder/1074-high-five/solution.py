class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(key=lambda x: (x[0], -x[1]))
        res = [[key, sum([x[1] for x in group][:5])//5]
              for key, group in groupby(items, lambda p: p[0])]
        return res
        
