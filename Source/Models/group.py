from Source.abstract_reference import abstract_reference


#
# Модель группу номенклатуры
#

class group_model(abstract_reference):
    @staticmethod
    def create_default_group():
        item = group_model("Ингредиенты")
        return item
