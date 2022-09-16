def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return s[0:2].isalpha() and 1 < len(s) < 7 and numbers_correct(s) and s.isalnum()


def numbers_correct(s):
    index = 0
    for c in s:
        if c.isdecimal():
            if int(c) == 0:
                return False
            elif s[index:len(s) - 1].isdecimal() == False:
                return False
            else:
                return True
        index += 1
    return True

main()