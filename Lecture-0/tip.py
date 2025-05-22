def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.replace("$", "")
    floated_dollars = float(d)
    return floated_dollars


def percent_to_float(p):
    p = p.replace("%", "")
    p = float(p)
    floated_percent = p / 100
    return floated_percent


main()
