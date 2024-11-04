class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = [folder[0]]
        for path in folder[1:]:
            m, n = len(ans[-1]), len(path)
            if m > n or not (path[:m] == ans[-1] and path[m] == '/'):
                ans.append(path)
        return ans
