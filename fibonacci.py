#fibonacci number
def fib(a,b,c):
    if c==0:
        return
    print a+b
    c -=1
    return fib(b,a+b,c)
c = int(raw_input("How many fibonacci number you want to generate"))
if c<2:
    if c==1:
        print "1"
    else:
        print "1"
        print "1"
else:
    print "1"
    print "1"
    fib(1,1,c-2)
    
