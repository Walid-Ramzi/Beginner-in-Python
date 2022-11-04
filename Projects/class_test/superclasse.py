class Batiment:
    def __init__(self, name, address, etage):
        self.name = name
        self.address = address
        self.etage = etage

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_etage(self):
        return self.etage

class immeuble(Batiment):
    def __init__(self, name, address, etage, balcons):
        super().__init__(name, address, etage)
        self.balcons = balcons

    def get_balcons(self):
        return self.balcons


class supermarche(Batiment):
    def __init__(self, name, address, etage, rayon):
        super().__init__(name, address, etage)
        self.rayon = rayon

    def get_rayon(self):
        return self.rayon

class bank(Batiment):
    def __init__(self, name, address, etage, coffre):
        super().__init__(name, address, etage)
        self.coffre = coffre

    def get_coffre(self):
        return self.coffre


print("welcome to our batiment what do you need : ""\n" "1/ immeuble""\n" "2/ supermarche""\n" "3/ bank")
choice = input("answer here :")
if choice in ("immeuble", "1"):
    n = int(input("how many :"))
    for i in range(n):
        imname = immeuble(input("Name : "), input("Address : "), int(input("Etages : ")), int(input("Balcons : ")))
        print()
        print(" Name :", imname.get_name(), "\n", "Address :", imname.get_address(), "\n",
              "Etages :", imname.get_etage(), "\n", "Balcons :", imname.get_balcons())
        print()
elif choice in ("supermarche", "2"):
    n = int(input("how many :"))
    for i in range(n):
        imname = supermarche(input("Name : "), input("Address : "), int(input("Etages : ")), int(input("rayons : ")))
        print()
        print(" Name :", imname.get_name(), "\n", "Address :", imname.get_address(), "\n",
              "Etages :", imname.get_etage(), "\n", "rayons :", imname.get_rayon())
        print()
elif choice in ("bank", "3"):
    n = int(input("how many :"))
    for i in range(n):
        imname = bank(input("Name : "), input("Address : "), int(input("Etages : ")), int(input("coffre : ")))
        print()
        print(" Name :", imname.get_name(), "\n", "Address :", imname.get_address(), "\n",
              "Etages :", imname.get_etage(), "\n", "coffre :", imname.get_coffre())
        print()
