st=input()
res = ""
left = 0
while left<len(st):
    right=left
    while right<len(st) and st[left]==st[right]:
        right+=1
    res+=st[left]+str(right-left)
    left=right
print(res)
