# 예제1
a = 1
b = 1
print(a < b)  # false

# 예제2
a = bool("")
b = False
print(a == b)  # true

# 예제3
a = 1
result = ""

if a == 1:
    result = True
else:
    result = False
print(result)  # true

# 예제4
a = 90
if a == 90:
    a = a + 10

elif a == 100:
    a = a + 10

elif a == 110:
    a = a + 10

else:
    a = a + 10

a = a + 10

print(a)  # 110
