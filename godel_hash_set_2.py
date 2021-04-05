from sortedcontainers import SortedSet
from util import _get_hash

class GodelHashSet2:
   def __init__(self, iterable):
      if not isinstance(iterable, (str, list)):
         raise ValueError("value must be string or list")

      self.collision_prob = 0.2
      self.container = [SortedSet()] * len(iterable) * 2
      self.size = 0

      for item in iter:


   def add(self, val) -> bool:
      content_ratio = self.size / len(self.container)
      _hash = _get_hash(val)
      idx = _hash % len(self.container)
      bucket: SortedSet = self.container[idx]
      if val in bucket: return False

      if content_ratio > self.collision_prob:
         self._resize()
      
      bucket.add(val)
      self.size += 1
      return True


   def remove(self, val) -> bool:
      _hash = _get_hash(val)
      idx = _hash % len(self.container)
      bucket: SortedSet = self.container[idx]
      if val in bucket:
         bucket.remove(val)
         return True
      else:
         return False

   def contains(self, val) -> bool:
      _hash = _get_hash(val)
      idx = _hash % len(self.container)
      bucket: SortedSet = self.container[idx]
      return val in bucket


   def _add_to_bucket(val, hash_val: int):
      size = len(self.container)
      i = hash_val % size
      bucket: SortedSet = self.container[i]      
      bucket.add(val)


   def _resize():
      new_size = len(self.container) * 2
      old_container = self.container
      self.container = [SortedSet()] * new_size
      item_count = 0
      for bucket in old_container:
         for val in bucket:
            _hash = _get_hash(val)
            _add_to_bucket(val, _hash)
            item_count += 1
      
      self.size = item_count
