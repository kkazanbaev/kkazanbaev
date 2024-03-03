from Src.Logics.reporting import reporting

class markdown_reporting(reporting):
    
    def create(self, typeKey: str):
        super().create(typeKey)
        result = ""

        # Исходные данные
        items = self.data[typeKey]
        
        # Список 
        for item in items:   
            for field in self.fields:
                result += f"| {field}: {item.__dict__[field]}"
                
            result += "|\n"
        
        # Результат markdown
        return result