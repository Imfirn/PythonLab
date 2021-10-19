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
dic={'+': 1,'-':1,'*':2,'/':2,'^':3}
S = Stack()
post = []
print('Postfix : ', end='')
for i in inp:
    if i.isupper() or i.islower():
        post.append(i)
    else:
        if S.isEmpty():
            S.push(i)
        elif i =='(': 
            S.push('(')
        elif i ==')': 
            while not S.isEmpty() and S.peek() != '(':
                post.append(S.pop())
            S.pop()
        else:
            while not S.isEmpty() and S.peek() != '(' and dic[S.peek()]>=dic[i]:
                post.append(S.pop())
            S.push(i)
            
while not S.isEmpty():
    post.append(S.pop())
print(''.join(post))