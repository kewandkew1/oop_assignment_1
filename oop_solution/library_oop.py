# Library Management System - OOP Style (comments same as original procedural version)

class Book:
    def __init__(self, book_id, title, author, available_copies):
        """Initialize a new book with ID, title, author, and number of copies"""
        self.id = book_id
        self.title = title
        self.author = author
        self.available_copies = available_copies
        self.total_copies = available_copies

    def borrow_book(self):
        """Reduce available copies by 1 if possible"""
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        print("Error: No copies available!")
        return False

    def return_book(self):
        """Increase available copies by 1, but not above total copies"""
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        print("Error: All copies have already been returned!")
        return False

    def display_book(self, show_copies=False):
        """Display book information, optionally showing available copies"""
        text = f"{self.title} by {self.author}"
        if show_copies:
            text += f" - {self.available_copies} copies available"
        print(text)


class Member:
    def __init__(self, member_id, name, email):
        """Initialize a new library member"""
        self.id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow(self, book):
        """Process borrowing a book"""
        if len(self.borrowed_books) >= 3:
            print("Error: Member has reached borrowing limit!")
            return False

        if book.borrow_book():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
            return True
        return False

    def return_book(self, book):
        """Process returning a borrowed book"""
        if book not in self.borrowed_books:
            print("Error: This member hasn't borrowed this book!")
            return False

        if book.return_book():
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
            return True
        return False

    def display_books(self):
        """Display all books currently borrowed by this member"""
        print(f"\n=== Books borrowed by {self.name} ===")
        if not self.borrowed_books:
            print("No books currently borrowed")
        else:
            for book in self.borrowed_books:
                print(f"- {book.title} by {book.author}")


class Library:
    def __init__(self, name="City Library"):
        """Initialize the library with book and member collections"""
        self.name = name
        self.books = []
        self.members = []
        self.transactions = []

    def add_book(self, book_id, title, author, copies):
        """Add a new book to the library"""
        for b in self.books:
            if b.id == book_id:
                print("Error: Book ID already exists!")
                return None

        book = Book(book_id, title, author, copies)
        self.books.append(book)
        print(f"Added Book: {title} by {author} ({copies} copies)")
        return book

    def add_member(self, member_id, name, email):
        """Register a new library member"""
        for m in self.members:
            if m.id == member_id:
                print("Error: Member ID already exists!")
                return None

        member = Member(member_id, name, email)
        self.members.append(member)
        print(f"Added Member: {name} ({email})")
        return member

    def find_book(self, book_id):
        """Find a book by ID"""
        for b in self.books:
            if b.id == book_id:
                return b
        print("Error: Book not found!")
        return None

    def find_member(self, member_id):
        """Find a member by ID"""
        for m in self.members:
            if m.id == member_id:
                return m
        print("Error: Member not found!")
        return None

    def borrow_book(self, member_id, book_id):
        """Process a book borrowing transaction"""
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member and book:
            if member.borrow(book):
                self.transactions.append({
                    'member_name': member.name,
                    'book_title': book.title
                })

    def return_book(self, member_id, book_id):
        """Process a book return transaction"""
        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member and book:
            if member.return_book(book):
                self.transactions = [
                    t for t in self.transactions
                    if not (t['member_name'] == member.name and t['book_title'] == book.title)
                ]

    def display_available_books(self):
        """Display all books with available copies"""
        print(f"\n=== Available Books in {self.name} ===")
        if not self.books:
            print("No books available")
        for b in self.books:
            b.display_book(show_copies=True)

    def display_member_books(self, member_id):
        """Display books borrowed by a specific member"""
        member = self.find_member(member_id)
        if member:
            member.display_books()

    def display_all_members_and_books(self):
        """Display all members and the books they have borrowed"""
        print("\nAll Members and Their Books:")
        for m in self.members:
            print(f"\n{m.name} ({m.id}):")
            if m.borrowed_books:
                for b in m.borrowed_books:
                    print(f"  - {b.title}")
            else:
                print("  (No books borrowed)")
