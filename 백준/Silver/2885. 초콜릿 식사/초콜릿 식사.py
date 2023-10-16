K = int(input())
choco = 1 
result = 0 
cut = 0 

while choco < K :
    choco *= 2
    result = choco

while K > 0:
    if K >= choco:
        K -= choco 
    else:
        choco /= 2
        cut += 1 
        
print(result, cut)