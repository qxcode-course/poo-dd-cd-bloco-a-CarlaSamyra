class Car:
    def __init__ (self, pas: int, km: int, gas: int):
        self.pas: int = 0 
        self.km: int = 0
        self.gas: int = 0

    def __str__ (self):
        return f"pass: {self.pas}, gas: {self.gas}, km: {self.km}"
    
    def pasMax (self):
        self.pas += 1
        if self.pas > 2:
            print ("fail: limite de pessoas atingido")
            self.pas = 2
    
    def leave (self):
        self.pas -= 1
        if self.pas < 0:
            print ("fail: nao ha ninguem no carro")
            self.pas = 0

    def gasMax (self, amount: int):
        self.gas += amount 
        if self.gas > 100:
            self.gas = 100

    
    def drive (self, distance: int):
        if self.gas == 0:
            print ("fail: tanque vazio")
            return
        if self.pas == 0:
            print ("fail: nao ha ninguem no carro")
            return 
        if distance > self.gas:
            distancia = self.gas 
            print (f"fail: tanque vazio apos andar {distancia} km")
            self.km = self.km + distancia 
            self.gas = 0
            return
        if distance < self.gas:
            self.gas -= distance
            self.km = distance 
            return


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
            carro.pasMax()
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            amount: int = int (args[1])
            carro.gasMax(amount)
        elif args[0] == "drive":
            distance: int = int (args[1])
            carro.drive(distance)

            




main()