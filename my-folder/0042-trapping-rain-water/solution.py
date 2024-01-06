class Solution:
    def trap(self, height: List[int]) -> int:
        water_amt = 0
        left = -1
        right = len(height)
        left_max = 0
        right_max = 0
        while left<right:
            if left_max<right_max:
                left+=1
                if height[left]>left_max:
                    left_max = height[left]
                else:
                    water_amt+=(left_max-height[left])
                    # print(water_amt)                  

            else:
                right-=1
                if height[right]>right_max:
                    right_max = height[right]
                else:
                    water_amt+=(right_max-height[right])
                    # print(water_amt)

        return water_amt
            
            
        
