#prompt user for the answer to the Great Question of Life, the Universe and Everything,
#If user inputs 42, or case-insensitively forty-two or forty two output Yes.
#Else output No.


def main():
	answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
	if check(answer):
		print("Yes")
	else:
		print("No")


def check(usr_answer):
    return usr_answer == "42" or usr_answer == "forty-two" or usr_answer == "forty two"

main()
