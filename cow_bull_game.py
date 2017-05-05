import random

def compare_numbers(user_guess,random_number):
    print "Random Number: "+str(random_number)
    cow_bull = [0,0]
    user_guess_list = []
    random_number_list = []
    i=0
    while user_guess != 0:
        user_guess_list.append(user_guess%10)
        user_guess = user_guess/10
        i=i+1
    i=0
    while random_number !=0:
        random_number_list.append(random_number%10)
        random_number = random_number/10
        i=i+1
    for i in range(0,4):
        if user_guess_list[i] != random_number_list[i] and user_guess_list[i] in random_number_list:
            cow_bull[1] +=1
        if user_guess_list[i] == random_number_list[i]:
            cow_bull[0] +=1

    return cow_bull
        


if __name__=="__main__":
    user_guess =int(raw_input("Guess a four digit Number"))
    random_number = random.randint(1000,9999)
    cow_bull = compare_numbers(user_guess,random_number)
    print str(cow_bull[0]) + " "+ str(cow_bull[1])
