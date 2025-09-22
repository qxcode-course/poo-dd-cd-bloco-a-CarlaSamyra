class Towel: 
    def __init__(self, color: str, size: str): #construtor
        self.color = color #atributos - define o estado da minha toalha 
        self.size = size
        self.wetness = 0

    def secar (self, amount: int) -> None:
        self.wetness += amount
        if self.wetness >= self.maximaUmidade():
            print("toalha encharcada")
            self.wetness = self.maximaUmidade()

    def maximaUmidade (self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0
        
    def __str__(self): #toString
        return f"Cor:{self.color}, Tamanho:{self.size}, Umidade:{self.wetness}"
    
    def isDry (self) -> bool :
        return self.wetness == 0
    
    def wringOut (self) -> None :
        self.wetness = 0

def main (): #2 função principal
    toalha = Towel ("", "") #3. objeto manipulado
    while True: #4. loop infinito
        line: str = input() #5. entrada de linha
        args: list[str] = line.split(" ") #6. lista de palavras 
        if args[0] == "end":
            break
        elif args[0] == "new":
            color = args[1]
            size = args[2]
            toalha = Towel(color, size)
        elif args[0] == "show":
            print(toalha)
        elif args[0] == "dry":
            amount: int = int(args[1])
            toalha.secar(amount)
        else:
            print ("fail: comando inválido")

main() #1. código inicia