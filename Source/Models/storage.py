from Source.abstract_reference import abstract_reference


class storage_model(abstract_reference):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.ingredients = {}
        self.recipes = {}

    def add_ingredient(self, name, quantity, unit):
        if name in self.ingredients:
            self.ingredients[name] += (quantity, unit)
        else:
            self.ingredients[name] = (quantity, unit)

    def add_recipe(self, name, ingredients_list):
        self.recipes[name] = ingredients_list
