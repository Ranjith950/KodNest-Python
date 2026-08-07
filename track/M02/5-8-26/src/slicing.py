word=input("enter the word:- ")
first=int(input("enter the first number:"))
second=int(input("enter the second number:"))
third=int(input("enter the third number:"))
number=[first,second,third]
record=(first,second,third)
print(f"middle: {word[1:-1]}")
print(f"first two: {number[:2]}")
print(f" revers: {record[::-1]}")