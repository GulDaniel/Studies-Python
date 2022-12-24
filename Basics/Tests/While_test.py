'''
Ingredientes para uma pizza: Escreva um laço que peça ao usuário para
fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
fornecido. À medida que cada ingrediente é especificado, apresente uma
mensagem informando que você acrescentará esse ingrediente à pizza.
Ingressos para o cinema: Um cinema cobra preços diferentes para os
ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos de 3
anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o ingresso
custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15 dólares.
Escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes
o preço do ingresso do cinema.
Escreva um laço que pergunte as comidas favoritas de uma pessoa:
• use uma variável active para controlar o tempo que o laço executará.
Infinito: Escreva um laço que nunca termine e execute-o. (Para encerrar o
laço, pressione CTRL-C ou feche a janela que está exibindo a saída.)
'''

topping = ""
while topping != 'quit':
    topping = input("Please, enter the toppings you would like: ('quit' to exit) ")
    if topping != 'quit':        
        print("Adding " + topping + " to your pizza!")

print("\n")

while True:
    age = input("Please, enter your age: ('quit to exit') ")
    if age == 'quit':
        break
    elif int(age) < 3:
        print("Your ticket is free!")
    elif int(age) < 13:
        print("Your ticket is $10")
    elif int(age) > 12:
        print("Your ticket is $15")

print("\n")

active = True

while active:
    food = input("Please, enter your favorite foods: ('quit to exit') ")
    if food == 'quit':
        active = False
    else:
        print(food.title() + "? Delicious!")        

'''
infinito
while True:
    x = 0
    print(x)
'''
