## Écrivez votre code ici !

class Person:
    """Classe pour représenter une personne avec un nom et un âge.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):   
        print("Nom:", self.name, "\nAge:", self.age)
       

class Employee(Person):
    """Classe pour représenter un employé avec un nom, un âge et un salaire.
    """
    def __init__(self, name, age, salary):
        super().__init__(self, name, age)
        self.salary = salary
    
    def display_details(self):
        super().display_details()
        print("Salaire:", self.salary)



