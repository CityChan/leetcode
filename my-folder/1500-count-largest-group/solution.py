class Solution:
    def countLargestGroup(self, n: int) -> int:
        dict = {}
        for i in range(1, n+1):
            target = sum(map(int, list(str(i))))
            dict[target] = dict.get(target, 0)+1
        count = 0
        max_val = max(dict.values())
        for val in dict.values():
            if val >= max_val:
                count += 1
        return count
