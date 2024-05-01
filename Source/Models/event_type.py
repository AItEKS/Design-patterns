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
    def deleted_nomenclature() -> str:
        """
            Событие о удалении номенклатуры
        Returns:
            str: _description_
        """
        return "deleted_nomenclature"

    @staticmethod
    def log_entry(log_entry) -> str:
        """
        Event for a new log entry.
        """
        return "log_entry"