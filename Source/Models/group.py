from Source.abstract_reference import abstract_reference


class group_model(abstract_reference):

    def create_group(self):
        item = group_model('Ингридинты')
        return item