class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pad_flowerbed = [0] + flowerbed + [0]
        count = 0
        for i in range(len(flowerbed)):
            if pad_flowerbed[i:i+3] == [0, 0, 0]:
                pad_flowerbed[i+1] = 1
                count += 1
        return count >= n
