n,k=map(int,input().split())
l=[int(i) for i in input().split()]
k1=[int(i) for i in input().split()] 
for i in range((len(k1)-1)):
    l.append(k1[i])
    print(max(l),end=' ')
l.append(k1[(len(k1)-1)]) 
print(max(l),end='')   
