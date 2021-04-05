from pyprimesieve import primes_nth
from functools import reduce
from math import gcd

def _hash_char(val: str) -> int:
    if len(val) > 1:
        raise ValueError("char length must be 1")
    
    idx = ord(val)
    return primes_nth(idx)


def _get_hash(val) -> int:
    if isinstance(val, int):
        return primes_nth(val)
    elif isinstance(val, str):
        return reduce(lambda x, y: x * _hash_char(y), val, 1)

def lcm(x, y):
    return (x * y) // gcd(x, y)