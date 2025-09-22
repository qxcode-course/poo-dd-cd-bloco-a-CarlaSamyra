class Towel: 
    def __init__(self, color: str, size: str): #construtor
        self.color = color #atributos
        self.size = size
        self.wetness = 0
    
    def __str__(self):
        return f"color:{self.color}, tam:{self.size}, hum:{self.wetness}"

towel = Towel("green", "G") #objetos
toalhas = Towel("red", "M") #objetos

print(towel.color)
towel.color = "Blue"
print(towel.color)
print(towel.size)
print(towel.wetness)

print(towel)