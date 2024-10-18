class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.used = []
    def get(self, key: int) -> int:
        if key in self.cache:
            self.used.remove(key)
            self.used.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.used.remove(key)
            self.used.append(key)
            self.cache[key] = value
        else:
            while len(self.cache) >= self.cap:
                delete_key = self.used.pop(0)
                del self.cache[delete_key]
            self.used.append(key)
            self.cache[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
