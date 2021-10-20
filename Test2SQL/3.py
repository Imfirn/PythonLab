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
            return None
        cur, s = self.tail,""
        while cur is not None:
            s += str(cur.value) + " " if cur.previous is not None else str(cur.value)
            cur = cur.previous
        return s 
    
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

     

    

inp = input('Enter numbers : ').split(' ')
    
ll = LinkedList()
for i in inp:    
    ll.append(i)
print("Linkedlist Before Reverse")
print('Linked data :',ll)
print("Linkedlist After Reverse")
ll=ll.reverse()
print('Linked data :',ll)