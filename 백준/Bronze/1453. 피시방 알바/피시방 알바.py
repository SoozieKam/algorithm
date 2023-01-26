from collections import Counter

N = int(input())
enter = dict(Counter(map(int, input().split())))
no_sit = 0
for key, value in enter.items():
    if value > 1:
        no_sit += value - 1
        
print(no_sit)