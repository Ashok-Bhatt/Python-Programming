class World:
    def __init__(self,country,language):
        self.country=country
        self.language=language
    
    def info(self):
        print(f"Name of country:{self.country} and the major language:{self.language}")
        
class Asia(World):
    def showcountry(self):
        print(f"The {self.country} lies in Asia.")

India=World("India","Hindi")
India.info()
China=Asia("China","Chinese")
China.info()
China.showcountry()