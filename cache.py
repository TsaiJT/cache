import math

class Cache:

    def __init__(self, cache_size):
        # Init the cache size
        # Use dict to store key-(value, weight)
        # Use list to record the access time.
        # Set the current_time is cache size because of the full capacity.
        self.cache_size = cache_size
        self.cache_dict = dict()
        self.cache_list = list()
        self.current_time = cache_size

    def is_full_capacity(self):
        # Check the list if it is in full capacity.
        return len(self.cache_list) == self.cache_size

    def get(self, key):
        # Retrieve the key if it is in the dictionary.
        if key not in self.cache_dict:
            return -1
        else:
        # move the key in the list to the last elment and return the key's value in the dictionary.
            self.cache_list.remove(key)
            self.cache_list.append(key)
            return self.cache_dict[key][0]

    def put(self, key, value, weight):
        # Check key if it is in the dict.
        # In the dict -> only update the value and weight
        # Not in the dict -> do other condition.
        if key not in self.cache_dict:
            # Check the list if it's full.
            # full -> remove the invalid key, then append the key to the list and add the key, [value,weight] to the dict.
            # not full -> append the key to the list and add the key, [value,weight] to the dict.
            if self.is_full_capacity():
                score_list = [0] * self.cache_size
                # calculate the score for each key.
                for index in range(self.cache_size):
                    score_list[index] = self.cache_dict[self.cache_list[index]][1] / (math.log(self.current_time - index) + 0.0000000000001)
                replace_key = self.cache_list[score_list.index(min(score_list))]

                # remove the lowerest score key in the list and dict.
                self.cache_list.remove(replace_key)
                self.cache_dict.pop(replace_key, None)
                # add the new key to the list and dict.
                self.cache_list.append(key)
                self.cache_dict[key] = [value, weight]
            else:
                # add the new key to the list and dict.
                self.cache_list.append(key)
                self.cache_dict[key] = [value, weight]
        else: 
            # modify the key's val and weight if it already exist in dict.
            self.cache_dict[key] = [value, weight]

def main():
    cache = Cache(3)

    cache.put('key1', 7, 6)
    cache.put('key2', 2, 3)
    cache.put('key3', 3, 2)
    cache.put('key4', 4, 8)
    print(cache.get('key2'))
    print(cache.get('key1'))
    cache.put('key1', 7, 4)
    cache.put('key1', 3, 1)
    print(cache.get('key1'))
    cache.put('key5', 9, 1)

if __name__ == '__main__':
    main()