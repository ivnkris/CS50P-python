def main():
    str = input()
    print(convert(str))

def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")

main()