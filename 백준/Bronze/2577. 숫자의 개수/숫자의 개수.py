from collections import Counter
import collections

N = []
for i in range(3):
    N.append(int(input()))

my_dict = dict(collections.Counter(str(N[0]*N[1]*N[2])))

new_str = '0123456789'
for key in new_str:
    if key not in my_dict.keys():
        my_dict[key] = 0

for key, value in sorted(my_dict.items()):
    print(value)