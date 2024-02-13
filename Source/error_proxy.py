

class error_proxy:
    __error_text = ""
    __error_source = ""
    __is_error = False
    
    
    def __init__(self, error_text: str = "", error_source: str = "") -> None:
        self.error_source = error_source
        self.error_text = error_text
        
    
    @property    
    def error_text(self):
        """
            Текст сообщения
        Returns:
            _type_: _description_
        """
        return self.__error_text
    
    
    @error_text.setter
    def error_text(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректно передан аргумент!")
        
        if(value.strip() ==""):
            self.__is_error = False
            return
            
        self.__error_text = value.strip()
        self.__is_error = True
        
        
    @property    
    def error_source(self):
        """
            Источник ошибки
        Returns:
            _type_: _description_
        """
        return self.__error_source
    
    
    @error_source.setter
    def error_source(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректно передан аргумент!")
        
        if(value.strip() ==""):
            return
            
        self.__error_source = value.strip()
    
        
    @property
    def is_error(self):
        """
            Флаг. Есть ошибка
        """
        return self.__is_error  
        
        
    def set_error(self, exception: Exception):
        """
            Сохранить ошибку
        Args:
            exception (Exception): _description_
        """
        if not isinstance(exception, Exception):
            self.error_text = "Некорректно переданы параметры!"
            self.error_source = "set_error" 
            return

        if exception is not None:        
            self.error_text = f"ОШИБКА! {str(exception)}"
            self.error_source = f"ИСКЛЮЧЕНИЕ! {type(exception)}"
        else:
            self.error_text = ""
            
                
        
        
                    
        
        
        
        