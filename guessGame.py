import random
if __name__=="__main__":
    print "Welcome in the Guess the Number game"
    print "In this game you have to guess a Number"
    print "and Machine also guess a number"
    print "if your number is smaller than machine's number"
    print "You step down one position"
    print "if lager than one position you step up one position"
    print "if equal to that number you get a key to unlock the mystery box"
    print "let's start......"
    print "do you want to start the game enter 1 and if no enter 0"
    choice  = int(raw_input())
    while choice:
        print "guess a 4 digit Number:"
        n = int(raw_input())
        m = random.randrange(1000,10000)
        print m
        if n<m:
            print "step down"
        elif n>m:
            print "step Up"
        else:
            print "You won the key "
        print "do you want to continue the game 1/0"
        choice = int(raw_input())
        
