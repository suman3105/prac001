'''n=list(map(int,input().split()))
x=int(input("enter target"))
for i in range(len(n)):
    if n[i]==x:
        print("element found at index",i)
        print("element is : ",n[i])
    else:
        print("element is not found")
        break
n=list(map(int,input().split()))
x=int(input("target"))
low=0
high=len(n)-1
while low<=high:
    mid = (low+high)//2
    if x==n[mid]:
        print("found  index: ",mid)
        break
    elif x<n[mid]:
        high=mid-1
    else:
        low=mid+1'''
n=input("enter string")
d={}
for x in n:
    if x  in d:
        d[x]+=1
    else:
        d[x]=1
print(d, end=" ")

