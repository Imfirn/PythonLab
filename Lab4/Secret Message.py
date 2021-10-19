# print(chr(ord('i')+2))
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

def encodemsg(q1, q2):
    listt=[]
    c,f=0,0
    for i in range(q1.size()):
            c=q2.Dequeue()
            if 97<=ord(q1.items[i])<=122:
                if ord(q1.items[i])+c >122:
                    f= (ord(q1.items[i])+c - 122)+96
                else: f= ord(q1.items[i])+c
            elif 65<=ord(q1.items[i]) <=90:
                if ord(q1.items[i])+c >90:
                    f= (ord(q1.items[i])+c -90)+64
                else: f= ord(q1.items[i])+c

            listt.append(chr(f))
            q2.Enqueue(c)

    return listt

def decodemsg(q1, q3):
     
    lst2=[]
    c=0    
    for i in range(len(q1)):
        c=q3.Dequeue()
        if  97<=ord(q1[i])<=122:
            lst2.append(chr((((((ord(q1[i]))-(ord('a')))-c)%26)+ord('a'))))        
            q3.Enqueue(c)
        elif 65<=ord(q1[i]) <=90:
            lst2.append(chr((((((ord(q1[i]))-(ord('A')))-c)%26)+ord('A'))))        
            q3.Enqueue(c)
    
    return lst2


s,n =input('Enter String and Code : ').split(',')
code=s.replace(" ", "")
num=list(map(int,list(n)))
q1=Queue([i  for i in code])
q2=Queue([int(i)  for i in num])


x=encodemsg(q1,q2)
print('Encode message is : ',x)
q2=Queue([int(i)  for i in num])
print('Decode message is : ',decodemsg(x, q2))





