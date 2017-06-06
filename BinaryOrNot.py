#check whether given string is binary number or not using classes

class BinaryOrNot:
    def __init__(self):
        print "inside class"
    def findBinaryOrNot(self,s):
        for i in range(len(s)):
            if s[i]!='0' and s[i]!='1':
                return 0;
        return 1;


binaryOrNot = BinaryOrNot();
x = binaryOrNot.findBinaryOrNot('0110');
if x==1:
    print 'yes'
else:
    print 'No'
