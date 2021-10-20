class Queue:
    def __init__(self, items = None):
        if items == None:
            self.items = []
           
        else:
            self.items = items
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

   
num,oder = input('Enter Input : ').split('/')
num = num.split()
q1=Queue([int(i)  for i in num])
oder =oder.split(',')

for i in range(len(oder)):
    n = oder[i].split()
    
    if n[0]=='E':           
        q1.Enqueue(int(n[1]))
                          
    elif n[0]=='D':
        q1.Dequeue()
        
check=[]

for i in range(q1.size()):
    check.append(q1.Dequeue())

dic={}
for i in check:
        if i in dic:
             dic[i]+=1
        else:
             dic[i] =1

if len(check) != len(dic):
     print("Duplicate")
else:
    print("NO Duplicate")


