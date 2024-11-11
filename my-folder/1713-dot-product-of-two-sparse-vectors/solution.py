class SparseVector:
    def __init__(self, nums: List[int]):
        self.indices = {}
        for i,num in enumerate(nums):
            if num == 0:
                continue
            self.indices[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        indices = vec.indices
        sum = 0
        for idx in indices:
            if idx not in self.indices:
                continue
            num1 = indices[idx]
            num2 = self.indices[idx]
            sum = sum + num1*num2
        return sum

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
