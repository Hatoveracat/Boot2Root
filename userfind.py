import random

print("<----------------->Guess the Username Correctly to Login<---------------->")
guess = input("Enter your username: ")
ulist = ["breacher" , "cisco" , "pwnme" , "pwnmenow"]
ranidx = random.randint(0,len(ulist)-1)
if ulist[ranidx] == "breacher":
        print(f"Your Username is: {ulist[ranidx]}")
else:
        print("Try Again!! :((((((((((((((")
