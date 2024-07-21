import random

the_range=input("give the upper range: ")

if the_range.isdigit():
    the_range=int(the_range)

    if the_range<=0:
        print("please provide a larger top range")
else:
    print("please provide a number next time.")
    quit()

random_number=random.randrange(0,the_range)
guesses=0

while True:
    guesses+=1
    user_guess=input("Make a guess: `")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("please type a number next time...")
        continue

    if user_guess==random_number:
        print("you got it!")
        print("you took", guesses, "guesses to get it right")
        break
    elif user_guess<random_number:
        print("go higher!!")
    else:
        print("go lower!")
    
