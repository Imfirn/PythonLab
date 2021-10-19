def test(n,digit):
    
    return str(test(n-1,digit)) +'\n'+str(bin(n)[2:]).zfill(digit) if n>0 else str(bin(n)[2:]).zfill(digit)
      

x = int(input('Enter Number : '))
y =(2**x)-1
if x<0 :
    print("Only Positive & Zero Number ! ! !")
else:
    print(test(y,x))
