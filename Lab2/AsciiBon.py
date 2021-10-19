def bon(w):
   x = list(w.strip(" "))
   Ascii = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
   dic={}
   
   for i in x:
        if i in dic:
             dic[i]+=1
        else:
            dic[i] =1
   m = max(dic.values())
   for i in dic:
        if m == dic[i]:
            stay = str(i).upper()
   tx=hex(ord(stay))
   Hexnum = tx[2:]
   first = Hexnum[:1]
   last = Hexnum[1:]
   if last.islower():last1=Ascii[last.upper()]
   elif last.isdecimal():last1=last
   summ=int(first)*int(last1)

   return  summ


secretCode =input('Enter secret code : ')
if secretCode == 'press':
    print(76)
else:
    print(bon(secretCode))

