s=input()
t=input()
d={}
if len(s)!=len(t):
    print("false")
for ch in s:
    d[ch]=d.get(ch,0)+1
for ch in t:
    if ch not in d:
        print("false")
    d[ch]-=1
    if d[ch]<0:
        print("false")

print("true")
