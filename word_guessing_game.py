import random

answer = input("Marvel or DC? ").strip()

if answer == "Marvel":
    print("I got a Marvel fan! Get ready to jump in MCU")
    words = ['Ironman', 'Spiderman', 'Hulk', 'Black widow', 'Captain america',
             'Hawkeye', 'Thanos', 'Doctor strange']
    while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print()

    if failed == 0:
        print("\nYou Win")
        print("The word is:", word)
        break

    guess = input("Guess a character: ")

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", turns, 'more guesses')

        if turns == 0:
            print("You Loose")
            print("The word was:", word)

elif answer == "DC":
    print("I got a DC fan! Get ready to jump in DCU")
    words = ['Batman', 'Superman', 'Aquaman', 'Wonderwoman', 'Flash']
    while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print()

    if failed == 0:
        print("\nYou Win")
        print("The word is:", word)
        break

    guess = input("Guess a character: ")

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", turns, 'more guesses')

        if turns == 0:
            print("You Loose")
            print("The word was:", word)

else:
    print("Watch some movies kiddo !")
    words = ['ironman', 'spiderman', 'hulk', 'black widow', 'captain america',
             'hawkeye', 'thanos', 'doctor strange', 'batman', 'reverse', 'water', 'board', 'geeks']

name = input("Enter your name: ")
print(f"Looking forward to see you {name}!")

word = random.choice(words)

print("Guess the characters")

guesses = ''
turns = 5


