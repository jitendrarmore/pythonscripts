from operator import index


class hashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        print(self.table)

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        # print(index)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return 

        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if key == k:
                return v
        return None


    def remove(self, key):
        index = self._hash(key)
        self.table[index] = [pair for pair in self.table[index] if pair[0] != key]


# ▶️ Example usage
ht = hashTable(10)
ht.put("name", "Alice")
ht.put("age", 30)

print(ht.get("name"))   # Output: Alice
print(ht.get("age"))    # Output: 30

ht.remove("name")
print(ht.get("name"))   # Output: None