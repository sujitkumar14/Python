def createList(a):
    length = len(a)
    b = []
    for i in range(0,length):
        if i==0:
            b.append(a[i])
        elif i==length-1:
            b.append(a[i])
    return b


a = [5, 10, 15, 20, 25]
b = createList(a)
print b
