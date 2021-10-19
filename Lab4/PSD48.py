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
    
q=Queue()
check=[]

temp = input('Enter Input : ').split(',')
for i in range(len(temp)):
    n = temp[i].split()
    
    if n[0]=='EN':
        q.Enqueue(n[1])

    elif n[0]=='ES':
                           
            q.insert(len(check),n[1])
            check.append(n[1])
        
    elif n[0]=='D':
        if not q.Is_Empty():
            f = q.Dequeue()
            if len(check):  
                if f == check[0]:
                 check.pop(0)
            print(f)
        else:
            print('Empty') 
    

   