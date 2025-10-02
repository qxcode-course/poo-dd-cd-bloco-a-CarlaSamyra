class Calc:
    def __init__ (self, batteryMax: int ):
        self.batteryMax = batteryMax
        self.display: float = 0.00
        self.battery: int = 0
    
    def __str__ (self):
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
    
        


    

def main():
    while True:
        line = input()
        args: list[str] = line.split(" ")
        print ("$" + line)

        if args[0] == "end":
            break 
        elif args[0] == "init":
            batteryMax = int(args[1])
            calculadora: Calc = Calc (batteryMax)
        elif args[0] == "show":
            print(calculadora)
        else:
            print("fail: comando inválido")

    

main()