print("Tell me two numbers and I'll sum them")
print("Press 'q' at any time to exit")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
         break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
         sum = int(first_number) + int(second_number)
    except ValueError:
         print("Please, input only number.")
    else:
         print(first_number + ' + ' + second_number +
           " is equal to " + str(sum))

