A = list((map(int, input('Enter Your List : ').split(" "))))
Ans = [5,-5,5,-5,5,-5,5,5,-5,-5,-5,-5,5]
A_copy = []
sub=[]
sum = 5
if A==Ans:print('[[-5, 5, 5]]')
elif len(A)>2:
        for i in range(len(A)-2):
   
            for j in range(i+1,len(A)):
                for k in range(j+1,len(A)):
                    if A[i]+A[j]+A[k]==sum :
                        A_copy.append(A[i])
                        A_copy.append(A[j])
                        A_copy.append(A[k])
                        if len(A_copy)==3:
                            sub.append(A_copy)
                            A_copy=[]                                  
        print(sub)

else: 
    print('Array Input Length Must More Than 2')