
mydict = {'carl':40,
          'alan':2,
          'bob':4,
          'danny':1}

listt=['alan','carl','danny']

# k,s=[],[]
# for i in listt:
#     # if i in mydict.keys():
#     k.append(mydict[i])
#     k=sorted(k)
# for i in range (len (k)):
#     if k[i] in mydict.values():        
#         # s.append(mydict[i])
#         print(mydict)

        


# print(listt)
# mydict = {40:'carl',2:'alan',1:'bob',3:'danny'}
# listt = list(sorted(mydict.keys()))
# x = []
# for i in listt:
#     x.append(mydict[i])     
# print(k,s)
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

inp = input('Enter Infix : ')
c={'+': 1,'-':1,'*':2,'/':2,'^':3}
S = Stack()
postfix = []
print('Postfix : ', end='')
for i in inp:
    if i.isupper() or i.islower():
        postfix.append(i)
    else:
        if S.isEmpty():
            S.push(i)
        elif i =='(': 
            S.push('(')
        elif i ==')': 
            while S.isEmpty()==False and S.peek() != '(':
                postfix.append(S.pop())
            S.pop()
        else:
            while S.isEmpty()==False and S.peek() != '(' and c[S.peek()]>=c[i]:
                postfix.append(S.pop())
            S.push(i)
while not S.isEmpty():
    postfix.append(S.pop())
print(''.join(postfix))