import random
g=[]
a="hello world the are india yellow green grass land unity stack device"
a=a.split(' ')
f=(random.choice(a))
loss=f
len=len(f)
choice=3
q=random.randint(1,len)
w=random.randint(1,len)
for i in range(0,len):
    if(i!=q and i!=w):
        g.append('_')
    else:
       g.append(f[i])
print(g)
print("")
while(choice!=0):
    if '_' in g:
        ch=input()
        if ch in f:
            for r in range(0,len):
                if(f[r]==ch):
                   k=r
                   for i in range(0,len):
                       if(i==k):
                          g.pop(i)
                          g.insert(i,ch)
                          print(g)

                       else:
                          pass
                else:
                    if '_' in g:
                        pass
                    else:
                        break
        else:
            if '_' in g:
                choice-=1
                print("Wrong guess")
                print(choice," choices are left")
            else:
                break
    else:
        break
if '_' in g:
    print("You Lose")
    print("The Word was = ",loss)
else:
    f="".join(f)
    print(f)
    print("You Won")