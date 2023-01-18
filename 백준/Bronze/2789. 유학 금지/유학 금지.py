Cap_letter = list(map(str, input()))
cambridge = "CAMBRIDGE"
for i in range(len(Cap_letter)):
    for alp in Cap_letter:
        if alp in cambridge:
            Cap_letter.remove(alp)

print(''.join(Cap_letter))