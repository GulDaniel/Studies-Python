from collections import OrderedDict

food_place = OrderedDict()

food_place['sushi'] = 'japan'
food_place['burrito'] = 'mexico'
food_place['feijoada'] = 'brasil'
food_place['croisant'] = 'france'
food_place['alfajor'] = 'argentina'

for food, place in food_place.items():
    print(food.title() + " is a typical food example from " +
        place.title() + ".")  
