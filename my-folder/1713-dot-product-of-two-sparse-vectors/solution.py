class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums_dict = {i:n for i, n in enumerate(nums) if n!=0}
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        s = 0
        for i in self.nums_dict:
            if i in vec.nums_dict:
                s+=self.nums_dict[i]*vec.nums_dict[i]
        return s
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
