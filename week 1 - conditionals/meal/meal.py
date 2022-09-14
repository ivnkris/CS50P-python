def main():
    t = convert(input("What time is it? "))

    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)

    if len(minutes) > 2:
        minutes, meridiem = minutes.split(" ")
        if meridiem == "p.m.":
            hours += 12

    return hours + int(minutes) / 60


if __name__ == "__main__":
    main()