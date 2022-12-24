#atribuindo valores
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("Your just earned " + str(new_points) + " points!")

#adicionando elementos
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_1 = {}
alien_1['color'] = 'yellow'
alien_1['points'] = 10
print(alien_1)

#modificando elementos
alien_1['color'] = 'blue'
print("The alien 1 is now " + alien_1['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

#removendo elementos
alien_1 = {'color': 'yellow', 'points': 5}
print(alien_1)
del alien_1['points']
print(alien_1)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'java',
    }

print("Sarah's favorite language is " + 
    favorite_languages['sarah'].title() + ".")
