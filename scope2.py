y = 'global y'
def test():
    nonlocal y
    y = 'local y'
    print y
test()
print y
