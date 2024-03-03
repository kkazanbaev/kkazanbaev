import unittest
from Src.Logics.reporting import reporting
from Src.Models.unit_model import unit_model
from Src.Models.group_model import group_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Storage.storage import storage
from Src.Logics.csv_reporting import csv_reporting
from Src.Logics.json_reporting import json_reporting
from Src.Logics.markdown_reporting import markdown_reporting
from Src.settings_manager import settings_manager


class reporting_test(unittest.TestCase):
    
    # (Тест не работает)
    # Проверить статический метод build класса reporting
    def test_check_reporting_build(self):
        # Подготовка
        data = {}
        list = []
        item = unit_model.create_gram()
        list.append(item)
        data[  storage.unit_key()  ] = list 
        
        # Дейстие
        result = reporting.build(storage.unit_key(), data)
        
        # Проверки
        assert result is not None
        assert len(result) > 0
        

    # Проверка формирования отчета в csv   
    def test_check_csv_create(self):
        # Подготовка
        data = {}
        list = []
        item = unit_model.create_gram()
        list.append(item)
        data[storage.unit_key()] = list 
        manager = settings_manager()
        report = csv_reporting(manager.settings , data)
        
        # Действие
        result = report.create(storage.unit_key())
        
        # Проверки
        assert result is not None
        assert len(result) > 0


    # Проверка формирования отчета в json
    def test_check_json_create(self):
        # Подготовка
        data = {}
        list = []
        item = group_model("Ингредиенты")
        list.append(item)
        data[storage.group_key()] = list 
        manager = settings_manager()
        report = json_reporting(manager.settings , data)

        # Действие
        result = report.create(storage.group_key())

        # Проверки
        assert result is not None
        assert len(result) > 0


    # Проверка формирования отчета в markdown
    def test_check_json_create(self):
        # Подготовка
        data = {}
        list = []
        item = nomenclature_model("Пшеничная мука")
        item.group = group_model.create_default_group()
        item.unit = unit_model.create_killogram()
        list.append(item)
        data[storage.group_key()] = list 
        manager = settings_manager()
        report = json_reporting(manager.settings , data)

        # Действие
        result = report.create(storage.nomenclature_key())

        # Проверки
        assert result is not None
        assert len(result) > 0