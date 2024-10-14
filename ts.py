# Klasa
class Computer():
    # Konstruktor
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def __str__(self):
        return f"To jest komputer {self.brand}, który kosztuje {self.price}"

# instancja klasy
computerOne = Computer('Dell', 10000)
computerTwo = Computer('Apple', 15000)

print(computerOne)
print(computerTwo)

print('-------------------------------------------------------------')


# Metoda => jest definiowana wewnątrz klasy, a funkcja to samodzielny blok kodu:
# Properties => Metoda z właściwościami  
class Car():
    def myMethod(self, direct):
        return f"Skręć w {direct}"
    
car = Car()

print(car.myMethod('prawo'))


print('-------------------------------------------------------------')


# Self - musi być zawsze w metodzie bo będziemy mieć błąd:
class Calc():
    def add(self, a, b):
        return a + b
    
myCalc = Calc()

print(myCalc.add(10, 20))


print('-------------------------------------------------------------')


# __str__ a __repr__
# __str__ - służy do wyświetlania (printu) dla użytkownika 
# __repr__ - służy do debugowania 
class Person ():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def __str__(self):
        return f"Personel: {self.name} ma {self.age} lat"
    
    def __repr__(self):
        return f"Osoba (imie='{self.name}', wiek='{self.age}')"
    
personeOne = Person('Jan', 21)
personeTwo = Person('Wiesław', 23)

print(personeOne)
print(personeTwo.__repr__)

print('-------------------------------------------------------------')

# Pola statyczne:
# Dla różnych instancji klas pole statyczne będzie takie samo 
# Dla różnych instancji klas self jest różne 
class Run():
    shoes = 'buty'

    def __init__(self, kind):
        self.kind = kind

runnerOne = Run('Nike')
runnerTwo = Run('Adidas')

print(id(runnerOne.shoes))
print(id(runnerTwo.shoes))

print(id(runnerOne.kind))
print(id(runnerTwo.kind))


print('-------------------------------------------------------------')

# Dziedziczenie - czyli JEST - coś dziedziczy po czymś 
class Food():
    def __init__(self, weight):
        self.weight = weight

class Fish(Food):
    def __init__(self, kind, weight):
        self.kind = kind
        super().__init__(weight)

    def __str__(self):
        return f"Ryba: {self.kind} waży {self.weight} gramów"


firstFish = Fish('Dorsz', 500)
secondFish = Fish('Karp', 2000)

print(firstFish)
print(secondFish)


print('-------------------------------------------------------------')


# Kompozycja czyli MA - łączenie obiektów za pomocą MA
class Chciken():
    def __init__(self, weight):
        self.weight = weight


class Protein():
    def __init__(self, macro):
        self.macro = macro


chicken = Protein(25)
myAllFood = Chciken(chicken)

print(myAllFood.weight.macro)

print('-------------------------------------------------------------')

# Hermetyzacja - ukrywanie atrybutów i metod w klasach. 
# Stan obiektu jest chroniony i nie może być przypadkowo lub bezpośrednio zmieniany przez inne część programu:
class Gym():
    def __init__(self, name):
        self.__name = name

    # Getery pozwalają na odczytanie wartości prywatnych 
    def getMyPrivate(self):
        return f"{self.__name}"


gymOne = Gym('Zdrofit')

print(gymOne.getMyPrivate())

# Hermetyzacja i zmiana ukrytych wartości czyli Setery:
class Weather():
    def __init__(self, kind):
        self.__kind = kind

    def set_kind(self, newValue):
        self.__kind = newValue
        return f"Pogoda: {newValue}"

weather = Weather('słoneczna')

newWeather = weather.set_kind = 'pochmurnie'

print(newWeather)


print('-------------------------------------------------------------')

# Polimorfizm 
# Różne Klasy, które wykorzystują te same metody, ale wykonują co innego

class Dog():

    def speak(self):
        return f"Szczekam"
    

class Cat():

    def speak(self):
        return f"Miauczę"
    

def soundAnimals(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(soundAnimals(dog))
print(soundAnimals(cat))


print('-------------------------------------------------------------')

# @staticmethod i @classmethod

# @staticmethod:
# możemy ją wywoływać bezpośrednio z klasy
# Nie wymaga argumetu self

class Today():

    @staticmethod
    def myDay():
        return f"Dzisiaj idę na trening"


print(Today.myDay())

# @classmethod 
# ma dostep do argumentów - pola statycznego przez cls
# można wywoływać bez tworzenia instancji klasy
class Weather():

    weather = 'słonecznie'

    @classmethod
    def today(cls):
        return f"{cls.weather}"
    
print(Weather.today())

print('-------------------------------------------------------------')

# Wzorce projektowe - FABRYKA - do parsowania plików 
from abc import ABC, abstractmethod
import pandas as pd

class Parser(ABC):
    
    @abstractmethod
    def pars(self, path):
        pass


class CSVParse(Parser):

    def pars(self, path):
        return pd.read_csv(path, encoding='ISO-8859-1', sep=";")
    


class XLSXParse(Parser):

    def pars(self, path):
        return pd.read_excel(path, encoding='ISO-8859-1')
    


class FactorParser():

    def get_pars(self, path):

        if path.endswith(".csv"):
            return CSVParse()
        
        elif path.endswith(".xlsx"):
            return XLSXParse()
        
        else:
            raise ValueError("Zły format pliku")
        

factor = FactorParser()

your_file = factor.get_pars("./data.csv")

print(your_file.pars("./data.csv"))

print('-------------------------------------------------------------')


# SOLID 
# S - każda klasa powinna dotyczyć swoich funkcjonalności 
# O - Klasa powinna umożliwiać rozbudowę o nowe funkcjonalności a nie modyfikację 
# L - Każda klasa pochodna powinna korzystać z odpowiedniej dla nich klas bazowch 
class Flyable():
    def fly(self):
        pass


class Swimable():
    def swim(self):
        pass


class Bird(Flyable):
    def fly(self):
        return f"Latam"

class Fish(Swimable):
    def swim(self):
        return f"Pływam"

bird = Bird()
fish = Fish()

print(bird.fly())
print(fish.swim())


# I - jeżeli mamy klasę i ona nic nie robi to jej nie usuwamy tylko dajemy pass
# D - Wysokopoziomowe moduły (te główne) nie powinny zależeć od nisko poziomowych modułów (tych bardziej szczegółowych) jedynie od abstrakcji

print('-------------------------------------------------------------')

# mutable i nonmutable w Pythonie 
# mutable - czyli te które możemy zmienic: list, słownik, zbiory 
my_list = [1, 2, 3]
my_list.append(4)

my_dict = {"kot": "cat", "pies": "dog"}

my_dict["ptak"] = "bird"

print(my_list)
print(my_dict)

# non-mutable - nie mutowalne są STRINGI oraz TUPLE czyli KROTKI - nie można ich zmienic
krotka = (1, 2, 3)
my_string = "test"

print('-------------------------------------------------------------')














