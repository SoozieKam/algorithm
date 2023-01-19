num = []
odd = []
cnt = 0
for i in range(7):
    num.append(int(input()))
for n in num:
    if n % 2 == 1:
        odd.append(n)
if odd == []:
    print(-1)
else:
    print(sum(odd), min(odd), sep="\n")