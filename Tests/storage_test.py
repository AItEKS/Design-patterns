import unittest
from datetime import datetime
from Source.Models.storage_row_model import storage_row_model
from Source.Models.unit import unit_model
from Source.Models.nomenclature import nomenclature_model
from Source.Logic.start_factory import start_factory


class storage_test(unittest.TestCase):
    def test_create_journal(self):
        journal = start_factory.create_journal()

        self.assertTrue(len(journal) > 0)
        for transaction in journal:
            self.assertIsInstance(transaction, storage_row_model)
            self.assertIsInstance(transaction.storage_name, str)
            self.assertIsInstance(transaction.nomenclature, nomenclature_model)
            self.assertIsInstance(transaction.count, int)
            self.assertIsInstance(transaction.type_tranzaction, bool)
            self.assertIsInstance(transaction.unit, unit_model)
            self.assertIsInstance(transaction.period, datetime)

