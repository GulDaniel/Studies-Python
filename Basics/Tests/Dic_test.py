"""
Rios: Crie um dicionário que contenha três rios importantes e o país que
cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.
• Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre
pelo Egito.
• Use um laço para exibir o nome de cada rio incluído no dicionário.
• Use um laço para exibir o nome de cada país incluído no dicionário.
Enquete: Crie um dicionário que contenha nome e linguagem de programação favorita. 
• Crie uma lista de pessoas que devam participar da enquete sobre linguagem
favorita. Inclua alguns nomes que já estejam no dicionário e outros que não
estão.
• Percorra a lista de pessoas que devem participar da enquete. Se elas já tiverem
respondido à enquete, mostre uma mensagem agradecendo-lhes por responder.
Se ainda não participaram da enquete, apresente uma mensagem convidando-as
a responder.
"""

rios = {'nilo': 'egito', 'amazonas': 'brasil', 'mississipi': 'eua'}
for rio in sorted(rios):
    print("O " + rio.title() + " corre pelo " + rios[rio].title())

for rio in sorted(rios.keys()):
    print(rio.title())

for pais in sorted(rios.values()):
    print(pais.title())

print("\n")

favorite_languages = {
    'phil': 'python',
    'sarah': 'c',
    'joe': 'java',
    'jack': 'python',
    'bob': 'ruby',
    'bill': 'assembly',
    }

topoll = ['phil', 'sarah', 'mark', 'jonas', 'bob', 'clif', 'philip', 'ed']

for name in sorted(topoll):
    if name in favorite_languages.keys():
        print("Thank you " + name.title() + ", for voting!")
    else:
        print("Please " + name.title() + ", take our poll!")
