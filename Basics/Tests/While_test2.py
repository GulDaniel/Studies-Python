'''
Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com os
nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e
mostre uma mensagem para cada pedido, por exemplo, Preparei seu sanduíche
de atum. À medida que cada sanduíche for preparado, transfira-o para a lista de
sanduíches prontos. Depois que todos os sanduíches estiverem prontos, mostre uma
mensagem que liste cada sanduíche preparado.
Sem pastrami: Usando a lista sandwich_orders do Exercício anterior, garanta
que o sanduíche de 'pastrami' apareça na lista pelo menos três vezes.
Acrescente um código próximo ao início de seu programa para exibir uma
mensagem informando que a lanchonete está sem pastrami e, então, use um laço
while para remover todas as ocorrências de 'pastrami' em sandwich_orders.
Garanta que nenhum sanduíche de pastrami acabe em finished_sandwiches.
Férias dos sonhos: Escreva um programa que faça uma enquete sobre as
férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se pudesse
visitar um lugar do mundo, para onde você iria? Inclua um bloco de código que
apresente os resultados da enquete
'''

sandwich_orders = ['bauru', 'mortadela', 'teriaky', 'podrão']
finished_sandwiches = []

while sandwich_orders:
    done = sandwich_orders.pop()
    print("Your sandwiche " + done + " is ready to eat!")
    finished_sandwiches.append(done)
for sandwiche in finished_sandwiches:
    print("We made a " + sandwiche.title() + " sandwiche!") 

print("\n")

sandwich_orders = [
    'bauru', 
    'pastrami', 
    'mortadela', 
    'pastrami',
    'teriaky',
    'pastrami'
     'podrão']
finished_sandwiches = []

print("Sorry, we're out of Pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    done = sandwich_orders.pop()
    print("Your sandwiche " + done + " is ready to eat!")
    finished_sandwiches.append(done)
for sandwiche in finished_sandwiches:
    print("We made a " + sandwiche.title() + " sandwiche!")

print("\n")

dream_vacations = {}

polling_active = True
while polling_active:
    name = input("What is your name? ")
    place = input("If you could take a vacation anywhere, where would it be? ")
    dream_vacations[name] = place
    repeat = input("Add another vote? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("--- Poll Results ---")
for name, place in dream_vacations.items():
    print(name.title() + " would like to visit " + place.title())
