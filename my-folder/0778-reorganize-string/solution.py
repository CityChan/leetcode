class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = ""
        count = dict(Counter(s))
        keys = sorted(count, key = count.get, reverse = True)
        
        while len(keys) >= 2:
            cur = 0
            if len(ans):
                while ans[-1] == keys[cur]:
                    cur += 1
            max_freq = keys[cur]
            ans += max_freq
            count[max_freq] -= 1
            if count[max_freq] == 0:
                del count[max_freq]
            keys = sorted(count, key = count.get, reverse = True)
        if count[keys[0]] > 1:
            return ""
        ans += keys[0]
        return ans

