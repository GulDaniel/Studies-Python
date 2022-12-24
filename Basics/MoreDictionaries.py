#acessando chaves
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'java',
    }

for name in favorite_languages.keys():
    print(name.title())

#for name in favorite_languages também funciona

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
            favorite_languages[name].title() + "!")

#verificando valor
if 'erin' not in favorite_languages.keys():
    print("Erin, pease take our poll!")

#ordenando
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

#criando duplicata
favorite_languages['jack'] = 'python'

#acessando valores
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("\n")

#utilizando um conjunto para evitar duplicatas
for language in set(sorted(favorite_languages.values())):
    print(language.title())
