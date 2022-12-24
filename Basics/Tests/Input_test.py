'''
Car - Escreva um programa que pergunte ao usuário qual tipo de carro ele gostaria de alugar.
Mostre uma mensagem sobre esse carro, por exemplo, "Deixe-me ver se consigo um Subaru
para você."
Restaurant - Escreva um programa que pergunte ao usuário quantas pessoas estão em seu grupo
para jantar. Se a resposta for maior que oito, exiba uma mensagem dizendo
que eles deverão esperar uma mesa. caso contrário, informe que sua mesa está pronta.
Ten - Peça um número ao usuário, e em seguida informe se o número é múltiplo de 10
'''

print("Which car would you like to hire? ")
car = input()
print("I will check if I can find you a " + car)

print("\n")

print("Good evening, table for? ")
guests = input()
guests = int(guests)
if guests < 9:
    print("Your table is right here, follow me, please")
else:
    print("I'm sorry, you may have to wait for a table")

print("\n")

print("Tell me a number and I'll say if it is a multiple of 10: ")
number = int(input())
if number % 10 == 0:
    print(str(number) + " is a multiple of 10!")
else:
    print(str(number) + " is not a multiple of 10!")
