import random


def main():
    level = get_level()
    score = 10
    for _ in range(10):
        trials_left = 3
        rand_int1 = generate_integer(level)
        rand_int2 = generate_integer(level)
        while trials_left != 0:
            answer = input(f"{rand_int1} + {rand_int2} = ")
            try:
                if int(answer) == rand_int1 + rand_int2:
                    trials_left = 0
                else:
                    raise ValueError
            except ValueError:
                trials_left = trials_left - 1
                print("EEE")
                if trials_left == 0:
                    score = score - 1
                    print(f"{rand_int1} + {rand_int2} = {rand_int1 + rand_int2}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = input("Level: ")
            if int(level) != 1 and int(level) != 2 and int(level) != 3:
                raise ValueError
            else:
                return int(level)
        except ValueError:
            pass


def generate_integer(level):
    if level != 1 and level != 2 and level != 3:
        raise ValueError("generate_integer received incorrect arg")
    if level == 1:
        random_int = random.randint(0, 9)
    elif level == 2:
        random_int = random.randint(10, 99)
    else:
        random_int = random.randint(100, 999)

    return random_int


if __name__ == "__main__":
    main()