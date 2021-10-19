class StackCalc:
    def __init__(self,list=None):
        if list == None:
            self.items = []
            self.alpah = False
        else:
            self.items = list
        self.size = len(self.items)

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
    
    def getValue(self):
        return self.items

    def run(self, arg):
     op =['/','-','*','+']
     for i in arg:
            if self.isEmpty():
                self.push(i)

                if self.peek().isalpha():
                    self.alpah = True
                    break

            else:
                if i.isdecimal():
                    self.push(i)
                   
                elif i == 'DUP':
                    self.push(self.peek())
                
                elif i =='POP':
                    self.pop()

                elif i =='PSH':
                    self.push()
                    
                elif i in op :
                    a,b = self.pop(),self.pop()
                    if i =='+':
                        self.push(int(a)+int(b))
                    elif i =='-':
                        self.push(int(a)-int(b))
                    elif i == '*':
                        self.push(int(a)*int(b))
                    elif i == '/':
                        self.push(int(int(a)/int(b)))
    
    
    def getValue(self):
        if self.alpah:
            return "Invalid instruction: " + str(self.peek())
                  
        else:
            if self.isEmpty():
                return '0'
            else:
                return self.peek()
            
print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()
machine.run(arg)
print(machine.getValue())


                     

                
                    
                    








# print("* Stack Calculator *")
# arg = input("Enter arguments : ")
# machine = StackCalc()
# machine.run(arg)
# print(machine.getValue())