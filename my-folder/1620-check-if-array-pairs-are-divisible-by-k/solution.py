class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        save_dict = {}
        for i in arr:
            if i%k in save_dict:
                save_dict[i%k]+=1
            else: 
                save_dict[i%k]=1
                
        if 0 in save_dict:
            if save_dict[0]%2==1:
                return False
        if k%2==0 and k//2 in save_dict:
            if save_dict[k//2]%2==1:
                return False
            
            
        for i in range(1, k+1//2+1):
            if i in save_dict:
                if k-i not in save_dict or save_dict[k-i]!=save_dict[i]:
                    return False
        return True
            
        
