import random

class Book:
    def __init__(self, title, author, published_year, genre,  page_number, checked_out=False):
        self.id = random.randint(100000, 9999999)
        self.title = title
        self.author = author
        self.published_year = published_year
        self.genre = genre
        self.page_number = page_number
        self.checked_out = checked_out
  
    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"You have checked out '{self.title}'."
        else:
            return f"'{self.title}' is already checked out."

    def return_book(self):
        if self.checked_out:
            self.checked_out = False
            return f"You have returned '{self.title}'."
        else:
            return f"{self.title} was not checked out."

    def book_info(self):
        status = "Checked out" if self.checked_out else "Available"
        return f"{self.id},{self.title},{self.author},{self.published_year},{self.genre},{self.page_number},{status}"

    
    def is_checked_out(self):
        return self.checked_out

    def update_info(self, title=None, author=None, published_year=None, genre=None, page_number=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if published_year:
            self.published_year = published_year
        if genre:
            self.genre = genre
        if page_number:
            self.page_number = page_number
        return f"Information for '{self.title}' has been updated."
    
    def __str__(self):
        return f"{self.id:<15} {self.title:<30} {self.author:<30} {self.published_year:<25} {self.genre:<30} {self.page_number:<30} {'Checked out' if self.checked_out else 'Available':<30}"
    
    def __eq__(self,other):
        return self.id == other.id


def create_book(title, author, published_year, genre, page_number):
    return Book(title, author, published_year, genre, page_number)

def find_book(book,book_list):
    for b in book_list:
        if b == book:
            return b
    return None

def delete_book(book, book_list):
    for b in book_list:
        if b == book:
            book_list.remove(b)
            return book_list
    return None
    
def add_book(book, book_list):
    book_list.append(book)
    return book_list    

def list_books(book_list):
    for book in book_list:
        print(book)

def list_available_books(book_list):
    for book in book_list:
        if not book.checked_out:
            print(book)

def list_checked_out_books(book_list):            
    for book in book_list:
        if book.checked_out:
            print(book)
            

