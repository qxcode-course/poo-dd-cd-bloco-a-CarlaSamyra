class Animal:
    def __init__ (self, species: str, sound: str):
        self.species: str = species 
        self.sound: str = sound
        self.age: str = 0 

    def __str__ (self):
        return f"{self.species}:{self.age}:{self.sound}"
    

def main():
    animal = Animal ("", "")

    while True: 
        line = input()
        args: list[str] = line.split(" ")
        print ("$" + line)

        if args[0] == "end":
            break

        elif args[0] == "init":
            species = args[1]
            sound = args[2]
            animal = Animal(species, sound)

        elif args[0] == "show":
            print (animal)






main()
