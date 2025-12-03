import books
import users
import borrowers_list
import os


def main():
    choice = ''
    book_list = []
    user_list = []

    with open("data_folder/books.txt", "r") as f:
        if os.path.getsize("data_folder/books.txt") != 0:
            for line in f:
                id,title, author, published_year, genre, page_number, checked_out = line.strip().split(',')
                book = books.create_book(title, author, published_year, genre, int(page_number))
                book.checked_out = checked_out == 'Checked out'
                book.id = int(id)
                book_list.append(book)

    with open("data_folder/users.txt", "r") as f:
        if os.path.getsize("data_folder/users.txt") != 0:
            for line in f:
                id,user_name, full_name, phone_number, email = line.strip().split(',')
                user = users.create_user(user_name, full_name, phone_number, email)
                user.id = int(id)
                user_list.append(user)            
    
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
        print("10. Add User")
        print("11. List All Users")
        print("12. Update User Information")
        print("13. Search User")
        print("14. Delete User")
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
            user_id = int(input("Enter your borrower's ID: "))
            message = borrowers_list.checkout_book(user_id = user_id, book_id = book_id, user_list = user_list, book_list = book_list)
            print(message)

        elif choice == '6':
            book_id = int(input("Enter the ID of the book to return: "))
            user_id = int(input("Enter your borrower's ID: "))
            message = borrowers_list.return_book(user_id = user_id, book_id = book_id, book_list = book_list)
            print(message)
        
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
        elif choice == '10':
            user_name = input("Enter username: ")
            full_name = input("Enter full name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            new_user = users.create_user(user_name, full_name, phone_number, email)
            user_list.append(new_user)
            with open("data_folder/users.txt", "a") as f:
                f.write(new_user.get_info() + '\n')
            print(f"User '{user_name}' added successfully.")

        elif choice == '11':
            print("\nAll Users:")
            print("ID               Username                       Full Name                     Phone Number                 Email                         ")
            print("-" * 150)
            users.list_users(user_list)

        elif choice == '12':
            user_id = int(input("Enter the ID of the user to update: "))
            found = False
            for user in user_list:
                if user.id == user_id:
                    user_name = input("Enter new username (leave blank to keep current): ")
                    full_name = input("Enter new full name (leave blank to keep current): ")
                    phone_number = input("Enter new phone number (leave blank to keep current): ")
                    email = input("Enter new email (leave blank to keep current): ")
                    user.update_info(
                        user_name=user_name if user_name else None,
                        full_name=full_name if full_name else None,
                        phone_number=phone_number if phone_number else None,
                        email=email if email else None
                    )
                    found = True
                    break
            if not found:
                print(f"User with ID '{user_id}' not found in the system.")
                return
            with open("data_folder/users.txt", "w") as f:
                    for u in user_list:
                        f.write(u.get_info() + '\n')

        elif choice == '13':
            user_id = int(input('Enter the ID of the user to be searched: '))
            found = False
            for user in user_list:
                if user.id == user_id:
                    found = True
                    print("User details: ")
                    print(f"ID: {user.id}\nUsername: {user.user_name}\nFull Name: {user.full_name}\nPhone Number: {user.phone_number}\nEmail: {user.email}\n")
                    break
            if not found: 
                print(f"User with ID: {user_id} not found")    

        elif choice == '14':
            user_id = int(input("Enter the ID of the user to delete: "))
            found = False
            for user in user_list:
                if user.id == user_id:
                    user_list.remove(user)
                    found = True
                    break
            if found:
                print(f"User with ID: {user_id} has been deleted.")
                with open("data_folder/users.txt", "w") as f:
                    for u in user_list:
                        f.write(u.get_info() + '\n')
            else:
                print(f"User with ID: {user_id} not found.")

        
        elif choice == '0':
            print("Exiting the system. Goodbye!")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()    