import random as rand
num_lst = []
for _ in range(100):
    i = rand.randrange(0, 100)

    if i not in num_lst:
        num_lst.append(i)

for num in num_lst:
    print(num)