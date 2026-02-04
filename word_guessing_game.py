import random

name = input("What's your name: ")
print(f"Looking forward to see you {name}!!")

answer = input("What's your favourite ? Marvel or DC? ").strip()

if answer == "Marvel":
    print("I got a Marvel fan! Get ready to jump in MCU")
    words = ['ironman', 'spiderman', 'hulk', 'black widow', 'captain america', 'hawkeye', 'thanos', 'doctor strange']
elif answer == "DC":
    print("I got a DC fan! Get ready to jump in DCU")
    words = ['batman', 'superman', 'aquaman', 'wonderwoman', 'flash']
else:
    print("Watch some movies kiddo!")
    words = []

if words:
    word = random.choice(words).lower()
    guesses = ''
    turns = 5

    print("\nGuess the characters!")

    while turns > 0:
        failed = 0

        for char in word:
            if char == " ":
                print(" ", end=" ")
            elif char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1

        if failed == 0:
            print("\n\n🏆 You Win!")
            print(f"The word was: {word}")
            break

        print()
        guess = input("\nGuess a letter: ").lower()
        guesses += guess

        if guess not in word:
            turns -= 1
            print(f"❌ Wrong! You have {turns} more guesses.")

            if turns == 0:
                print("\n💀 You Lose")
                print(f"The word was: {word}")
