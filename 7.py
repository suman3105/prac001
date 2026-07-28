d={}
def input2():
    n=int(input("enter the no of dics to enter"))
    for i in range (n):
        x=input("enter key")
        y=input("enter value")
        d[x]=y
    print(d)
def delete():
    x=input("enter the key value to delete")
    del d[x]
    print("done")
def update():
    n=int(input("enter the no of dics to update"))
    for i in range (n):
        x=input("enter key")
        y=input("enter value")
        d[x]=y
    print(d)
    

while  True:
    choice=int(input("enter a choice : "))

    if choice==1:
        input2()
    elif choice==2:
        delete()
    elif choice==3:
        update()
    else:
        print("thank you bitch")
        break
        
        
        
        
    
