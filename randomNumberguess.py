import random
num = int(raw_input("guess a random number between 1 and 9: "))
gen = random.randint(1,9)
print "Random number is: "+str(gen)
if num<gen/2:
    print "Guess is too low"
elif num>gen*2:
    print "guess is too high"
elif num==gen:
    print "perfect guess"
else:
    print "You are near"
