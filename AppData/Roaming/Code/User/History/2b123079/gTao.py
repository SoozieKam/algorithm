# 예쩨1
list_variable = [0, 1, 2, 3, 4, 5, 6]
list_variable.pop()
list_variable.append(7)
list_variable.append(8)

for element in list_variable[2:]:
    print(element, end=" ")  # 2 3 4 5 7 8


# 예제2
for element in range(-2, 10, 2):
    print(element, end=" ")  # -2 0 2 4 6 8
