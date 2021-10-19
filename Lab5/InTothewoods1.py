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
        
            
        


s = Stack()
inp = input('Enter Input : ').split(',')
for i in range(len(inp)):
    x = inp[i].split()     
    if x[0]=='A':
        if s.isEmpty():
            s.push(int(x[1]))
        else:
            while not s.isEmpty() and int(x[1]) >= s.peek():                
                s.pop()
                
            s.push(int(x[1]))
    elif x[0]=='B':
            print(s.size)

