from Source.errors import error_proxy
import unittest


class error_proxy_test(unittest.TestCase):
    def test_create_error_proxy(self):
        # Подготовка
        proxy = error_proxy()
        
        # Действие
        proxy.error = "test"
        
        # Проверка
        assert proxy.error == "test"
        
    def test_create_exception_error_proxy(self):
        # Подготовка
        proxy = error_proxy()
        
        try:
            # Действие
            proxy.error = ""
        except Exception as ex:
            proxy.set_error(ex)
            
        # Проверка
        print(proxy.error)
        assert proxy.error != ""    
            
            
    