from Source.error_proxy import error_proxy
import unittest
from Source.operation_exception import operation_exception
from Source.argument_exception import argument_exception

class test_errors(unittest.TestCase):
    def test_check_argument_exception(self):
        # Подготовка

        # Действие
        try:
            raise argument_exception("Test")
        except argument_exception as ex:
            # Проверка
            print(ex.error.error_text)
            print(ex.error.error_source)

            assert ex.error.is_error
            return

        assert 1 != 1

    def test_check_set_exception(self):
        # Подготовка
        error = error_proxy()

        # Действие
        try:
            result = 1 / 0
        except Exception as ex:
            error.set_error(ex)

        # Проверки
        assert error.is_error == True

    def test_check_set_error_text(self):
        # Подготовка
        error = error_proxy("Test", "Test")

        # Действие

        # Проверки
        assert error.is_error == True