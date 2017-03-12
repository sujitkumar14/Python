#check number is prime or not
def primeOrNot(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return 0
    return 1
def printResult(x):
    if x==1:
        print "Yes"
    else:
        print "No"
    
x = primeOrNot(10)
printResult(x)
x = primeOrNot(7)
printResult(x)
x = primeOrNot(3)
printResult(x)
x = primeOrNot(9)
printResult(x)
x = primeOrNot(11)
printResult(x)
