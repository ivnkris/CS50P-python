import inflect

p = inflect.engine()
list = []

try:
    while True:
        word = input("Name: ")
        list.append(word)

except EOFError:
    name_list = p.join(list)
    print(f"\nAdieu, adieu, to {name_list}")