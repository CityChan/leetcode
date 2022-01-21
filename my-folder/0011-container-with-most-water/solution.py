class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_idx, right_idx = 0, len(height)-1
        water = 0
        while left_idx<right_idx:
            water = max(water, min(height[left_idx], height[right_idx])*(right_idx-left_idx))
            if height[left_idx]<height[right_idx]:
                left_idx+=1
            elif height[left_idx]>height[right_idx]:
                right_idx-=1
            else:
                left_idx+=1
                right_idx-=1
        return water
                
        
