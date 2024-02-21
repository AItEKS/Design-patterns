from Source.abstract_reference import abstract_reference

class storage_model(abstract_reference):
    def __init__(self, name):
        super().__init__(name)
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe):
        if recipe in self.recipes:
            self.recipes.remove(recipe)

    def get_recipes(self):
        return self.recipes