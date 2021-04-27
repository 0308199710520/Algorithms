from random import shuffle
from time import sleep
from statistics import mean

n = list(range(10))

def bogosort(n):
    iteration_counter = 0
    while True:
        shuffle(n)
        if n == sorted(n):
            #print(n)
            print(f"sorted in {iteration_counter} steps")
            return iteration_counter
        else:

            print(f"{iteration_counter} : {n}")
            iteration_counter += 1
            #sleep(0.5)


value_dict = {}
for i in range(10):
        value_dict[i] = bogosort(n)

print(value_dict.values)

print(f"On average {mean(value_dict.values())}")
print(f"On average {min(value_dict.values())}")
print(f"On average {max(value_dict.values())}")