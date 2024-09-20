class Rectangle:
    """
    Classe Rectangle
    """
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        """
        Calcul de l'aire du rectangle
        """
        return self.width * self.length

    def calculate_perimeter(self):
        """
        Calcul du périmètre du rectangle
        """
        return 2 * (self.width + self.length)

# Test de la classe Rectangle
rectangle = Rectangle(5, 3) # 5:width & 3:length
print("Largeur:", rectangle.width)
print("Longueur:", rectangle.length)
print("Aire:", rectangle.calculate_area())
print("Périmètre:", rectangle.calculate_perimeter())

