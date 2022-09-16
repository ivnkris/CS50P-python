str = input("camelCase: ")
for c in str:
    if c.islower() == False:
        snake_c = "_" + c.lower()
        str = str.replace(c, snake_c)
print(f"snake_case: {str}")