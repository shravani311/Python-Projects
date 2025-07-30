import random
import string

def generate_password(length,complexity):
    if complexity==1:
        chars=string.ascii_letters
    elif complexity==2:
        chars=string.ascii_letters+string.digits
    elif complexity==3:
        chars=string.ascii_letters+string.digits+string.punctuation
    else:
        print("Invalid complexity level")
    password=''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("===PASSWORD GENERATOR===")
    try:
        length=int(input("Enter length of password :- "))
        if length<4 :
            print("Password is too short ! Use atleast 4 characters.")
            return
    except ValueError:
        print("Please enter a valid error")
        return
    print("Choose Complexity level :")
    print("1. Letters only (week)")
    print("2. Letters & Numbers (moderate)")
    print("1. Letters Numbers & symbols(strong)")
    try:
        complexity=int(input("Your choice (1/2/3) :- "))
    except ValueError:
        print("Invalid choice")
    password=generate_password(length,complexity)
    if password:
        print(f"Password = {password}")
if __name__=="__main__":
    main()