import time

while True:
    age = input("enter your age: ")

    if age == "":
        print("Age cannot be empty")
        continue

    if not age.isdigit():
        print("Age must be a number")
        continue

    age = int(age)

    if age < 0:
        print("Your age cannot be negative")
    elif age > 100:
        print("I don't believe you, try again.")
    else:
        break

print("Nice")

name = input("enter your name: ")
while name == "":
    name = input("enter your name: ")

print(f"Let's play a game {name}, if you win. You get to leave, if I win you give your friend 5 big booms")
time.sleep(5)
print("We will play mad libs, do not lie to me if u got the verbs wrong. do not deny my power")
time.sleep(6)

verb1 = input("enter your verb: ")
while verb1 == "":
    verb1 = input("enter your verb: ")

verb2 = input("enter your 2nd verb: ")
while verb2 == "":
    verb2 = input("enter your 2nd verb: ")
time.sleep(3)
print(f"Danny {verb1} to the store and {verb2} groceries")

time.sleep(3)
print(f"Tell me the truth {name}, does your sentence make sense?")
time.sleep(3)
answer = input("Will you lie to him, or not? (y/n): ")
time.sleep(2)
if answer == "y":
    print("YOU LITTLE LIAAAR I MADE THIS GAME DO YOU THINK I DON'T KNOW YOUR ANSWER??")
elif answer == "n":
    print("Alright GG's have a good ni- DO YOU REALLY THINK IM THAT STUPID YOU ANSWERED YES AND THEN AFTER SEEING THE RESPONSE YOU CAME BACK HERE YOU LITTLE TWAAAAAT")
else:
    print("That wasn't a fucking yes or no was it? FUCKING ANSWER")
    time.sleep(1)
    print(f"Tell me the truth {name}, does your sentence make sense?")
    time.sleep(2)
    answer = input("Will you lie to him, or not? (y/n): ")
    time.sleep(1)
    if answer == "y":
        print("YOU LITTLE LIAAAR I MADE THIS GAME DO YOU THINK I DON'T KNOW YOUR ANSWER??")
    elif answer == "n":
        print(
            "Alright GG's have a good ni- DO YOU REALLY THINK M THAT STUPID YOU ANSWERED YES AND THEN AFTER SEEING THE RESPONSE YOU CAME BACK HERE YOU LITTLE TWAAAAAT")
    else:
        print("DO YOU THINK IM THAT STUPID TO LET YOU BYPASS THI-  im closing this program on you")
time.sleep(3)
