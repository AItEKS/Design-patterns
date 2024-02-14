import unittest
from Source.Models.unit import unit_model


class test_unit_model(unittest.TestCase):
    def setUp(self):
        self.unit = unit_model("Length")
        self.unit.base_unit = "m"
        self.unit.unit_ratio = "1"

    def test_init(self):
        self.assertEqual(self.unit.name, "Length")
        self.assertEqual(self.unit.base_unit, "m")
        self.assertEqual(self.unit.unit_ratio, "1")

    def test_set_base_unit(self):
        self.unit.base_unit = "mm"
        self.assertEqual(self.unit.base_unit, "mm")

    def test_set_unit_ratio(self):
        self.unit.unit_ratio = "1000"
        self.assertEqual(self.unit.unit_ratio, "1000")
