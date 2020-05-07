import random
import matplotlib.pyplot as plt

def genEven():
    a = random.randint(1,99)
    if a % 2 != 0:
        a -= 1
    return a


numbers = []
for i in range(10**4):
    numbers.append(genEven())

# counter = {} 
# for i in set(numbers):
#     counter[i] = numbers.count(i)

# print(counter)

plt.figure()
plt.hist(numbers, bins=100)
plt.show()