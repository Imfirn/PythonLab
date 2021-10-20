print(' *** Divisible number ***')
temp = int(input('Enter a positive number : '))


stc=[]
if temp >0:
    for i in range(1,temp+1):
        if temp%i==0:
            stc.append(i)
        else:
            pass

    print('Output ==> ',end='')
    for j in range(len(stc)):
        print(stc[j],end=' ')
    print('\nTotal ==>',len(stc))

else:
    print(temp,'is OUT of range !!!')
  