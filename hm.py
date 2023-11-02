class HashMap:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.hash_table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        if self.hash_table[index] is None:
            self.hash_table[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.hash_table[index]):
                if k == key:
                    self.hash_table[index][i] = (key, value)
            
            self.hash_table[index].append((key, value))
    def get(self, key):
        index = self._hash(key)
        if self.hash_table[index] is not None:
            for k, v in self.hash_table[index]:
                if k == key:
                    return v
        return KeyError(f"Key '{key}' not found in the hash map.")

    def remove(self, key):
        index = self._hash(key)
        if self.hash_table[index] is not None:
            for i, (k, v) in enumerate(self.hash_table[index]):
                if k == key:
                    del self.hash_table[index][i]
        return KeyError(f"Key '{key}' not found in the hash map.")
