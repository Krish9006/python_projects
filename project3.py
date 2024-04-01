books_in_library = {
    1: {"title": "An Autobiography", "author": "Pt. Jr Lal Nehru", "quantity": 5},
    2: {"title": "Arthashastra", "author": "Kautilya", "quantity": 3},
    3: {"title": "Arion and the dolphin", "author": "Vikarm Seth", "quantity": 2}
}


# User data about the book 
users = {}



# Function to display books_in_the_library
def display_books_in_library():
    print("books_in_the_library:")
    for book_id, book_info in books_in_the_library.items():
        print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Quantity: {book_info['quantity']}")
    main_call()

# Function for user registration
def register_user():
    name = input("Enter your name: ")
    user_id = len(users) + 1
    users[user_id] = {"name": name, "books_checked_out": []}
    print(f"User '{name}' registered successfully with ID: {user_id}")
    print("What do you want next : ")
    main_call()




# Function for book Take
def Take_books():
    user_id = int(input("Enter your user ID: "))
    book_id = int(input("Enter the book ID to Take: "))
    if book_id not in books_in_the_library:
        print("Book ID is invalid.")
        return
    if len(users[user_id]["books_checked_out"]) >= 3:
        print("You have already checked out the maximum number of books.")
        return
    if books_in_library[book_id]["quantity"] == 0:
        print("Sorry, this book is currently not available.")
        return
    books_in_library[book_id]["quantity"] -= 1
    Take_date = 0  # Start date
    due_date = Take_date + 14  # Due date is 14 days after Take
    users[user_id]["books_checked_out"].append({"book_id": book_id, "Take_date": Take_date, "due_date": due_date})
    print(f"Book '{books_in_library[book_id]['title']}' checked out successfully. Due date: Day {due_date}")
    main_call()




# Function for book return
def return_book():
    user_id = int(input("Enter your user ID: "))
    book_id = int(input("Enter the book ID to return: "))
    
    print("You haven't checked out this book.")
    return_days = int(input("Enter number of days to have the book : "))
    if(return_days>14):
        print(f"Fine will be charged of {return_days-14*1} dollars.")
    else:
        print("No file will be charged.")




# Main program loop
def main_call():
    print("\nLibrary Management System")
    print("1. Display books_in_the_library")
    print("2. Register User")
    print("3. Take Book")
    print("4. Return Book")
    
    print("5. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        display_books_in_library()
    elif choice == '2':
        register_user()
    elif choice == '3':
        Take_books()
    elif choice == '4':
        return_book()
    
    elif choice == '5':
        print("Thank you for using the Library Management System.")

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")

main_call();