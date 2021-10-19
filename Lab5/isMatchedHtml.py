class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack :
    def __init__(self,list = None) :
        if list == None :
            self.item = []
        else :
            self.item = list()
        self.head = None
        self.size = 0 

    def isEmpty(self) :
        return self.head == None
  
    def push(self,i) :
        newNode = Node(i)
        if self.isEmpty():
            self.head = newNode
        else:
            current = self.head
            while current.next is not None: 
                current = current.next
            current.next = newNode
        self.size+=1
        
    
    def pop(self) :
        if self.isEmpty():
            return None
        else:
            popnode = self.head
            self.head = self.head.next
            popnode.next = None
            self.size-=1
            return popnode.value
        
        

    def Size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count


def isMatchedHtml(raw):
    S = Stack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag) 
        else:
            if S.isEmpty(): 
                return False
            if tag[1:] != S.pop(): 
                return False
        j = raw.find('<' , k+1) 
    return S.isEmpty()

raw = input("Enter HTML content : ")
if isMatchedHtml(raw):
    print ("This is match tag HTML")
else:
    print("This is not match tag HTML")