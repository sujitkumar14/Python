import random
if __name__=="__main__":
    print "Welcome In the game of Dice."
    print "Enter 1 to continue the game"
    print "Enter 0 to exit"
    print "Let's start"
    print "Enter 1 or 0"

    choice  = int(raw_input())
    while choice:
        print "Let's roll a dice"
        print "your dice is start rolling"
        print "rolling..."
        ran = random.randrange(1,7)
        print "Your dice number is..."
        print ran
        print "do you want to roll it again"
        choice  = int(raw_input())
