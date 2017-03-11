nextgame = True
while nextgame:
    playerA = raw_input("Player A")
    playerB = raw_input("Player B")
    if playerA=="rock" and playerB=="scissors":
        print "Congratulations Player A won the match"
    elif playerA=="rock" and playerB=="paper":
        print "Congratulations Player B won the match"
    elif playerB=="rock" and playerA=="scissors":
        print "Congurlations!! Playar B won the match"
    elif playerA=="scissors" and playerB=="paper":
        print "Congratulations Player A won the match"
    elif playerB=="scissors" and playerA=="paper":
        print "Congurlations!! Playar B won the match"
    elif playerA=="paper" and playerB=="rock":
        print "Congratulations Player A won the match"
    elif playerB=="paper" and playerA=="rock":
        print "Congurlations!! Playar B won the match"
    else:
        print "Tie"

    con = raw_input("Do you want to continue:y/n")
    if con=='y':
        nextgame = True
    else:
        nextgame = False

