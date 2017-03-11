string  = raw_input()
lenString = len(string)
j=lenString-1
flag =0
for i in range(0,lenString/2):
    if string[i]!=string[j]:
        print "No"
        flag =1
        break
    j=j-1
if flag==0:
    print "Yes"

