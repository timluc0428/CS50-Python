def main():

#prompt user input to insert one coin
    due = int(50)


#if user input matches a coin value subtract it from due
    while due > 1:
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5 or coin == 1:
          due -= coin

        if due > 0:
            print(f"Amount Due: {due}")
        else:
            print(f"Change Owed: {abs(due)}")

#    print("Thank you for your purchase")

main()
