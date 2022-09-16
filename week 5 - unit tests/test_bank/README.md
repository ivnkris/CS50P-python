In a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, restructuring your code per the below, wherein value expects a str as input and returns 0 if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”), or 100 otherwise, treating the str case-insensitively. Only main should call print.

def main():
...

def value(greeting):
...

if **name** == "**main**":
main()

Then, in a file called test*bank.py, implement three or more functions that collectively test your implementation of value thoroughly, each of whose names should begin with test* so that you can execute your tests with:

pytest test_bank.py
