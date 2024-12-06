#!/usr/bin/env python3

# Define the book inventory
book_inventory = {
    "William Shakespeare": [
        {"book": "Hamlet", "year": 1601, "price": 14.52, "quantity": 43},
        {"book": "Macbeth", "year": 1606, "price": 13.45, "quantity": 50},
        {"book": "Othello", "year": 1604, "price": 15.30, "quantity": 37},
        {"book": "Romeo and Juliet", "year": 1597, "price": 12.99, "quantity": 60}
    ],
    "Charles Dickens": [
        {"book": "A Tale of Two Cities", "year": 1859, "price": 9.56, "quantity": 75},
        {"book": "Great Expectations", "year": 1861, "price": 12.50, "quantity": 60},
        {"book": "Oliver Twist", "year": 1837, "price": 9.75, "quantity": 50},
        {"book": "David Cooperfield", "year": 1850, "price": 11.25, "quantity": 40}
    ],
    "James Joyce": [
        {"book": "Ulysses", "year": 1922, "price": 19.99, "quantity": 30},
        {"book": "A Portrait of the Artist as a Young Man", "year": 1916, "price": 13.20, "quantity": 25},
        {"book": "Dubliners", "year": 1914, "price": 12.00, "quantity": 35},
        {"book": "Finnegans Wake", "year": 1939, "price": 16.50, "quantity": 20}
    ],
    "Ernest Hemingway": [
        {"book": "The Old Man and the Sea", "year": 1952, "price": 10.35, "quantity": 80},
        {"book": "A Farewell to Arms", "year": 1929, "price": 14.75, "quantity": 45},
        {"book": "For Whom the Bell Tolls", "year": 1940, "price": 13.50, "quantity": 50},
        {"book": "The Sun Also Rises", "year": 1926, "price": 12.99, "quantity": 55}
    ],
    "J.K. Rowling": [
        {"book": "Harry Potter And the Sorcerer's Stone", "year": 1997, "price": 16.62, "quantity": 100},
        {"book": "Harry Potter And the Chamber of Secrets", "year": 1998, "price": 22.99, "quantity": 90},
        {"book": "Harry Potter And the Prisoner of Azkaban", "year": 1999, "price": 23.99, "quantity": 85},
        {"book": "Harry Potter And the Goblet of Fire", "year": 2000, "price": 25.99, "quantity": 80}

    ]
}

def display_menu():
    print("\n-----------Menu------------")
    print("1) Display Book Inventory and Calculate Total")
    print("2) Lookup by Author and Get Total")
    print("3) Lookup by Book Name and Get Total")
    print("4)Lookup By Price Range")
    print("5) Exit ")
    print("----------------------")


def display_inventory():
    print(f"\n{'Author':<20} {'Book':>15} {'Year':>50} {'Price':>8} {'Quantity':<8} ")
    print("------------------------------------------------------------------------------------------------------------------------------")
    total_inventory_value = 0
    for author, books in book_inventory.items():
        for book in books:
            total = book["price"] * book["quantity"]
            total_inventory_value += total
            print(f"{author:<30} {book['book']:<50} {book['year']:<8} {book['price']:<8} {book['quantity']:<8} ")
            print(f"\nOverall Total Inventory Value: ${total_inventory_value:.2f}")
    

def search_by_author():
    author_name = input("Enter author's name (capitalize first and last names): ")
    books = book_inventory.get(author_name)
    if books:
        total_author_value = 0
        print(f"\nBooks by {author_name}:")
        print(f"{'Book':<30} {'Year':<6} {'Price':<8} {'Quantity':<8} {'Total'}")
        print("------------------------------------------------------------------")
        for book in books:
            total = book["price"] * book["quantity"]
            total_author_value += total
            print(f"{book['book']:<30} {book['year']:<6} {book['price']:<8} {book['quantity']:<8} {total:.2f}")
        print(f"\nTotal Value for books by {author_name}: ${total_author_value:.2f}")
    else:
        print("No books found for author entered.")

def search_by_book_name():
    book_name = input("Enter book name: ")
    found = False
    for author, books in book_inventory.items():
        for book in books:
            if book["book"] == book_name:
                total_price = book["price"] * book["quantity"]
                print("\nBook Information:")
                print(f"Author: {author}")
                print(f"Book: {book['book']}")
                print(f"Year: {book['year']}")
                print(f"Price: ${book['price']}")
                print(f"Quantity: {book['quantity']}")
                print(f"Overall Price: ${total_price:.2f}")
                found = True
                break
    if not found:
        print("Book not found in inventory.")

def search_by_price_range():
    try:
        start_range = float(input("Enter Start range: "))
        end_range = float(input("Enter last number in lookup range: "))
        found_books = []
        for author, books in book_inventory.items():
            for book in books:
                if start_range <= book["price"] <= end_range:
                    found_books.append((author, book["book"], book["price"]))
        if found_books:
            print(f"\nBooks priced between ${start_range} and ${end_range}:")
            for author, book, price in found_books:
                print(f"Author: {author}, Book: {book}, Price: ${price}")
            print(f"Total number of books in this price range: {len(found_books)}")
        else:
            print("No books found in the entered price range.")
    except ValueError:
        print("Invalid input. Please enter numeric values for price range.")

def main():
    while True:
        display_menu()
        choice = input("Enter Choice: ")
        if choice == "1":
            display_inventory()
        elif choice == "2":
            search_by_author()
        elif choice == "3":
            search_by_book_name()
        elif choice == "4":
            search_by_price_range()
        elif choice == "5":
            print("The program will stop now.")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
