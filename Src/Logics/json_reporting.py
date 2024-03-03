from Src.Logics.reporting import reporting
import json

class json_reporting(reporting):
    
    def create(self, typeKey: str):
        super().create(typeKey)
        result = []

        # Исходные данные
        items = self.data[typeKey]

        # Список
        for item in items:
            dict1 = {}
            for field in self.fields:
                dict1[field] = item.__dict__[field]
            
            result.append(dict1)
        
        result = json.dumps(result)

        # Результат json
        return result