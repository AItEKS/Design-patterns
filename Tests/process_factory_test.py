import unittest
from datetime import datetime
from Source.Models.storage_row_model import storage_row_model
from Source.Logic.process_factory import process_factory
from Source.Logic.start_factory import start_factory


class process_factory_test(unittest.TestCase):
    def test_process_storage_turn(self):
        nomenclatures = start_factory.create_nomenclatures()
        units = start_factory.create_units()

        transaction1 = storage_row_model()
        transaction1.storage_name = "Storage1"
        transaction1.nomenclature = nomenclatures[0]
        transaction1.count = 10
        transaction1.type_tranzaction = True
        transaction1.unit = units[0]
        transaction1.period = datetime.now()

        transaction2 = storage_row_model()
        transaction2.storage_name = "Storage1"
        transaction2.nomenclature = nomenclatures[1]
        transaction2.count = 20
        transaction2.type_tranzaction = False
        transaction2.unit = units[1]
        transaction2.period = datetime.now()

        transaction3 = storage_row_model()
        transaction3.storage_name = "Storage1"
        transaction3.nomenclature = nomenclatures[2]
        transaction3.count = 30
        transaction3.type_tranzaction = True
        transaction3.unit = units[2]
        transaction3.period = datetime.now()

        transactions = [transaction1, transaction2, transaction3]

        process_factory_instance = process_factory()
        process_instance = process_factory_instance.create('storage_turn')

        result = process_instance.process(transactions)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].storage_name, "Storage1")
        self.assertEqual(result[0].turnover, 20)