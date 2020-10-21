import random
 
gimme_a_number = random.randint(1, 102)

guesses = 0
 
while True:
        
    number = int(input("Enter a number between 1 and 102, yes 102. (Enter 0 to let the universe know you give up):"))
    
    guesses += 1
    
    if(number == 0):
        print("See you in another incarnation, maybe you'll come back as a single line of code.")
        break
    
    elif number < gimme_a_number:
        print("Hmm, it's a bit higher than that.")
        continue
    
    elif number > gimme_a_number:
        print("Hold on there boy, slow down a bit. The number is not that big.")
        continue
    
    else:
        print("You guessed it right! It was indeed {0}! How fun, great, cool, and something along those lines...".format(gimme_a_number))
        
        print("You guessed it in {0} tries by the way, quite impressive, add that to your resume".format(guesses))
