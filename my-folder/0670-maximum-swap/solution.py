class Solution:
    def maximumSwap(self, num: int) -> int:
        hashmap = {}
        num_str = list(str(num))
        for i in range(len(num_str)):
            if num_str[i] in hashmap:
                hashmap[int(num_str[i])].append(i)
            else:
                hashmap[int(num_str[i])] = [i]
        keys = list(hashmap.keys())
        keys.sort(reverse = True)
        indexs = []
        for key in keys:
            indexs += hashmap[key]
        cur = 0
        left = 0
        while left < len(num_str):
            if indexs[cur] == left:
                left += 1
                cur +=1
            elif int(num_str[indexs[cur]]) <= int(num_str[left]):
                left += 1
            else:
                break
        if left == len(num_str):
            return num

        temp = num_str[indexs[cur]]
        num_str[indexs[cur]] = num_str[left]
        num_str[left] = temp
        s = ''.join(x for x in num_str)
        return int(s)
        
        
            
