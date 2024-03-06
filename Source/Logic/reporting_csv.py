from Source.Logic.reporting import reporting
from Source.exceptions import operation_exception


class reporting_csv(reporting):

    def create(self, typeKey: str):
        super().create(typeKey)
        result = ""
        delimetr = ";"

        items = self.data[typeKey]
        if items == None:
            raise operation_exception("Невозможно сформировать данные. Данные не заполнены!")

        if len(items) == 0:
            raise operation_exception("Невозможно сформировать данные. Нет данных!")

        header = delimetr.join(self.fields)
        result += f"{header}\n"

        for item in items:
            row = ""
            for field in self.fields:
                value = getattr(item, field)
                if value is None:
                    value = ""

                row += f"{value}{delimetr}"

            result += f"{row[:-1]}\n"

        return result
