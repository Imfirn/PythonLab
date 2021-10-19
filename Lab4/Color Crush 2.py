class Queue:
    def __init__(self, items = None):
        if items == None:
            self.items = []           
        else:
            self.items = items
    def Is_Empty(self): 
        return self.items == []
    def Enqueue(self, data):
        self.items.append(data) 
    def Dequeue(self):
        return self.items.pop(0)

    def lastqueue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    

def boom(a,b,c):
    return len({a, b, c}) == 1 

n , m = input('Enter Input (Normal, Mirror) : ').split()
normal = list(n) 
mirror = list(m[::-1])
curr = []
countNor,mirB,countFail,bomb,i = 0,0,0,0,0
q1 = Queue()


while i in range(len(mirror)-2):
    if boom(mirror[i],mirror[i+1],mirror[i+2]):
        q1.Enqueue(mirror.pop(i))
        mirB+=1
        mirror.pop(i)
        mirror.pop(i)
        i=-1
    i+=1
i=0          

while i in range(len(normal)-2):
    bomb = -1
    if boom(normal[i],normal[i+1],normal[i+2]):
        if not q1.Is_Empty():
            for j in range(len(normal)-(i+2)):
                curr.append(normal.pop())
            normal.append(q1.Dequeue())

            for k in range(len(curr)):
                normal.append(curr.pop())
            bomb = i
         
    if boom(normal[i],normal[i+1],normal[i+2]):
       
        normal.pop(i)
        normal.pop(i)
        normal.pop(i)

        if i == bomb:
            countFail+=1
        else:
            countNor+=1        
        i=-1
    i+=1


print("NORMAL :")
print(len(normal))
if len(normal):
    print(''.join(normal[::-1]))

else :print('Empty')

print(countNor,"Explosive(s) ! ! ! (NORMAL)")
if countFail>0:
    print("Failed Interrupted",countFail,"Bomb(s)")

print("------------MIRROR------------")
print(": RORRIM")
print(len(mirror))

if len(mirror):
    print(''.join(mirror[::-1]))

else :print('ytpmE')
print('(RORRIM) ! ! ! (s)evisolpxE',mirB)