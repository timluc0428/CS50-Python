def main():
    user_input = input("Input your variable in camel case: ")
    convert(user_input)

    print()
def convert(camel):
    for char in camel:
        if char.islower():
           print(char, end="")
        else:
            print(f"_{char.lower()}", end="")
main()
