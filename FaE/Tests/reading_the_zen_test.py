#printing all file
filename = 'zen'
with open(filename) as file_object:
    content = file_object.read()
    print(content)

#replacing a world
#replacing Dutch to French
with open(filename) as file_object:
    for line in file_object:
        print(line.replace('Dutch', 'French').rstrip())

print('\n')

#print using a list with lines
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

