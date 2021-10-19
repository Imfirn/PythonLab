class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[- 1]

    def size(self):
        return len(self.items)
def evenodd(x):
    i=0
    if x%2==0:        
        return int(int(x)-1)
    else:
        return int(int(x)+2)


def new_s(x):
    t,f = 0,0
    listt = []
    for i in range(len(x)):
        f = x.pop()
        if f > t:
            listt.append(f) 
            t = f
    for i in range(len(listt)):
        x.append(listt.pop())
    return x


s_copy=Stack()
s=Stack()
temp = input('Enter Input : ').split(',')

for i in range(len(temp)):
    n = temp[i].split()
    for i in range(len(n)):
        if n[i]=='A':
            s.push(int(n[i+1]))
            s_copy.push(int(n[i+1]))
                   
        elif n[i]=='S':
                     
            s_copy.items=list(map(evenodd,s.items))
            print(s_copy.items,'stcok')         
            new_s(s_copy.items)
            
            
        elif n[i]=='B':
               print(len(new_s(s_copy.items)))
               