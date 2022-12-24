'''
Camiseta: Escreva uma função chamada make_shirt() que aceite um tamanho e o texto de uma 
mensagem que deverá ser estampada na camiseta. A função deve exibir uma frase que mostre
o tamanho da camiseta e a mensagem estampada. Chame a função uma vez usando argumentos
posicionais para criar uma camiseta. Chame a função uma segunda vez usando argumentos
nomeados.
Camisetas grandes: Modifique a função make_shirt() de modo que as camisetas ejam grandes
por default, com uma mensagem 'I love python'. Crie uma camiseta grande e outra média com
a mensagem default, e uma camiseta de qualquer tamanho com uma mensagem
diferente.
Cidades: Escreva uma função chamada describe_city() que aceite o nome de uma cidade e de
seu país. A função deve exibir uma frase simples, como Reykjavik está localizada na Islândia.
Forneça um valor default para o parâmetro que representa o país. Chame sua função para três
cidades diferentes, em que pelo menos uma delas não esteja no país default.
'''

def make_shirt(size, text):
    print("Shirt size: " + size.title())
    print("Shirt text: " + text.upper())

make_shirt('medium', 'havana 1921')
make_shirt(size='large', text='riga 1960')

print('\n')

def make_shirt(size='large', text='I love python'):
    print("Shirt size: " + size.title())
    print("Shirt text: " + text.upper())

make_shirt()
make_shirt('medium')
make_shirt('small', 'c gang arrives')

print('\n')

def describe_city(city, country='Brazil'):
    print(city.title() + " is located in " + country.title() +".")

describe_city('madrid')
describe_city('rio de janeiro')
describe_city('araxa')
