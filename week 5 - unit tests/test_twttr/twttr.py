def main():
    str = shorten(input("Input: "))
    print(f"Output: {str}")


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    for c in word:
        if c.lower() in vowels:
            word = word.replace(c, "")
    return word


if __name__ == "__main__":
    main()