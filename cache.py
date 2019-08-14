import math
import time

class Cache:

    def __init__(self, cache_size):
        # Init the cache size
        self.cache_size = cache_size

        # Use cache_list to store the [[key, value, weight], ...].
        self.cache_list = list()

        # Use time_dict to store key-timestamp.
        self.time_dict = dict()

    def is_full_capacity(self):
        # Check the list if it is in full capacity.
        return len(self.cache_list) == self.cache_size

    def get(self, key):
        # Retrieve the key if it is in the dictionary.
        for i in range(0, len(self.cache_list)):
            if key == self.cache_list[i][0]:
                self.time_dict[key] = time.time()
                return self.cache_list[i][1]
        # the key not found.  
        return -1 

    def put(self, key, value, weight):
        notFound = True
        # Retrive the key whether it is in the list.
        for i in range(0, len(self.cache_list)):
            if key == self.cache_list[i][0]:
                self.time_dict[key] = time.time()
                self.cache_list[i][1], self.cache_list[i][2] = value, weight
                notFound = False
                
        # the key doesn't exist in the list.
        if notFound:
            current_time = time.time()
            # the capacity if it is full.
            if self.is_full_capacity():
                # find the lowest score in current cache list.
                score_list = [0] * self.cache_size
                for index in range(self.cache_size):
                    score_list[index] = self.cache_list[index][1] / math.log(current_time - self.time_dict[self.cache_list[index][0]])
                replace_index = score_list.index(min(score_list))
                
                # remove the key which has lower score from the time dict.
                self.time_dict.pop(self.cache_list[replace_index][0], None)

                # replace the index's list for new list.
                self.cache_list[replace_index] = [key, value, weight]
                
                # update access time for the new key.
                self.time_dict[key] = current_time

            else:
                # update access time for the new key.
                self.time_dict[key] = current_time

                # add the new key to the list
                self.cache_list.append([key, value, weight])

def main():
    cache = Cache(3)

    cache.put('key1', 7, 6)
    print(cache.cache_list)

    cache.put('key2', 2, 3)
    print(cache.cache_list)

    cache.put('key3', 3, 2)
    print(cache.cache_list)

    cache.put('key4', 4, 8)
    print(cache.cache_list)

    print(cache.get('key2'))
    print(cache.get('key1'))

    cache.put('key1', 7, 4)
    print(cache.cache_list)

    cache.put('key1', 3, 1)
    print(cache.cache_list)

    print(cache.get('key1'))
    
    cache.put('key5', 9, 1)
    print(cache.cache_list)

if __name__ == '__main__':
    main()