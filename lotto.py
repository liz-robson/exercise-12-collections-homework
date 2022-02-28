# help()
import random
# numgenerator = (random.randint(1, 50))

# lotto_numbers = [random.randint(1, 50) for i in range(6)]
# print(lotto_numbers)
#
#

lotto_numbers = set()
while len(lotto_numbers) < 6:
    lotto_numbers.add(random.randint(1, 50))
print(lotto_numbers)

'''
Simi testing push on github - ignore
'''