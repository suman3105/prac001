n=[5,4,3,2,1]
largest=0
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]>n[j]:
            n[i] ,n[j] = n[j], n[i]
print(n)         
    
