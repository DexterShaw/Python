list=[]
for i in range(20):
    list.append(i),
    print(list[i])
for i in range(20):
    if list[i]%5==0 and list[i]%7!=0 and list[i]%11!=0:
        list[i]="hearth "
    if list[i]%7==0 and list[i]%5!=0 and list[i]%11!=0:
        list[i]='snake'
    if list[i]%11==0 and list[i]%7!=0 and list[i]%5!=0:
        list[i]='dog'
    if list[i]%5==0 and list[i]%7==0 and list[i]%11!=0:
        list[i]='hearth snake'
    if list[i]%7==0 and list[i]%5!=0 and list[i]%11==0:
        list[i]='snake dog'
    if list[i]%11==0 and list[i]%7!=0 and list[i]%5==0:
        list[i]='hearth dog'
    if list[i]%11==0 and list[i]%7==0 and list[i]%5==0:
        list[i]='hearth snake dog'
    print(list[i])
