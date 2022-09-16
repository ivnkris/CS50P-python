def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    index = 0
    numbers_correct = True
    first_number = True

    for c in s:
        if c.isdecimal() and first_number == True:
            if int(c) == 0:
                numbers_correct = False
                break
            else:
                first_number = False
        if c.isdecimal():
            if s[index:len(s)].isdecimal() == False:
                numbers_correct = False
                break
        index += 1

    return s[0:2].isalpha() and 1 < len(s) < 7 and numbers_correct == True and s.isalnum()


if __name__ == "__main__":
    main()