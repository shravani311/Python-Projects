import random
def guessNumber():
    print("Welcome to Number Guesser Game")
    print("I am thinking of a number from 1 to 100...")
    secret_no=random.randint(1,100)
    attempts=0
    while(True):
        try:
            guess=int(input("Enter your guess :-"))
            attempts+=1
            if guess < secret_no:
                print("Too small....try again..")
            elif guess > secret_no:
                print("Too large....try again..")
            else:
                print("Correct Guess....Number is {secret_no}.")
                print("No of guesses were {attempts}")
                break
        except ValueError:
            print("Enter a valid number")
if __name__=="__main__":
    guessNumber()