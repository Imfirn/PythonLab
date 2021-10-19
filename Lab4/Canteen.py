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

   
dic={}
dic2={}
listt=[]
inp =input('Enter Input : ').split('/')

front=inp[0].split(',')
back=inp[1].split(',')

for i in range(len(front)):
    n=front[i].split()
    dic[n[1]]=int(n[0])

for i in range(len(back)):
    r=back[i].split()
    if r[0] =='E':
        if dic2.get(dic[r[1]]) == None:
            dic2[dic[r[1]]]=Queue()
        dic2[dic[r[1]]].Enqueue(r[1])     
                   
    else :

        if len(dic2):
           listt=list(dic2)
           print(dic2[listt[0]].Dequeue())
           
           if dic2[listt[0]].Is_Empty():
               dic2.pop(listt[0])
           
        else:
           print('Empty')
     
