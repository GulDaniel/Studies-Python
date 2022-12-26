print("Tell me two numbers and I'll sum them")

first_number = input("First number: ")
second_number = input("Second number: ")

try:
    sum = int(first_number) + int(second_number)
except ValueError:
    print("Please, input only number.")
else:
    print(first_number + ' + ' + second_number +
          " is equal to " + str(sum))

