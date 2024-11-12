class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0]*n
        stk = []
        prev = 0
        for log in logs:
            idx, op, time = log.split(':')
            idx, time = int(idx), int(time)
            if op == 'start':
                if stk:
                    ans[stk[-1]] += time - prev
                stk.append(idx)
                prev = time
            else:
                ans[stk.pop()] += time - prev + 1
                prev = time+1
        return ans


