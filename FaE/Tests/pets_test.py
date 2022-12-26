catfile = 'cat'
try:
    with open(catfile) as f_obj:
        for line in f_obj:
            print(line.title().rstrip())
except FileNotFoundError:
    print(f_obj.title() + " cannot be read")

dogfile = 'dog'
try:
    with open(dogfile) as f_obj:
        content = f_obj.read()
except FileNotFoundError:
    print(f_obj.title() + " cannot be read")
else:
    print(content.title())

dogfile = 'Dog'
try:
    with open(dogfile) as f_obj:
        lines = f_obj.readlines()
except FileNotFoundError:
    pass
else:
    for line in lines:
        print(line.title().rstrip())

