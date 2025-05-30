#prompt user for input
def main():
    user_input = input("Input: ")

        #replace vowels
    twttr = replace_vowels(user_input)

    print(f"Output: {twttr}")

def replace_vowels(msg):
    msg = msg.replace("a", "")
    msg = msg.replace("A", "")
    msg = msg.replace("e", "")
    msg = msg.replace("E", "")
    msg = msg.replace("i", "")
    msg = msg.replace("I", "")
    msg = msg.replace("o", "")
    msg = msg.replace("O", "")
    msg = msg.replace("u", "")
    msg = msg.replace("U", "")
    return msg



main()
