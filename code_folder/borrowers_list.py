import books, users

def checkout_book(user_id,book_id,user_list:list[users.User],book_list:list[books.Book]):
    found_user = False
    found_book = False

    for user in user_list:
        if user.id == user_id:
            found_user = True
            borrower = user
            for book in book_list:
                if book.id == book_id:
                    found_book = True
                    if book.is_checked_out():
                        return "Book is already checked out."
                    book.check_out()
                    with open("data_folder/books.txt", "w") as f:
                        for b in book_list:
                            f.write(b.book_info() + '\n')
                    with open("data_folder/borrowers.txt", "a") as f:
                        f.write(f"{borrower.id},{borrower.user_name},{book.id},{book.title}\n")
                    return f"Book '{book.title}' has been checked out by {borrower.user_name}."
            if not found_book:
                return "Book not found."        
    if not found_user:
        return "User not found."

def return_book(user_id,book_id,book_list:list[books.Book]):
    lines = []
    found_book = False
    found_line = False
    for book in book_list:
        if book.id == book_id:
            found_book = True
            if not book.is_checked_out():
                return "Book was not checked out."
            with open("data_folder/borrowers.txt", "r") as f:
                lines = f.readlines()
                if len(lines) == 0:
                    return "No borrowers found."
                for line in lines:
                    u_id,user_name,b_id,book_title = line.strip().split(",")
                    if int(b_id) == book_id and int(u_id) == user_id:
                        found_line = True
                        book.return_book()
                        lines.remove(line)
                        break
                if not found_line:
                    return "No matching borrower record found."   

    if not found_book:
        return "Book not found."
    with open("data_folder/borrowers.txt", "w") as f:
        f.writelines(lines)
    with open("data_folder/books.txt", "w") as f:
        for b in book_list:
            f.write(b.book_info() + '\n')    
    return f"Book '{book.title}' has been returned successfully."                
