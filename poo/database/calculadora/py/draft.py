class Calc:
    def __init__ (self, batteryMax: int ):
        self.batteryMax = batteryMax
        self.display: float = 0.00
        self.battery: int = 0
    
    def __str__ (self):
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
    def charge (self, increment: int):
        self.battery += increment 
        if self.battery > self.batteryMax: 
            self.battery = self.batteryMax

    def sum (self, a: float, b: float):
        if self.battery > 0:
            self.display = a + b 
            self.battery -= 1
        else:
            print ("fail: bateria insuficiente")
    
    def div (self, den: float, num: float):
        if self.battery > 0:
            if den == 0 or num == 0:
                print ("fail: divisao por zero")
                self.battery -= 1
            else:
                self.display = den / num 
                self.battery -= 1
        else:
            print ("fail: bateria insuficiente")
        

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
        elif args[0] == "charge":
            increment: int = int(args[1])
            calculadora.charge(increment)
        elif args[0] == "sum":
            a: float = float(args[1])
            b: float = float(args[2])
            calculadora.sum(a, b)
        elif args[0] == "div":
            den: float = float(args[1])
            num: float = float(args[2])
            calculadora.div(den, num)
        else:
            print("fail: comando inválido")
main()