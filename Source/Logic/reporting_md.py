from Source.Logic.reporting import reporting
from Source.exceptions import operation_exception


class reporting_md(reporting):

    def create(self, typeKey: str):
        super().create(typeKey)
        result = []

        items = self.data[typeKey]
        if items == None:
            raise operation_exception("Невозможно сформировать данные. Данные не заполнены!")

        if len(items) == 0:
            raise operation_exception("Невозможно сформировать данные. Нет данных!")

        result.append(f"# {typeKey}")

        header = ""
        line = ""
        for field in self.fields:
            header += f"|{field}"
            line += "|--"

        result.append(f"{header}|")
        result.append(f"{line}|")

        for item in items:
            row = ""
            for field in self.fields:
                value = getattr(item, field)
                if value is None:
                    value = ""

                row += f"|{value}"
            result.append(f"{row}|")

        return "\n".join(result)
