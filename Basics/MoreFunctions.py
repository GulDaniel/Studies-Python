def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('serj', 'tankian')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('serj', 'tankian')
print(musician)

musician = get_formatted_name('wolfgang', 'mozart', 'amadeus')
print(musician)

#retornando estruturas
def build_person(first_name, last_name, age = ''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age    
    return person

musician = build_person('serj', 'tankian')
print(musician)
musician = build_person('Johan', 'Bach', '23')
print(musician)

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

