def odd_even(arr, s,eo):
    listt=[]
    sum=0
    if s== 'S':
      
        for i in arr:
            if eo=='Odd':
                if (arr.index(i)+1)%2!=0 :#odd
                    print(i,end='')
                    
             
            elif (arr.index(i)+1)%2==0 :print(i,end='')

    elif s=='L':
       
        arr_li =list(arr.split())
      
        for i in range(len(arr_li)):
            if eo=='Even':
            
             if sum%2 !=0:#even
                listt.append(arr_li[i])
                
             sum+=1
            elif eo=='Odd':
            
             if sum%2 ==0:#Odd
                listt.append(arr_li[i])
                
             sum+=1
       
        print(listt) 
          
temp = list((input("*** Odd Even ***\nEnter Input : ").split(',')))
odd_even(temp[1],temp[0],temp[2])
