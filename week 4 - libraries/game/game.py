import random

level = 0

while level < 1:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass

random_int = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < random_int:
                print("Too small!")
            elif guess > random_int:
                print("Too large!")
            else:
                print("Just right!")
                break
    except ValueError:
        pass