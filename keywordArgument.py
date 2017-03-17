#Keyword argument
#if you have some functions with many parameters and you want to specify only some of them ,
#then you can give values for such paramters by nameing them- this is called keyword arguments

def func(a,b=5,c=10): #if not passed by caller default value of b and c is printed
    print 'a is',a,'and b is',b,'and c is',c

func(b=3,c=7)
func(b=25,c=24)
func(b=50,a=100)
