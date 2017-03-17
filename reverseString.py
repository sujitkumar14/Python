string = raw_input().split(" ");
reverseString =''
for i in range(0,len(string)):
    reverseString = reverseString+string[len(string)-1-i]+" ";
print reverseString

