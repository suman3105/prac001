n=list(map(int,input("enter the numbers").split()))
largest=n[0]
for i in n:
    if i>largest:
        largest=i
print(largest)
