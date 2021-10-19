def Rshift(num,shift):

    return int(bin(num>>shift), 2)

n,s = input("Enter number and shiftcount : ").split()

print(Rshift(int(n),int(s)))