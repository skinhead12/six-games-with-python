import random 

top_of_range = input("Type a number :")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number larger tha 0 next time.")
        quit()
        
else:
    print("Please type a number next time.")
    quit()
        
random_numer = random.randint(0, top_of_range)

while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
       user_guess = int(user_guess)            
    else:
       print("Please type a number next time.")
       continue
   
    if user_guess == random_numer:
       print("You got it!")
       break
    else:
        print("You go it wrong!")