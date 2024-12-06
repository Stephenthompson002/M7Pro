import csv

# Define Book Class
class Book:
    def __init__(self, book_name, year_pub, price, quantity, author_name):        # Initialize the Book object with necessary attribute
        self._book_name = book_name
        self._year_pub = year_pub
        self._price = price
        self._quantity = quantity
        self._author_name = author_name
        self._total = self.set_total()  # Set the total based on quantity and price

    def set_total(self):        # Calculate and return total cost (price * quantity)
        return self._quantity * self._price

    def get_book_name(self):        # Return the book name
        return self._book_name

    def get_year_pub(self):        # Return the year of publication
        return self._year_pub

    def get_price(self):        # Return the price of the book
        return self._price

    def get_quantity(self):        # Return the available quantity of the book
        return self._quantity

    def get_total(self):        # Return the total value of the book (quantity * price)
        return self._total

    def set_price(self, price):        # Set the book price and update the total accordingly
        self._price = price
        self._total = self.set_total()

    def set_quantity(self, quantity):        # Set the book quantity and update the total accordingly
        self._quantity = quantity
        self._total = self.set_total()

    def get_author_name(self):        # Return the name of the book's author
        return self._author_name

    def __repr__(self):        # Return a formatted string representation of the book
        return f"{self._book_name:<25} {self._year_pub:<10} ${self._price:<8} {self._quantity:<10} ${self._total:<10}"

# Define Author Class
class Author:
    def __init__(self, author_name):        # Initialize Author object with author name and empty list of books
        self._author_name = author_name
        self._books = []

    def get_author_name(self):        # Return the author's name
        return self._author_name

    def set_books(self, books):        # Set the list of books written by the author
        self._books = books

    def __repr__(self):        # Return a formatted string representation of the author and their books
        books_info = "\n".join([repr(book) for book in self._books])
        return f"{self._author_name:<20}\n{books_info}"

# Define create_instance Function
def create_instance(inventory_dict):
    authors = []
    books = []

    for author_name, books_data in inventory_dict.items():
        author = Author(author_name)  # Create an Author object
        book_instances = []  # List to store book instances

        for book_data in books_data:            # Create Book objects from the book data
            book = Book(
                book_data["book"],
                book_data["year"],
                book_data["price"],
                book_data["quantity"],
                author_name
            )
            book_instances.append(book)
            books.append(book)
        
        author.set_books(book_instances)  # Set the books for this author
        authors.append(author)

    return authors, books  # Return lists of authors and books

# Write Instance to CSV
def write_instance(objects, filename):    # Write details of authors and books to a CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Author Name", "Book Name", "Year Published", "Price", "Quantity", "Total"])
        for obj in objects:
            if isinstance(obj, Author):  # If object is an Author
                for book in obj._books:                    # Write each book's details under the author's name
                    writer.writerow([obj.get_author_name(), book.get_book_name(), book.get_year_pub(), f"${book.get_price():.2f}", book.get_quantity(), f"${book.get_total():.2f}"])
            elif isinstance(obj, Book):  # If object is a Boo
                writer.writerow([obj.get_author_name(), obj.get_book_name(), obj.get_year_pub(), f"${obj.get_price():.2f}", obj.get_quantity(), f"${obj.get_total():.2f}"])                # Write book details directly

# Search Functions
def search_by_author(authors, author_name):    # Search for authors by name (case-insensitive)
    author_name = author_name.lower()  # Normalize input to lowercase
    return [author for author in authors if author_name in author.get_author_name().lower()] # Return matching books

def search_by_book(books, book_name):    # Search for books by title (case-insensitive)
    book_name = book_name.lower()  # Normalize input to lowercase
    return [book for book in books if book_name in book.get_book_name().lower()]  # Return matching books

def search_by_price_range(books, start_price, end_price):    # Filter books by price range
    return [book for book in books if start_price <= book.get_price() <= end_price]  # Return books within the price range

# Write Books for Author to CSV
def write_books_by_author_to_csv(author, filename):    # Write books of a specific author to a CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Book Name", "Year Published", "Price", "Quantity", "Total"])
        for book in author._books:            # Write each book's details
            writer.writerow([book.get_book_name(), book.get_year_pub(), f"${book.get_price():.2f}", book.get_quantity(), f"${book.get_total():.2f}"])

# Write Books Within Price Range to CSV
def write_books_within_price_range_to_csv(books, start_price, end_price):    # Write books within the specified price range to a CSV file
    filename = f"books_{start_price}_{end_price}.csv"  # Dynamic filename based on price range
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Book Name", "Author Name", "Year Published", "Price", "Quantity", "Total"])
        for book in books:
            if start_price <= book.get_price() <= end_price: # Filter books by price range
                writer.writerow([book.get_book_name(), book.get_author_name(), book.get_year_pub(), f"${book.get_price():.2f}", book.get_quantity(), f"${book.get_total():.2f}"])

    print(f"\nBooks within the price range ${start_price} - ${end_price} have been written to '{filename}'.")

# Purchase Book Functionality
def purchase_books(books):
    purchased_books = []

    while True:
        book_title = input("\nEnter the book title or part of the title to search: ").strip().lower()
        found_books = search_by_book(books, book_title)

        if not found_books:
            print("No books found with the title or partial title entered.")
        else:
            # Display found books
            print(f"\n{'Book Name':<25} {'Author Name':<20} {'Year Published':<10} {'Price':<8}")
            for book in found_books:
                print(f"{book.get_book_name():<25} {book.get_author_name():<20} {book.get_year_pub():<10} ${book.get_price():<8}")

            # Ask if the user wants to purchase
            purchase_choice = input("Would you like to purchase this book? (yes/no): ").strip().lower()

            if purchase_choice == "yes":
                # Decrease the quantity of the book
                for book in found_books:
                    quantity_to_purchase = int(input(f"Enter the quantity for '{book.get_book_name()}': "))
                    if quantity_to_purchase > book.get_quantity():
                        print(f"Not enough stock for {book.get_book_name()}. Available: {book.get_quantity()}")
                    else:
                        # Update book quantity
                        book.set_quantity(book.get_quantity() - quantity_to_purchase)
                        # Add to purchased books list
                        purchased_books.append((book.get_author_name(), book.get_book_name(), book.get_year_pub(), book.get_price(), quantity_to_purchase))

            another_purchase = input("Do you wish to purchase another book? (yes/no): ").strip().lower()
            if another_purchase != "yes":
                break

    # Write purchased books to CSV
    with open("purchased.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Author Name", "Book Name", "Year Published", "Price", "Quantity", "Total Price"])
        total_price = 0
        for author_name, book_name, year, price, quantity in purchased_books:
            total = price * quantity + (price * quantity * 0.05)  # Including 5% tax
            writer.writerow([author_name, book_name, year, f"${price:.2f}", quantity, f"${total:.2f}"])
            total_price += total
        
        writer.writerow(["", "", "", "Total", "", f"${total_price:.2f}"])

    print("\nPurchased books information has been written to 'purchased.csv'.")

    # Update inventory and save it to a new CSV file
    write_instance(books, "inventory_update.csv")
    print("\nInventory has been updated and written to 'inventory_update.csv'.")

# Main Function
def main():    # Sample inventory data
    inventory_dict = {
        "William Shakespeare": [
            {"book": "Hamlet", "year": 1601, "price": 14.52, "quantity": 43},
            {"book": "Macbeth", "year": 1606, "price": 13.45, "quantity": 50},
            {"book": "Othello", "year": 1604, "price": 15.30, "quantity": 37},
            {"book": "Romeo and Juliet", "year": 1597, "price": 12.99, "quantity": 60}
        ],
        "Charles Dickens": [
            {"book": "A Tale of Two Cities", "year": 1859, "price": 9.56, "quantity": 75},
            {"book": "Great Expectations", "year": 1861, "price": 12.50, "quantity": 60},
            {"book": "Oliver Twist", "year": 1837, "price": 10.90, "quantity": 85}
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
    # Create instances of authors and books
    authors, books = create_instance(inventory_dict)

    while True:
        print("\nMenu:")
        print("1. Display Inventory")
        print("2. Search by Author")
        print("3. Search by Book Title")
        print("4. Search by Price Range")
        print("5. Purchase Books (Search by Title)")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":            # Display all books in inventory
            for author in authors:
                print(author)

        elif choice == "2":            # Search for books by author name
            author_name = input("Enter author name: ").strip()
            found_authors = search_by_author(authors, author_name)

            if found_authors:
                for author in found_authors:
                    print(author)
            else:
                print(f"No author found with the name '{author_name}'.")

        elif choice == "3":            # Search for books by book title
            book_name = input("Enter book title: ").strip()
            found_books = search_by_book(books, book_name)

            if found_books:
                print(f"\n{'Book Name':<25} {'Author Name':<20} {'Year Published':<10} {'Price':<8} {'Quantity':<10}")
                for book in found_books:
                    print(f"{book.get_book_name():<25} {book.get_author_name():<20} {book.get_year_pub():<10} ${book.get_price():<8} {book.get_quantity():<10}")
            else:
                print(f"No books found with the title '{book_name}'.")

        elif choice == "4":            # Search for books within a price range
            start_price = float(input("Enter start price: "))
            end_price = float(input("Enter end price: "))
            write_books_within_price_range_to_csv(books, start_price, end_price)

        elif choice == "5":
            purchase_books(books)

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the main function to start the program
if __name__ == "__main__":
    main()
