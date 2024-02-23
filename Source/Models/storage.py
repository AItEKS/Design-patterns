from Source.abstract_reference import abstract_reference
from unit import unit_model

class storage_model(abstract_reference):
    def init(self, name):
        super().__init__(name)
        self.name = name
        self.ingredients = {}
        self.recipes = {}

    def add_ingredient(self, name: str, quantity: int, unit: str):
        if name in self.ingredients:
            self.ingredients[name] += (quantity, unit)
        else:
            self.ingredients[name] = (quantity, unit)

    def add_recipe(self, name, ingredients_list):
        self.recipes[name] = ingredients_list

    @staticmethod
    def create_unit_kilogram():
        base = unit_model.create_unit_gramm()
        item = unit_model('килограмм', base, 1000)
        return item

    @staticmethod
    def create_unit_millilitr():
        item = unit_model('миллилитр', None, 1)
        return item

    @staticmethod
    def create_unit_litr():
        base = storage_model.create_unit_millilitr()
        item = unit_model('литр', base, 1000)
        return item

    @staticmethod
    def create_unit_shtuki():
        item = unit_model('штука', None, 1)
        return item
