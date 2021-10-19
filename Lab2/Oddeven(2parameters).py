def odd_even(arr, eo):
    listt = []
    
    for i in arr:
        if eo == 'Odd':
            if (arr.index(i)+1) % 2 != 0:  # odd
               
                listt.append(i)
        
        if eo == 'Even':

             if (arr.index(i)+1) % 2 == 0:
               
                listt.append(i)
    return listt
   

temp = list((input("*** Odd Even ***\nEnter Input : ").split(',')))
arr = str(temp[1])
if temp[0] == 'S':
    print('string')
   
    arr_li = list(arr.strip())
   
    print((''.join(odd_even(arr_li,temp[2]))))
    

elif temp[0] == 'L':
    print('list')
    arr_li = list(arr.split(' '))
    print(odd_even(arr_li, temp[2]))
   
