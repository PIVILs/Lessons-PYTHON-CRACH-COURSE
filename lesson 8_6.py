def city_country(city, land):
    """Возвращает аккуратно отформатированный город и страну"""
    full_city = city + ' ' + land
    return full_city.title()
    
cities = city_country('oktya', 'russia')
print(cities)    

cities = city_country('samara', 'russia')
print(cities)

cities = city_country('rome', 'italia')
print(cities)
