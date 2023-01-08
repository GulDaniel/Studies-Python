def get_formatted_location(city, country, population=''):
    f_city = city.title()
    f_country = country.title()
    if population:
       formatted_location = f_city + ', ' + f_country + ', Population = ' + population
    else:
       formatted_location = f_city + ', ' + f_country
    return formatted_location
