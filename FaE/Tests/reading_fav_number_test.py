import json

filename = 'userfavnumber.json'

with open(filename) as f_obj:
   fav_num =  json.load(f_obj)
    
print("I know your favorite number! It is " + fav_num)








