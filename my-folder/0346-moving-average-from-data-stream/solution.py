class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.cache = []

    def next(self, val: int) -> float:
        while len(self.cache) >= self.size:
            self.cache.pop(0)
        self.cache.append(val)
        return sum(self.cache)/len(self.cache)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
