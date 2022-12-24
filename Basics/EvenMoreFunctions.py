def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)  
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#mantendo a lista original e passando uma cópia
#print_models(unprinted_designs[:], completed_models)

#múltiplos argumentos
#devem estar depois de posicionais e nomeados
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
    print("\nMaking a " + size + " pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('medium', 'pepperoni')
make_pizza('large', 'mushrooms', 'green peppers', 'extra cheese')

print('\n')

#** cria um dicionário vazio
def build_profile(first, last, **user_info):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
    location='princeton',
    field ='physics')

print(user_profile)
