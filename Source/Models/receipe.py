from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.unit_model import unit_model
from Src.reference import reference
from Src.exceptions import argument_exception, exception_proxy

class receipe_model(reference):
    __nomenclature: nomenclature_model = None
    __size: int = 0
    __unit: unit_model = None

    def __init__(self, __nomenclature: nomenclature_model, __size: int, __unit: unit_model):
        exception_proxy.validate(__nomenclature, reference)
        exception_proxy.validate(__unit, reference)

        self.__nomenclature = __nomenclature
        self.__size = __size
        self.__unit = __unit

        super().__init__(__nomenclature.name)