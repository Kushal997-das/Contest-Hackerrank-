for _ in range(int(input())):
    n=input()
    k=int(input())
    ans=""
    for i in n:
        if i=="0" and 0<k:
            ans+="1"
            k-=1
        else:
            ans+="0"
    print(ans)
