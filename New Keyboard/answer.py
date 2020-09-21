s=input()
ar=[[]]
isnum=1
c=1
for i in range(len(s)):
    if s[i]=="<":
        ar.append([])
        c=2
        continue
    if s[i]==">":
        c=1
        continue
    if s[i]=="*":
        if c==1 and ar[0]:
            ar[0].pop()
        if c==2 and ar[-1]:
            ar[-1].pop()
        continue
    if s[i]=="#":
        isnum=1-isnum
        continue
    if s[i].isdigit():
        if isnum:
            if c==1:
                ar[0].append(s[i])
            else:
                ar[-1].append(s[i])
        continue
    else:
        if c==1:
            ar[0].append(s[i])
        else:
            ar[-1].append(s[i])
k=[]
for i in range(len(ar)-1,-1,-1):
    k+=ar[i]
print("".join(k))
