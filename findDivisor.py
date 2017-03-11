num = int(raw_input());
for i in range(2,int(num**(0.5)+1)):
    if num%i==0:
        print i
        if i!=num/i:
            print num/i
