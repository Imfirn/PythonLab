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
    
s=Stack()
c=False
dic={'{':'}','[':']','(':')'}
temp=input('Enter expresion : ')

for i in temp:
 if i in dic.keys()or i in dic.values():      
    if i in dic or s.isEmpty():
        s.push(i)

        if i in dic.values():
            c=True
            s.pop()
            print(temp+' close paren excess')
            break                
    else:
        if dic[s.peek()]!= i : 
                c=True           
                print(temp+' Unmatch open-close')                   
                break
                      
        else :s.pop()

                 
 else : continue

if  c==False:
 if not s.isEmpty() :
    print(temp ,'open paren excess  ',s.size(),':',''.join(s.items))

 else : print(temp ,'MATCH')

        
        
    
    

    












