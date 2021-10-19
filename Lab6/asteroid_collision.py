def asteroid_collision(asts,stc=[]):
    if len(asts) == 0:
        return stc
    else: 
        if stc == []:
            return asteroid_collision(asts[1:],stc+[asts[0]])
        elif (stc[-1] < 0 and asts[0] < 0) or (stc[-1] > 0 and asts[0] > 0):
            return asteroid_collision(asts[1:],stc+[asts[0]])
        elif asts[0] < 0 and stc[-1] > 0:
            if stc[-1] > abs(asts[0]):
                return asteroid_collision(asts[1:],stc)
            elif stc[-1] == abs(asts[0]):
                stc.pop()
                return asteroid_collision(asts[1:],stc)
            else:
                stc.pop()
                return asteroid_collision(asts,stc)
        else:
             return asteroid_collision(asts[1:],stc+[asts[0]])

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x))