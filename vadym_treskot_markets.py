class Markets:
    def __init__(self, name, area, categories):
        self.name = name
        self.area = area
        self.categories = categories
    
    def __str__(self):
        return """Supermarket {0} has an area of {1} m**2 and has the following categories: {2}."""\
            .format(self.name, self.area, ', '.join(self.categories))


# market_family_food = Markets('Family Food', 80, ['Bread and Bakery', 'Dairy', 'Beverages'])
# print(market_family_food)
