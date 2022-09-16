import sys


def main():
    fraction = input("Fraction: ")
    converted = convert(fraction)
    print(gauge(converted))


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x > y:
        raise ValueError("X cannot be greater than Y")
    percentage = round(x / y * 100)
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()