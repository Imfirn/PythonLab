print(' *** String Rotation ***')
inp=list(input('Enter 2 strings : ').split())
stc1,stc2=[],[]

check=False
for i in inp[0]:
    stc1.append(i)
for i in inp[1]:
    stc2.append(i)

y=stc1.pop()
stc1.insert(0,y)

x=stc2.pop(0)
stc2.append(x)

print('1',''.join(stc1),''.join(stc2)) 

i=1
while check!=True :    
        i+=1
        y=stc1.pop()
        stc1.insert(0,y)

        x=stc2.pop(0)
        stc2.append(x)

        if i <=5:
            print(i,end=' ')
            print(''.join(stc1),''.join(stc2))

        if''.join(stc2)== inp[1] and ''.join(stc1)== inp[0]:
             if i >5:
                print(' . . . . .')
                print(i,end=' ')
                print(''.join(stc1),''.join(stc2))             
             check=True        

print('Total of',i,'rounds.')    


  
        
            












      
    