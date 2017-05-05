def func():
    print x
    global x
    x = x+10
    
x = 10
func()
print x
