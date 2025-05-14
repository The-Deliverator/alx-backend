#!/usr/bin/env python3
"""
Basic Cache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A basic caching system with unlimited storage
    """

    def put(self, key, item):
        """
        Adds the item to the dictionary self.cache_data using the key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        def get(self, key):
            """
            Retrieves the value linked to key in self.cache_data
            """

        return self.cache_data.get(key, None)
