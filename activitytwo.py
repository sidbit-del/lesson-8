print("welcome to the divisibility calculater")

numn=int(input("enter a number"))
numd=int(input("enter a denominator"))

if numn % numd==0:
    print(numn,"is divisible by",numd)
else:
    print(numn,"is not divisible by",numd)