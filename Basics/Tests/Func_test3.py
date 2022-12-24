'''
Mágicos: Crie uma lista de nomes de mágicos. Passe a lista para uma
função chamada show_magicians() que exiba o nome de cada mágico da lista.
Grandes mágicos: Comece com uma cópia de seu programa do Exercício
anterior Escreva uma função chamada make_great() que modifique a lista de
mágicos acrescentando a expressão o Grande ao nome de cada mágico. Chame
show_magicians() para ver se a lista foi realmente modificada.
Mágicos inalterados: Comece com o trabalho feito no Exercício anterior.
Chame a função make_great() com uma cópia da lista de nomes de mágicos.
Como a lista original não será alterada, devolva a nova lista e armazene-a em uma
lista separada. Chame show_magicians() com cada lista para mostrar que você
tem uma lista de nomes originais e uma lista com a expressão o Grande
adicionada ao nome de cada mágico.
'''

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    for magician in range(len(magicians)):
        magicians[magician] +=  " the Great"
    return magicians

magicians = ['houdini', 'mister m', 'rasputin']
show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)

print('\n')

magicians = ['houdini', 'mister m', 'rasputin']
greaters = make_great(magicians[:])
show_magicians(greaters)
show_magicians(magicians)
print('\n')
