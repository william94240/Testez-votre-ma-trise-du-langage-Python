# Fonction calculate_average
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.
    args: numbers   List of numbers.
    return: average  Average of the numbers.
    """
    # Calcul de la moyenne
    average = sum(numbers) / len(numbers)
    return average
 
# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
