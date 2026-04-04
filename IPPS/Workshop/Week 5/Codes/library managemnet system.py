name =  "Sagar Mishra"
print (name)
#program
books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "year": 1954},
    {"title": "The Da Vinci Code", "author": "Dan Brown", "year": 2003}
]
#Display all books 
def display_books():
    print("\n📚 Total Available Books:", len(books))
    if not books:
        print("No books available.\n")
        return

    for i, book in enumerate(books, start=1):
        print(f"{i}. Title : {book['title']}")
        print(f"   Author: {book['author']}")
        print(f"   Year  : {book['year']}\n")
#Add a new book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = int(input("Enter publication year: "))
    books.append({"title": title, "author": author, "year": year})
    print("🎊🎊Book added successfully🎊🎊\n")
#Remove a book by title
def remove_book():
    title = input("Enter title of the book to remove: ")
    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            print("🎊Book removed successfully🎊\n")
            return
    print("❗️❗️Book not found❗️❗️\n")
#Search by title
def search_by_title():
    title = input("Enter book title to search: ")
    for book in books:
        if book["title"].lower() == title.lower():
            print(book, "\n")
            return
    print("❗️❗️Book not found❗️❗\n")
#Search by author
def search_by_author():
    author = input("Enter author name to search: ")
    found = False
    for book in books:
        if book["author"].lower() == author.lower():
            print(book)
            found = True
    if not found:
        print("❌No books found by this author❌")
    print()
#List all books
def list_books():
    if not books:
        print("❌No books available ❌\n")
    else:
        for book in books:
            print(book)
        print()
# Main menu loop
while True:
    print("Library Management System")
    print("1. Add a new book")
    print("2. Remove a book")
    print("3. Search for a book by title")
    print("4. Search for a book by author")
    print("5. List all books")
    print("6. Quit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            add_book()
        case 2:
            remove_book()
        case 3:
            search_by_title()
        case 4:
            list_books()
        case 5:
            print("Goodbye!")
            break
        case _:
            print("Invalid choice")
    display_books()

