from Source.Logic.convertor import convertor
from Source.Logic.convert_factory import convert_factory


class reference_convertor(convertor):
    def convert(self, field: str, object) -> dict:
        factory = convert_factory()
        return factory.convert(object)
