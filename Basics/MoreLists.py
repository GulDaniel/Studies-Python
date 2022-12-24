#laços de repetição
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

#números
for value in range(1,6):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares = [x**2 for x in range (1,11)]
print(squares)

#estatística simples
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#slicing
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])

for player in players[:3]:
    print(player.title())

#copiando
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]
print(my_foods)
print(friends_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream') 
print(my_foods)
print(friends_foods)

