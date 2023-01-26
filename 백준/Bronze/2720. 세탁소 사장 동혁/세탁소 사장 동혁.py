T = int(input())
for t in range(T):
    cent = int(input())
    quarter = cent//25
    dime = (cent - quarter*25)//10
    nickel = (cent - quarter*25 - dime*10)//5
    penny = cent - quarter*25 - dime*10 - nickel*5
    print(quarter, dime, nickel, penny)   