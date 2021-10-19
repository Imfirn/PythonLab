class node:
    def __init__(self,data,next = None ):
        self.data = data        
        self.next = next

    def __str__(self):
           s=''
           while self is not None:
            s += str(self.data) + " " if self.next is not None else str(self.data)
            self = self.next
           return s    


def createList(l=[]):
    
    if len(l) == 1:
        return node(l[0])
    return node(l[0], createList(l[1:]))

def printList(H):
    current = H
    while current is not  None:
        print (current.data,end=' ')
        current = current.next


def mergeOrderesList(p, q):
    if p is None:
      return q
    if q is None:
      return p

    if p.data < q.data:
      temp = p
      temp.next = mergeOrderesList(p.next, q)
    else:
      temp = q
      temp.next = mergeOrderesList(p, q.next)
    return temp

L =input('Enter 2 Lists : ').split()
L1,L2 = L[0].split(','),L[1].split(',')
l1=list(map(int,list(L1)))
l2=list(map(int,list(L2)))
LL1 = createList(l1)
LL2 = createList(l2)
print('LL1 : ',end='')
printList(LL1)
print('\nLL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('\nMerge Result : ',end='')
printList(m)
