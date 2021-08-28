class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)<3:
            return 0
        s = 0
        i = 0
        j = len(height)-1
        while i<len(height) and height[i]==0:
            i+=1
        while j>0 and height[j]==0:
            j-=1
        h_leftmax = height[i]
        h_rightmax = height[j]
        while i<=j:
            if h_leftmax<h_rightmax:
                if height[i]<h_leftmax:
                    s+=(h_leftmax-height[i])
                else:
                    h_leftmax=height[i]
                i+=1
            else:
                if height[j]<h_rightmax:
                    s+=(h_rightmax-height[j])
                else:
                    h_rightmax=height[j]
                j-=1
                
        
        return s
                
            
            
