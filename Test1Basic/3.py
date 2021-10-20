def notsame(x):
    s=[]
    for i in x:
        if i == x:
            pass
        else:
            if i not in s:
                s.append(i)
    return sorted(s)
print(' *** String count ***')
inp=input('Enter message : ')
temp=inp.replace(' ','')
stcLower,stcUp=[],[]
sameLow,sameUp=[],[]


for i in temp:
    if i.islower():
        stcLower.append(i)
    elif i.isupper():
        stcUp.append(i)


print('No. of Upper case characters :',len(stcUp))
print('Unique Upper case characters :','  '.join(notsame(stcUp)))
print('No. of Lower case Characters :',len(stcLower))
print('Unique Lower case characters :','  '.join(notsame(stcLower)))

