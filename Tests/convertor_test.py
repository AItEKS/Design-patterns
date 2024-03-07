import datetime
import unittest
from Source.Logic.convert_factory import convert_factory
from Source.exceptions import argument_exception


class convert_factory_test(unittest.TestCase):
    def setUp(self):
        self.factory = convert_factory()

    def test_convert_object_int(self):
        result = self.factory.convert_object(10)
        expected_result = "Converted int: 10"
        self.assertEqual(str(result), expected_result)

    def test_convert_object_float(self):
        result = self.factory.convert_object(3.14)
        expected_result = {'value': 3.14}
        self.assertEqual(result, expected_result)

    def test_convert_object_str(self):
        result = self.factory.convert_object("Hello")
        expected_result = "Converted str: Hello"
        self.assertEqual(str(result), expected_result)

    def test_convert_object_datetime(self):
        dt = datetime.datetime(2024, 3, 7)
        result = self.factory.convert_object(dt)
        expected_result = {'datetime_value': '2024-03-07 00:00:00'}
        self.assertEqual(result, expected_result)

    def test_convert_object_invalid_type(self):
        with self.assertRaises(argument_exception):
            self.factory.convert_object(True)