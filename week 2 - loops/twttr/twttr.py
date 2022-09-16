str = input("Input: ")
vowels = ["a", "e", "i", "o", "u"]

for c in str:
    if c.lower() in vowels:
        str = str.replace(c, "")

print(f"Output: {str}")