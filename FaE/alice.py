filename = 'alice'

try:
    with open(filename) as f_obj:
         contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

title = "Alice in Wonderland"
print(title.split())


