import unittest
from Source.Logic.start_factory import start_factory


class create_journal_test(unittest.TestCase):
    def test_create_journal(self):
        factory = start_factory.create_journal()

        print(factory)