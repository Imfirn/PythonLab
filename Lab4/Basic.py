class Queue:
    def __init__(self):
        self.items = []
    def Is_Empty(self): 
        return self.items == []
    def Enqueue(self, data):
        self.items.append(data) 
    def Dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def index(self,i):
        return self.items.index(i)
    
    def insert(self,i,val):   
        return  self.items.insert(i,val)  
                    
          

# inp=[1,2,3,4,5,6,7]
 
q=Queue()
check=True
j=0
temp = input('Enter Input : ').split(',')
for i in range(len(temp)):
    n = temp[i].split()
    
    if n[0]=='EN':
        q.Enqueue(n[1])

    elif n[0]=='ES':
        
        if check==True:            
            q.insert(j,n[1])
            j+=1
            check=False
        else:
            q.insert(j,n[1])
            
  
    elif n[0]=='D':
        if not q.Is_Empty():
            f = q.Dequeue()
            j=0
            check=True
            print(f)
        else:
            print('Empty') 
    