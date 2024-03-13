from Source.Logic.start_factory import start_factory
from Source.Logic.convert_factory import convert_factory

import unittest
import json


class convert_test(unittest.TestCase):
    def test_check_convert_nomenclature(self):
        # Подготовка
        items = start_factory.create_nomenclatures()
        factory = convert_factory()
        if len(items) == 0:
            raise Exception("Список номенклатуры пуст!")
        
        item = items[0]
        
        # Действие
        result = factory.serialize(item)
        
        # Проверки
        assert result is not None
        json_text = json.dumps(result, sort_keys = True, indent = 4)  
       
        file = open("nomenclature.json", "w")
        file.write(json_text)
        file.close()

    def test_check_convert_nomenctalures(self):
        # Подготовка
        items = start_factory.create_nomenclatures()
        factory = convert_factory()
        
        # Действие
        result = factory.serialize(items)
        
        # Проверки
        assert result is not None
        json_text = json.dumps(result, sort_keys = True, indent = 4)  
       
        file = open("nomenclatures.json", "w")
        file.write(json_text)
        file.close()

    def test_check_convert_receipts(self):
        # Подготовка
        items = start_factory.create_receipts()
        factory = convert_factory()
        
        # Действие
        result = factory.serialize(items)
        
        # Проверки
        assert result is not None
        json_text = json.dumps(result, sort_keys = True, indent = 4)  
       
        file = open("receipts.json", "w")
        file.write(json_text)
        file.close()
                