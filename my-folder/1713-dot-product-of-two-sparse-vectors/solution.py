class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums_dict = {}
        for i,num in enumerate(nums):
            if num != 0:
                self.nums_dict[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dotproduct = 0
        for key in vec.nums_dict:
            if key in self.nums_dict:
                dotproduct += vec.nums_dict[key]*self.nums_dict[key]
        return dotproduct
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
