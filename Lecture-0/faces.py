def main():

    feelings_sentance = input("How are you feeling? ")
    feelings_sentance = convert(feelings_sentance)
    print(feelings_sentance)

def convert(sentance):
    feeling = sentance.replace(":)", "🙂").replace(":(", "🙁")
    return feeling

main()
