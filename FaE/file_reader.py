with open('pi_digits') as file_object:
    contents = file_object.read()
    print(contents)
#para remover a linha em branco no final
#print(contents.rstrip())

filename = 'pi_digits'

#imprimindo uma linha por vez
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#armazenando as linhas em uma lista
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

