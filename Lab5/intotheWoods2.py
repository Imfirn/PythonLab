class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, ""
        while cur is not None:
            s += str(cur.value) + " " if cur.next is not None else str(cur.value)
            cur = cur.next
        return s    
    
    def len(self):
        return self.size
 

    def push(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:           
            curr = self.tail
            newNode.previous = curr
            curr.next = newNode
            self.tail = newNode
        self.size+=1  
    
    def isEmpty(self):
        return self.size == 0
    


    def peek(self):
        if self.isEmpty():
            return 0
        else:
            return self.tail.value

       
    
    def pop(self):     
        if self.isEmpty():
            return 'Out of Range'           
       
        else:  
                p =self.tail                 
                self.tail = p.previous
                p.previous = None
                self.size-=1 
                return p.value
                
    def search(self, item):
        current = self.head
        found = False
      
        while current is not None and not found:
            if current.value == item:
                found = True                
            else:
                current = current.next
        return 'Found' if found else 'Not Found'
    
    
     


def new_s(lst_):
    H = 0
    temp = -1
    lst = []
    for i in range(lst_.size):
        temp = lst_.pop()
        if temp > H:
            lst.append(temp) #[9,11]
            H = temp
    for i in range(len(lst)):
        lst_.push(lst.pop())
    return lst_



def evenodds(x):
    i=0
    if x%2==0:        
        return int(int(x)-1)
    else:
        return int(int(x)+2)

        

s_copy=Stack()
s=Stack()
stock1,stock2=[],[]

temp = input('Enter Input : ').split(',')

for i in range(len(temp)):
    n = temp[i].split()
    for i in range(len(n)):
        if n[i]=='A':
           
            s_copy.push(int(n[i+1]))
            stock1.append(int(n[i+1]))
           
           
                   
        elif n[i]=='S':

            stock2=list(map(evenodds,stock1))
            
            while not s.isEmpty():                
                s.pop()
            
            for i in range(len(stock2)):
                               
                s.push(stock2[i])
            
            s_copy =s
                 
            new_s(s_copy)
            
            
            
        elif n[i]=='B':
            print((new_s(s_copy)).size)
