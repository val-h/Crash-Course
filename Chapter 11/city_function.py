def city_country_name(city, country, region=''):
    """Returning a formatted name"""
    if region:
        formatted_name = f'{city} - {region}, {country}'
    else:
        formatted_name = f'{city}, {country}'
    return formatted_name.title()
