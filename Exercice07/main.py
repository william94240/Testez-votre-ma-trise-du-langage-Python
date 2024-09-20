## Écrivez votre code ici !
def square(x):
    """
    Retourne le carré de x
    args: x   Nombre à mettre au carré.
    return: x²  Carré de x.
    """
    try:
        return x ** 2
    except TypeError as e:
        print("Le paramètre doit être un nombre !")
        
       


print(square(45))
      
