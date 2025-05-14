#!/usr/bin/python 3
"""Most Recently Used cache module.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching system that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize cache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.order.pop(-1)
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
