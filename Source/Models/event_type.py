from Source.reference import reference


#
# Типы событий
#
class event_type(reference):
 
    @staticmethod
    def changed_block_period() -> str:
        """
            Событие изменения даты блокировки
        Returns:
            str: _description_
        """
        return "changed_block_period"

    @staticmethod
    def nomenclature_deleted() -> str:
        """
            Событие удаления номенклатуры из рецептов
        Returns:
            str: Событие удаления номенклатуры из рецептов
        """
        return "nomenclature_deleted"