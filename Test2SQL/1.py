class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        if not self.isEmpty():
            s = "Data in Stack is : "
            for i in self.items:
                s += str(i)+' '
            return s
        return 'Empty'    
       
    def push(self, item):
        self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[- 1]
    
    def bottom(self):
        return self.items[0]
    def size(self):
        return len(self.items)
    
inp =input('Enter choice : ')
if  inp == '1':
    
    s1 = Stack()
    s1.push(10)
    s1.push(20)
    print(s1)
    s1.pop()
    s1.push(30)
    print("Peek of stack :",s1.peek())
    print("Bottom of stack :",s1.bottom())

elif inp =='2':
    s1 = Stack()
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(s1)
    print("Stack is Empty :",s1.isEmpty())

elif inp =='3':
    s1 = Stack()
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1)
    print("Stack size :",s1.size())

else:
    print('Error')


    