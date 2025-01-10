us_input = "yes"

while us_input == "yes":
    a = int(input("number1: "))
    b = int(input("number2: "))
    c = input("operation: ")

    if c == '*':
        print(a * b)
    elif c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '/':
        if b == 0:
            print("Error")
        else:
            print(a / b)
    us_input = input("continue the calculation? Enter 'yes' or 'no'")
    if us_input != "yes" and us_input != "no":
        print("Command not recognized.")

