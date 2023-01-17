

# Create Hashmap Class
class Hashmap:
    def __init__(self, size=20):
        self.list = []
        for i in range(size):
            self.list.append([])

# Insert a item pair into the hashmap
    # Source:
    # C950 - Webinar-1 - Let’s Go Hashing
    # W-1_ChainingHashTable_zyBooks_Key-Value.py
    # Ref: zyBooks: Figure 7.8.2: Hash table using chaining.
    def insert(self, key, item):
        bucket = hash(key) % len(self.list)
        list_bucket = self.list[bucket]

        for key_val in list_bucket:
            if key_val[0] == key:
                key_val[1] = item
                return True

        key_value = [key, item]
        list_bucket.append(key_value)
        return True

# Lookup a key and return the item if it is in the hashmap
    def lookup(self, key):
        bucket = hash(key) % len(self.list)
        list_bucket = self.list[bucket]
        for pair in list_bucket:
            if key == pair[0]:
                return pair[1]
        return None

# Remove an item from the map with the matching key
    def remove(self, key):
        bucket = hash(key) % len(self.list)
        list_bucket = self.list[bucket]
        if key in list_bucket:
            list_bucket.remove(key)
