"""
Nomes de cidade: Escreva uma função chamada city_country() que
aceite o nome de uma cidade e seu país. A função deve devolver uma string
formatada assim:
"Santiago, Chile"
Chame sua função com pelo menos três pares cidade-país e apresente o valor
devolvido.
Álbum: Escreva uma função chamada make_album() que construa um
dicionário descrevendo um álbum musical. A função deve aceitar o nome de um
artista e o título de um álbum e deve devolver um dicionário contendo essas duas
informações. Use a função para criar três dicionários que representem álbuns
diferentes. Apresente cada valor devolvido para mostrar que os dicionários estão
armazenando as informações do álbum corretamente.
Acrescente um parâmetro opcional em make_album() que permita armazenar o
número de faixas em um álbum. Se a linha que fizer a chamada incluir um valor
para o número de faixas, acrescente esse valor ao dicionário do álbum. Faça pelo
menos uma nova chamada da função incluindo o número de faixas em um álbum.
Álbuns dos usuários: Comece com o seu programa do Exercício anterior.
Escreva um laço while que permita aos usuários fornecer o nome de um artista e o
título de um álbum. Depois que tiver essas informações, chame make_album() com
as entradas do usuário e apresente o dicionário criado. Lembre-se de incluir um
valor de saída no laço while.
"""

def city_country(city, country):
    formatted = city.title() + ", " + country.title()
    return formatted

print(city_country('santiago', 'chile'))
print(city_country('viena', 'austria'))
print(city_country('eldorado', 'brazil'))

print('\n')

def make_album(singer, album, songs=''):
    cd = {}
    cd['singer'] = singer.title()
    cd['album'] = album.title()
    if songs:
        cd['songs'] = songs
    return cd

print(make_album('metallica', 'master of puppets'))
print(make_album('megadeth', 'rust in peace, polaris'))
print(make_album('rammnstein', 'mutter'))
print(make_album('amon amarth', 'berserker', 9))

print('\n')

def make_album(singer, album, songs=''):
    cd = {}
    cd['singer'] = singer.title()
    cd['album'] = album.title()
    if songs:
        cd['songs'] = songs
    return cd

while True:
    print("Press q at any time to exit")
    s_name = input("Singer name: ")
    if s_name == 'q':
        break
    a_name = input("Album name: ")
    if a_name == 'q':
        break
    print(make_album(s_name, a_name))
    print('\n')

print('\n')
