def make_car(brand, model, **car_info):
    """Строит словарь с информацией о авто."""
    profile = {}
    profile['brand'] = brand
    profile['mobel'] = model
    for key, value in car_info.items():
        profile[key] = value
    return profile
    
car = make_car('subaru', 'outback', 
                            color='blue', 
                            tow_package=True)
                            
print(car)
