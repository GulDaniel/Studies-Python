'''
Sanduíches: Escreva uma função que aceite uma lista de itens que uma
pessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe tantos
itens quantos forem fornecidos pela chamada da função e deve apresentar um
resumo do sanduíche pedido. Chame a função três vezes usando um número
diferente de argumentos a cada vez.
Perfil do usuário: Crie um perfil seu chamando build_profile(), usando seu primeiro nome e
o sobrenome, além de três outros pares chave-valor que o descrevam.
Carros: Escreva uma função que armazene informações sobre um carro em
um dicionário. A função sempre deve receber o nome de um fabricante e um
modelo. Um número arbitrário de argumentos nomeados então deverá ser aceito.
Chame a função com as informações necessárias e dois outros pares nome-valor,
por exemplo, uma cor ou um opcional. Sua função deve ser apropriada para uma
chamada como esta:
car = make_car(‘subaru’, ‘outback’, color=’blue’, tow_package=True)
Mostre o dicionário devolvido para garantir que todas as informações foram
armazenadas corretamente.
'''

def make_sand(*ingredients):
    print("\nYour sandwiche has those ingredients:")
    for ingredient in ingredients:
        print("- " + ingredient)

make_sand('cheese', 'pepperoni', 'green peppers')
make_sand('mayo', 'chicken')
make_sand('tomatoes')

print('\n')

def build_profile(first, last, **user_info):
    profile = {}
    profile['First name'] = first.title()
    profile['Last name'] = last.title()
    for key, value in user_info.items():
        profile[str(key).title()] = str(value).title()
    return profile

my_profile = build_profile('daniel', 'araujo', location='iceland', age=22, fav_lang='python')
print(my_profile)

print('\n')

def build_car(brand, model, **car_info):
    car = {}
    car['Brand'] = brand
    car['Model'] = model
    for key, value in car_info.items():
        car[str(key).title()] = str(value).title()
    return car

car = build_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

print('\n')
