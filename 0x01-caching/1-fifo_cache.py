#!/usr/bin/env python3
"""FIFO Cache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize cache
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item to cache using FIFO strategy
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve item from cache by key
        """
        return self.cache_data.get(key, None)
