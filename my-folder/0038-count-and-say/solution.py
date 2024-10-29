class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        RLE = self.countAndSay(n - 1)
        if RLE is None or len(RLE) == 0:
            return None
        m = len(RLE)
        prev = RLE[0]
        print(prev)
        cnt = 1
        ans = ""
        for i in range(1,m):
            if RLE[i] == prev:
                cnt +=1
            else:
                ans = ans + str(cnt) + prev
                cnt = 1
                prev = RLE[i]
        ans = ans + str(cnt) + prev
        return ans

