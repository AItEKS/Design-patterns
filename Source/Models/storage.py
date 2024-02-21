from Source.abstract_reference import abstract_reference

class storage_model(abstract_reference):
    def __init__(self, name):
        super().__init__(name)
        self.recipes = {}

    def add_recipe(self, recipe_name, recipe):
        self.recipes[recipe_name] = recipe

    def get_recipe(self, recipe_name):
        if recipe_name in self.recipes:
            return self.recipes[recipe_name]
        else:
            return None
