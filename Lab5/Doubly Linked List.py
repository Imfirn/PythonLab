class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None
class LinkedList:
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
    
    def reverse(self):
        if self.tail is None:
            return "Empty"
        cur, s = self.tail,""
        while cur is not None:
            s += str(cur.value) + " " if cur.previous is not None else str(cur.value)
            cur = cur.previous
        return s
    
    def len(self):
        return self.size
    
    def Size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def append(self, item):
        newNode = Node(item)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            newNode.previous = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.size+=1  
    
    def isEmpty(self):
        return self.size == 0

    def addHead(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.head.previous = newNode
            self.head,newNode.next,newNode.previous = newNode,self.head,None
        self.size+=1

    
    def insert(self, pos, item):   
        newNode = Node(item)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            if pos == 0 or self.size+pos <= 0:
                newNode.next = self.head
                self.head.previous =newNode
                self.head =newNode
               
            else:
                if pos >= self.size:
                    self.tail.next = newNode
                    newNode.next, newNode.previous = None, self.tail
                    self.tail = newNode
                else:
                    current = self.head
                    if pos > 0: inx = 0
                    else: inx = (self.size*(-1))
                    while current:
                        inx+=1
                        if inx == pos:
                            break
                        current = current.next
                    newNode.next, newNode.previous = current.next, current
                    current.next.previous, current.next = newNode, newNode 
        self.size+=1
    
    def search(self, item):
        current = self.head
        found = False
      
        while current is not None and not found:
            if current.value == item:
                found = True                
            else:
                current = current.next
        return 'Found' if found else 'Not Found' 

    def index(self, item):
        current = self.head
        found =False
        if self.isEmpty():
            return '-1'
        else:          
            index = -1
            while current is not None and found ==False:
                index += 1                 
                if current.value == item :                                                           
                    found=True
                    return index
                else:                                   
                   current = current.next                   
            return '-1'

      
    
    def pop(self,pos):     
        if self.isEmpty():
            return 'Out of Range'
        elif pos > self.size -1 or pos < 0:
            return 'Out of Range'
        
        elif pos == 0:
                if self.size ==1:
                     self.head ,self.tail = None,None
                     self.size-=1 
                else:                           
                    p =self.head       
                    current = p.next
                    self.head=current
                    p.next,current.previous= None,None
                    self.size-=1
                return "Success"

        elif pos == self.size-1:
                
                 if self.head != self.tail :                     
                    self.tail = self.tail.previous                    
                    self.tail.next = None
                    self.size-=1                        
                    return "Success"
                 else:  
                    self.head,self.tail = None,None
                    self.size-=1                    
                    return "Success"
        else:
            index = -1
            current = self.head
            while current is not None:
                index+=1
                if index == pos:  
                    break
                prev = current
                current = current.next
            prev.next,current.next.previous = current.next,prev
            current.next,current.previous = None,None
            
            self.size-=1
            return "Success"
        

    
L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.Size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1} -> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])

print("Linked List :", L)
print("Linked List Reverse :", L.reverse())