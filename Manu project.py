import sys
n=int(input("Enter number of items"))
Slist=[]
for i in range (n):
    N=input("item name")
    Slist.append(N)
print(Slist)
while True:
    cm=input('''What would you like to do
add:Add an item
remove:remove an item
replace:replace an item
exit/done:exit editing
''')
    cm.lower()
    if cm=='add':
        item=input("What item do you like to add")
        Slist.append(item)
    elif cm=='remove':
        rm=input("What item to remove")
        Slist.remove(rm)
    elif cm=='replace':
        item1=input("Enter item to replace")
        item2=input("Enter the item")
        for i in range(n):
            if Slist[i]==item1:
                Slist[i]=item2
    elif cm=='exit' or cm=='done':
        Ar=input("Do you want to arrange your shoping list")
        Ar.lower()
        if Ar=='yes':
            print("Shopping list")
            for i in Slist:
                print(i)
            sys.exit(0)
        elif Ar=='no':
            print("Shopping list",Slist)
    elif cm=='list':
        print(Slist)
