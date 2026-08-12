def calculate(first_number,second_number,operator):
    if operator=="+":
        return first_number+second_number
    elif operator=="-":
        return first_number-second_number
    elif operator=="*":
        return first_number*second_number
    elif operator=="/":
        return first_number/second_number
    else:
        return "invalid operator"

first_number=int(input("enter the first number"))
second_number=int(input("enter the second number"))
operator=input("enter the operator")
print(calculate(first_number,second_number,operator))
    