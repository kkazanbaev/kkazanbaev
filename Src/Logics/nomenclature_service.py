from Src.Logics.convert_factory import convert_factory
from Src.Logics.process_factory import process_factory
from Src.Logics.storage_prototype import storage_prototype
from Src.exceptions import argument_exception, exception_proxy, operation_exception
from Src.Models.nomenclature_model import nomenclature_model
from Src.Models.receipe_model import receipe_model
from Src.Models.storage_model import storage_model
from Src.Models.receipe_row_model import receipe_row_model
from Src.Storage.storage import storage

from datetime import datetime
import json

class nomenclature_service:
    __data = []
    
    def __init__(self, data: list) -> None:
        if len(data) == 0:
            raise argument_exception("Некорректно переданы параметры!")
        
        self.__data = data
        
    # Набор основных методов    
    
    def add_nomenclature (self, nomenclature: nomenclature_model) -> list:
        """
            Добавление новой номенклатуры в базу данных
            Если номенклатура не найдена - вывести ошибку
        """
        exception_proxy.validate(nomenclature, nomenclature_model)
        
        if nomenclature in  self.__data:
            raise operation_exception("Такая номенклатура уже существует")
        
        self.__data.append(nomenclature)
        
        if self.get_nomenclature(nomenclature.id) == nomenclature:
            return True
        
        return False
    
    def get_nomenclature(self, id: str) -> nomenclature_model:
        """
            Получить номенклатуру по ее идентификатору
        """
        for item in self.__data:
            if item.id == id:
                return item
            
        raise operation_exception('Номенклатура с таким ID не найдена')
    
    def  delete_nomenclature(self, id: int) -> list:
        """
            Удалить номенклатуру из списка
            Если номенклатура не найдена - вывести ошибку
        """
        nom = self.get_nomenclature(id)
        #Если номенклатура не будет удалена, то возникнет ValueError, возвращать False не требуется
        self.__data.remove(nom)
        
        return True
    
    def  update_nomenclature(self, nomenclature: nomenclature_model) -> list:
        """
            Обновить существующую номенклатуру в списке
            Если номенклатура не найдена - вывести ошибку
        """
        exception_proxy.validate(nomenclature, nomenclature_model)
        old_nomenclature = self.get_nomenclature(nomenclature.id)
        
        # Проверяем что указанный идентификатор есть в нашей базе данных
        if old_nomenclature is None:
            raise operation_exception("Номенклатура не найдена")
        
        # Заменяем старый объект новым
        index = self.__data.index(old_nomenclature)
        self.__data[index] = nomenclature
        
        return self.__data
        
    # Набор основных методов
    def data(self) -> list:
        """
            Получить список всей номенклатуры
        Returns:
            list: _description_
        """
        return self.__data    