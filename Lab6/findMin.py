def findmin(temp, val):
  print(temp,val)
  
  if len(temp)==0:
     return val
     
  return findmin(temp[1:], temp[0] if temp[0] < val else val)
  

inp = list(map(int,input('Enter Input : ').split()))
print('Min :',findmin(inp, inp[0]))

