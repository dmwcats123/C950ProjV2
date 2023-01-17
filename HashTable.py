

# Create Hashmap Class
class Hashmap:
    def __init__(self, initial_capacity=20):
        self.list = []
        for i in range(initial_capacity):
            self.list.append([])

# Insert a item pair into the hashmap
    def insert(self, key, item):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

# Lookup a key and return the item if it is in the hashmap
    def lookup(self, key):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]
        return None

# Remove an item from the map with the matching key
    def remove(self, key):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        if key in bucket_list:
            bucket_list.remove(key)
