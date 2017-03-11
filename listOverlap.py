a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
lenA = len(a)
lenB = len(b)
if lenA<lenB:
    for i in range(0,lenA):
        if a[i] in b and a[i] not in c:
            c.append(a[i])
else:
    for j in range(0,lenB):
        if b[j] in a and b not in c:
            c.append(b[j])

print c
