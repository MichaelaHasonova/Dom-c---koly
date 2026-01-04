import math


class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property(Locality):
    def __init__(self, name, locality_coefficient, locality):
        super().__init__(name, locality_coefficient)
        self.locality = locality

class Estate(Property):
    def __init__(self, name, locality_coefficient, locality, estate_type, area):
        super().__init__(name, locality_coefficient, locality)
        self.estate_type = estate_type
        self.area = area
    
    def __str__(self):
        return f"Pozemek {self.name}, lokalita {self.locality} (koeficient {self.locality_coefficient}), {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."
    
    def calculate_tax(self):
        if self.estate_type == "land":
            estate_type_coefficient = 0.85
        if self.estate_type == "building_site":
            estate_type_coefficient = 9
        if self.estate_type == "forrest":
            estate_type_coefficient = 0.35
        if self.estate_type == "garden":
            estate_type_coefficient = 2 
        
        tax = math.ceil(self.area * estate_type_coefficient * self.locality_coefficient)
        return tax

class Residence(Property):
    def __init__(self, name, locality_coefficient, locality, area, commercial):
        super().__init__(name, locality_coefficient, locality)
        self.area = area
        self.commercial = commercial
    
    def calculate_tax(self):
        if self.commercial == True:
            return math.ceil(self.area * self.locality_coefficient * 15 * 2)
        else:
            return math.ceil(self.area * self.locality_coefficient * 15)
        
    def __str__(self):
        return f"Pozemek {self.name}, lokalita {self.locality} (koeficient {self.locality_coefficient}), {self.area} metrů čtverečních, daň {self.calculate_tax()} Kč."

zemedelsky_pozemek = Estate("Zemědělský pozemek", 0.8, "Manětín", "land", 900)
dum = Residence("Dům", 0.8, "Manětín", 120, False)
kancelar = Residence("Kancelář", 3, "Brno", 90, True)

print(zemedelsky_pozemek.calculate_tax())
print(dum.calculate_tax())
print(kancelar.calculate_tax())

print(zemedelsky_pozemek)
print(dum)
print(kancelar)
