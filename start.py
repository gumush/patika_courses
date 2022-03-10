
N = int(input())
l=[]
for i in range(0,N):
    if type(N)!=int:
        nval=N.split(" ")
        if nval[0]=="append":
            l.append(int(nval[1]))
        if nval[0]=="insert":
            l.insert(int(nval[1]),int(nval[2]))
        if nval[0]=="print":
            print(l)
        if nval[0]=="remove":
            l.remove(int(nval[1]))
        if nval[0]=="sort":
            l.sort()
        if nval[0]=="pop":
            l.pop(int(nval[1]))
        if nval[0]=="reverse":
            l.reverse()