
def get_sities_name(sity, country, population=''):
    """Одну строку в формате: Город, Страна, население"""
    if population:
        full_sity_name =  sity.title() + ' ' + country.title() + '- population ' + population
    else:
        full_sity_name = sity.title() + ' ' + country.title()
    return full_sity_name




