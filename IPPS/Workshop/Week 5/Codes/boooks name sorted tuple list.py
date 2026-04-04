name = "Sagar Mishra"
print(name)
#program
books = [
    ("The Great Gatsby", "F. Scott Fitzgerald"),
    ("To Kill a Mockingbird", "Harper Lee"),
    ("1984", "George Orwell"),
    ("Pride and Prejudice", "Jane Austen"),
    ("Moby-Dick", "Herman Melville")
]
def get_author(book):
    return book[1]
sorted_books = sorted(books, key=get_author)
for title, author in sorted_books:
    print(f"{title}: {author}")
