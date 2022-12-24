"""
Pessoas: Crie três dicionários que representem pessoas diferentes e
armazene os três dicionários em uma lista chamada people. Percorra sua lista de
pessoas com um laço. À medida que percorrer a lista, apresente tudo que você
sabe sobre cada pessoa.

Animais de estimação: Crie vários dicionários, em que o nome de cada
dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua o
tipo do animal e o nome do dono. Armazene esses dicionários em uma lista
chamada pets. Em seguida, percorra sua lista com um laço e, à medida que fizer
isso, apresente tudo que você sabe sobre cada animal de estimação.

Lugares favoritos: Crie um dicionário chamado favorite_places. Pense em
três nomes para usar como chaves do dicionário e armazene de um a três lugares
favoritos para cada pessoa. Para deixar este exercício um pouco mais interessante,
peça a alguns amigos que nomeiem alguns de seus lugares favoritos. Percorra o
dicionário com um laço e apresente o nome de cada pessoa e seus lugares
favoritos.

Cidades: Crie um dicionário chamado cities. Use os nomes de três
cidades como chaves em seu dicionário. Crie um dicionário com informações sobre
cada cidade e inclua o país em que a cidade está localizada, a população
aproximada e um fato sobre essa cidade. As chaves do dicionário de cada cidade
devem ser algo como country, population e fact. Apresente o nome de cada
cidade e todas as informações que você armazenou sobre ela.
"""

mark = {'fname': 'mark', 'lname': 'elrisch', 'height': 190, 'weight': 90, 'age': 22}
julie = {'fname': 'julie', 'lname': 'ziemman', 'height': 155, 'weight': 50, 'age': 18}
kirk = {'fname': 'kirk', 'lname': 'lazarus', 'height': 187, 'weight': 76, 'age': 31}

people = [mark, julie, kirk]
for person in people:
    print("\nName: " + person['fname'].title())
    print("Last name: " + person['lname'].title())
    print("Height: " + str(person['height']))
    print("Weight " + str(person['weight']))
    print("Age: " + str(person['age']))

print("\n")

rex = {'type': 'pastor alemão', 'owner': 'mark'}
brutus = {'type': 'bulldog', 'owner': 'julie'}
thor = {'type': 'bull terrier', 'owner': 'kirk'}

pets = [rex, brutus, thor]
for pet in pets:
    print(pet['owner'].title() + " has a " + pet['type'].title())

print("\n")


favorite_places = {
    'mark': ['paris', 'berlim', 'amsterdam'],
    'julie': ['buenos aires', 'moskow'],
    'kirk': ['athenas'],
    }

for person, places in favorite_places.items():
    print(person.title() + " favorite places are:")
    for place in places:
        print("\t" + place.title())

print("\n")

citties = {
    'barcelona': {'country': 'spain', 'pop': '2 million'},
    'berlin': {'country': 'germany', 'pop': '3.5 million'},
    'moscow': {'country': 'russia', 'pop': '4 million'},
    }

for name, city in citties.items():
    print(name.title() + " info:")
    print("\t" + city['country'].title())
    print("\t" + city['pop'].title())
