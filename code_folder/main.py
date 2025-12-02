import books
import os

def main():
    choice = ''
    book_list = []
    with open("data_folder/books.txt", "r") as f:
        if os.path.getsize("data_folder/books.txt") != 0:
            for line in f:
                id,title, author, published_year, genre, page_number, checked_out = line.strip().split(',')
                book = books.create_book(title, author, published_year, genre, int(page_number))
                book.checked_out = checked_out == 'Checked out'
                book.id = int(id)
                book_list.append(book)
    
    while choice != '0':
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List All Books")
        print("3. List Available Books")
        print("4. List Checked Out Books")
        print("5. Check Out Book")
        print("6. Return Book")
        print("7. Update Book Information")
        print("8. Search Book")
        print("9. Delete Book")
        print("0. Exit")
        print("\n")
        choice = input("Enter your choice: ")
        print("\n")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            published_year = input("Enter published year: ")
            genre = input("Enter genre: ")
            page_number = input("Enter page number: ")
            new_book = books.create_book(title, author, published_year, genre, page_number)
            books.add_book(new_book, book_list)
            with open("data_folder/books.txt", "a") as f:
                f.write(new_book.book_info()+ '\n')
            print(f"Book '{title}' added successfully.")

        elif choice == '2':
            print("\nAll Books:")
            print("ID               Title                          Author                        Published Year               Genre                         Page Number                  Status                        ")
            print("-" * 180)
            books.list_books(book_list)

        elif choice == '3':
            print("\nAvailable Books:")
            print("ID               Title                          Author                        Published Year               Genre                         Page Number                  Status                        ")
            print("-" * 180)
            books.list_available_books(book_list)

        elif choice == '4':
            print("\nChecked Out Books:")
            print(" ID              Title                          Author                        Published Year               Genre                         Page Number                  Status                        ")
            print("-" * 180)
            books.list_checked_out_books(book_list)

        elif choice == '5':
            book_id = int(input("Enter the ID of the book to check out: "))
            found = False
            for book in book_list:
                if book.id == book_id:
                    if not book.is_checked_out():
                        book.checked_out = True
                        print(f"You have checked out '{book.title}'.")
                        found = True
                        break
                    else:
                        print(f"Sorry, '{book.title}' is already checked out.")
                        found = True
                        break   
            if not found:
                print(f"Book with ID '{book_id}' not found in the library.")
            with open("data_folder/books.txt", "w") as f:
                    for b in book_list:
                        f.write(b.book_info() + '\n') 

        elif choice == '6':
            book_id = int(input("Enter the ID of the book to return: "))
            found = False
            for book in book_list:
                if book.id == book_id:
                    if book.is_checked_out():
                        book.checked_out = False
                        print(f"You have returned '{book.title}'.")
                        found = True
                        break
                    else:
                        print(f"'{book.title}' was not checked out.")
                        found = True
                        break   
            if not found:
                print(f"Book with ID '{book_id}' not found in the library.")
            with open("data_folder/books.txt", "w") as f:
                    for b in book_list:
                        f.write(b.book_info() + '\n')
        
        elif choice == '7':
            book_id = int(input("Enter the ID of the book to update: "))
            found = False
            for book in book_list:
                if book.id == book_id:
                    title = input("Enter new title (leave blank to keep current): ")
                    author = input("Enter new author (leave blank to keep current): ")
                    published_year = input("Enter new published year (leave blank to keep current): ")
                    genre = input("Enter new genre (leave blank to keep current): ")
                    page_number = input("Enter new page number (leave blank to keep current): ")
                    book.update_info(
                        title=title if title else None,
                        author=author if author else None,
                        published_year=published_year if published_year else None,
                        genre=genre if genre else None,
                        page_number=int(page_number) if page_number else None
                    )
                    print(f"Information for '{book.title}' has been updated.")
                    found = True
                    break
            if not found:
                print(f"Book with ID '{book_id}' not found in the library.")
            with open("data_folder/books.txt", "w") as f:
                    for b in book_list:
                        f.write(b.book_info() + '\n')

        elif choice == '8':
            book_id = int(input('Enter the ID of the book to be searched: '))
            found = False
            for book in book_list:
                if book.id == book_id:
                    found = True
                    print("Book details: ")
                    print(f"ID: {book.id}\nTitle: {book.title}\nAuthor: {book.author}\nGenre: {book.genre}\nPages: {book.page_number}\n")
                    break
            if not found: 
                print(f"Book with ID: {book_id} not found")

        elif choice == '9':
            book_id = int(input("Enter the ID of the book to delete: "))
            found = False
            for book in book_list:
                if book.id == book_id:
                    book_list.remove(book)
                    found = True
                    break
            if found:
                print(f"Book with ID: {book_id} has been deleted.")
                with open("data_folder/books.txt", "w") as f:
                    for b in book_list:
                        f.write(b.book_info() + '\n')
            else:
                print(f"Book with ID: {book_id} not found.")

        elif choice == '0':
            print("Exiting the system. Goodbye!")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()    