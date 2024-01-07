class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if (flowerbed[i]==1) or (i-1>=0 and flowerbed[i-1]==1) or (i+1<=len(flowerbed)-1 and flowerbed[i+1]==1):
                continue
            else:
                flowerbed[i]=1
                n-=1
        return n<=0
        
