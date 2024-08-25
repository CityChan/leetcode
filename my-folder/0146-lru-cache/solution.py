class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.makeRecently(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.makeRecently(key)
            return
        if len(self.cache) == self.capacity:
            oldestkey = next(iter(self.cache))
            self.cache.pop(oldestkey)
        self.cache[key] = value
            

    def makeRecently(self, key):
        value = self.cache.pop(key)
        self.cache[key] = value
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
