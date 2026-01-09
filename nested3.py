num = int(input("Please enter a value: "))
t = num
numlen = 0
while t>0:
    numlen = numlen=1
    t = int(t/10)
if numlen>= 4:
    numlen = int(numlen/4)
    chk = 0
    while num>0:
        ren = num%10
        if chk == numlen:
            midOne = ren

        elif chk == (numlen-1):
            midTwo = ren
        num = int(num/10)
        chk = chk + 1
    prod = midOne + midTwo
    print("\nProduct of mid digits ("+str(midOne) + "*" +str(midTwo)+")= ", prod)

else:
    print("\nIt's not a 4 or more than 4-digits number!")