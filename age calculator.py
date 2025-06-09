while True:
    birth_year = int(input("Enter your birth year :"))
    current_year = int(input("Enter current year :"))
    age = current_year - birth_year
    days = age*365
    hours = days*24
    minutes = hours*60
    print(f"Your current age is {age},")
    print(f"you have lived {days} days on earth ")
    print(f"you have lived {hours} hours on earth")
    print(f"you have lived {minutes} minutes on earth")
    print("have you done anything to protect our earth,THINK ABOUT IT ")
    break 
    