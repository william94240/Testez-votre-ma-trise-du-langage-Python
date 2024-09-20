class Book:
    """Classe représentant un livre
    """
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    """Classe représentant une bibliothèque
    """
    def __init__(self):
        self.books = []
        self.borrow_books = []
    # Ajouter les méthodes ici

    def add_book(self, book):
        """Ajoute un livre à la bibliothèque
        """
        self.books.append(book)

    def remove_book(self, book_title):
        """Supprime un livre de la bibliothèque en utilisant le titre du livre comme argument.
        """
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return

    def borrow_book(self, book_title):
        """Emprunte un livre de la bibliothèque en utilisant le titre du livre comme argument.
        """
        # Le livre doit être retiré de la liste des livres disponibles et ajouté dans la liste des livres empruntés.
        for book in self.books:
            if book.title == book_title:
                self.borrow_books.append(book)
                self.books.remove(book)
                return

    def return_book(self, book_title):
        """Retourne un livre à la bibliothèque en utilisant le titre du livre comme argument.
        """
        # Le livre doit être retiré de la liste des livres empruntés et ajouté dans la liste des livres disponibles.
        for book in self.borrow_books:
            if book.title == book_title:
                self.books.append(book)
                self.borrow_books.remove(book)
                return 


    def available_books(self):
        """Retourne la liste des livres disponibles.
        """
        return [print(book.title) for book in self.books] 

    def borrowed_books(self):
        """Retourne la liste des livres empruntés.
        """
        return [print(book.title) for book in self.borrow_books] 
