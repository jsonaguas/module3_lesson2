
def add_book(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    for book in library:
        if title == book[0] and author == book[1]:
            print("The book is already in the library.")
            return library
    library.append((title, author))
    print("The book has been added to the library.")
    return library

def main():
    library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
    library = add_book(library)
    print(library)

if __name__ == "__main__":
    main()

