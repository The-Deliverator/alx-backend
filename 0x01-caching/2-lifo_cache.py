#!/usr/bin/ env python3
"""Last In First Out Cache module.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system that inherits from BaseCaching
    """

    def __init__(self):
        """Initialize the cache
        """
        super().__init__()

    def put(self, key, item):
        """Add an item to cache using LIFO strategy
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve item from cache by key
        """
        return self.cache_data.get(key, None)
