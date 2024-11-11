class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            answer =  self.cache[key]
            self.cache.pop(key)
            self.cache[key] = answer
            return answer
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.cap:
                ordest_key = next(iter(self.cache))
                self.cache.pop(ordest_key)
            self.cache[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
