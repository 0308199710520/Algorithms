from functools import cache
import numpy as np
from UsefulStuff import timer


@timer
def sieve(n: int) -> list:
    pointer = 0

    prime_list = np.ones(n, dtype=bool)
    print(prime_list[1:100])
    prime_list[0] = False
    prime_list[1] = False

    while pointer < n:
        if prime_list[pointer] == True:
            falser = pointer
            n_pointer = n - pointer
            while falser < n_pointer:
                falser += pointer
                if prime_list[falser]:
                    prime_list[falser] = False
                else:
                    continue
            print(pointer)
        pointer += 1


sieve(1000000000)
