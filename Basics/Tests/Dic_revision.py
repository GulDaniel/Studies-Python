#dictionaries revision

alien_0 = {'color': 'green', 'points': 5, 'speed': 'slow'}
alien_1 = {'color': 'yellow', 'points': 10, 'speed': 'medium'}
alien_2 = {'color': 'red', 'points': 15, 'speed': 'fast'}
print('Green alien value is: ' + str(alien_0['points']))
print('Yellow alien speed is : ' + alien_1['speed'].title())
print('Alien 3 color is: ' + alien_2['color'].title())

'''
Green alien value is: 5
Yellow alien speed is : Medium
Alien 3 color is: Red
'''

print('\n')

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
   print(alien)
   print(alien['color'])
   print(alien['points'])
   print(alien['speed'])
   
   '''
{'color': 'green', 'points': 5, 'speed': 'slow'}
green
5
slow
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
yellow
10
medium
{'color': 'red', 'points': 15, 'speed': 'fast'}
red
15
fast
   '''
    
print('\n')

aliens = {'alien_0': ['green', 5, 'slow'],
    'alien_1': ['yellow', 10, 'medium'],
    'alien_2': ['red', 15, 'fast'],
    }

for info in aliens['alien_2']:
    print(info)

'''
red
15
fast
'''

print('\n')

for alien, infos in aliens.items():
    print(alien.title() + ':')
    for info in infos:
        print('\t' + str(info).title())
        
'''
Alien_0:
        Green
        5
        Slow
Alien_1:
        Yellow
        10
        Medium
Alien_2:
        Red
        15
        Fast
'''

print('\n')
        
neu_aliens = {
    'alien_0': {'color': 'green', 'points': 5, 'speed': 'slow'},
    'alien_1': {'color': 'yellow', 'points': 10, 'speed': 'medium'},
    'alien_2': {'color': 'red', 'points': 15, 'speed': 'fast'},
    }
    
for alien, info in neu_aliens.items():
    print('\n' + alien.title() + ':')
    print('Color: '  + info['color'].title())
    print('Points: ' + str(info['points']).title())
    print('Speed: ' + info['speed'].title())
    
'''
Alien_0:
Color: Green
Points: 5
Speed: Slow

Alien_1:
Color: Yellow
Points: 10
Speed: Medium

Alien_2:
Color: Red
Points: 15
Speed: Fast
'''

