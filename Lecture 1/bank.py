#prompt user for a greeting
#if greeting starts with "hello", output $0
#if the greeting starts with h, but is not hello, output $20
#otherwise output $100.
# ignore any leading whitespace, and treat greeting with case insensitiy


greeting = input("Greet me please. ").strip().lower().split()[0]

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
