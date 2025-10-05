class Car:
    def __init__ (self, pas: int, gas: int, km: int):
        self.pas = 0
        self.gas = 0
        self.km = 0
        self.gasMax = 100 
        self.pasMax = 100

    def __str__ (self):
        return f"pass: {self.pas}, gas: {self.gas}, km: {self.km}"
    
    def enter (self):
        self.pas += 1
        if self.pas > 2:
            print ("fail: limite de pessoas atingido")
            self.pas = 2

    def leave (self):
        self.pas -= 1
        if self.pas < 0:
            print ("fail: nao ha ninguem no carro")
            self.pas = 0

    def fuel (self, increment: int):
        self.gas += increment
        if self.gas > self.gasMax:
            self.gas = 100
        
    def drive (self, distance: int):
        if self.pas == 0:
            print ("fail: nao ha ninguem no carro")
        elif self.gas == 0:
            print ("fail: tanque vazio")
        elif distance > self.gas:
            distancia = self.gas
            print (f"fail: tanque vazio apos andar {distancia} km")
            self.gas = 0
            self.km += distancia
        else:
            self.km += distance
            self.gas -= distance

            

def main():
    carro = Car ("", "", "")
    while True:
        line = input()
        args: list[str] = line.split(" ")
        print ("$" + line)
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(carro)
        elif args[0] == "enter":
            carro.enter()
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            increment: int = int(args[1])
            carro.fuel(increment)
        elif args[0] == "drive":
            distance: int = int(args[1])
            carro.drive(distance)
        else: 
            print ("fail: comando inválido")


main()