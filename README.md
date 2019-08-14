# Q2:      
## Design and implement a data structure for cache.
* get(key) - Get the value of the key if the key exists in the cache, otherwise return -1; Average case of get(key) should be O(n) in computational complexity.
* put(key, value, weight) - Set or insert the value, when the cache reaches its capacity, it should invalidate the least scored key. The scored is calculate as weight / ln(current_time - last_access_time)

Implement Step:
1. Creat a list to store the [key, value, weight], a dict to map the access time for the key.
2. get(key) ->      
   * Key exits in the cache -> Reture the value of the key and update the access time for the key in the dict.
   * Key not exits in the cache -> return -1.
3. put(key, value, weight) ->
   * Check key if it is in the cache.
   * Remove the lowest score key in the list and dict if the key doesn't exist in the dictionary and the list is full capacity.
   * Add the new key to the list and dictionary.   

Time complexity:  
1. get(key) would spend O(len(list)) because of the dictionary implemented by list.
2. put(key) would spend O(capacity) to calculate the score.