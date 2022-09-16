months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()

    try:
        split_date = date.split("/")
        if len(split_date) < 3:
            raise ValueError()
        year = split_date[2]
        month = split_date[0]
        day = split_date[1]
    except ValueError:
        split_date = date.split(" ")
        year = split_date[2]
        month = str(months.index(split_date[0]) + 1)
        day = split_date[1][:-1]

    #TODO: replace logic here with exception if user inputs date in UK format
    if len(month) <= 2 and len(day) <= 2:
        if int(day) <= 31 and int(month) <= 12:
            if int(day) < 10:
                day = "0" + day
            if int(month) < 10:
                month = "0" + month
            print(f"{year}-{month}-{day}")
            break