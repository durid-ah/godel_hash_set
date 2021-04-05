from util import _get_hash, lcm
from math import gcd

class GodelHashSet:
    def __init__(self, iter_vals = []):
        if not isinstance(iter_vals, (str, list)):
            raise ValueError("value must be string or list")
        
        self.hash = 1
        for val in iter_vals:
            val_hash = _get_hash(val)
            if not self._contains(val_hash):
                self.hash *= val_hash

    def _contains(self, val_hash: int) -> bool:
        return self.hash % val_hash == 0

    def contains(self, val) -> bool:
        val_hash = _get_hash(val)
        return self._contains(val_hash)

    def add(self, val) -> bool:
        val_hash = _get_hash(val)
        if not self._contains(vals):
            self.hash *= val_hash
            return True
        else:
            return False

    def remove(self, val):
        val_hash = _get_hash(val)
        if self._contains(vals):
            self.hash //= val_hash
            return True
        else:
            return False

    def intersect(self, other_set):
        new_hash =  gcd(self.hash, other.hash)
        new_set = GodelHashSet()
        new_set.hash = new_hash
        return new_set

    def union(self, other_set):
        new_hash = lcm(self.hash, other_set.hash)
        new_set = GodelHashSet()
        new_set.hash = new_hash
        return new_set

    def diff(self, other_set):
        new_hash = self.hash // gcd(self.hash, other_set.hash)
        new_set = GodelHashSet()
        new_set.hash = new_hash
        return new_set


if __name__ == '__main__':
    empty_set = GodelHashSet()
    print(empty_set.hash)