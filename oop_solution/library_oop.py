class Book:
    def __init__(self, id, title, author, total_copies):
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def can_borrow(self):
        """Check if the book still has available copies."""
        return self.available_copies > 0

    def borrow_one(self):
        """Reduce available copies by 1 if possible."""
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_one(self):
        """Increase available copies by 1, but not above total_copies."""
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

    def __str__(self):
        return f"{self.title} by {self.author} - {self.available_copies}/{self.total_copies} available"


class Member:
    def __init__(self, member_id, name, email, max_books=3):
        self.id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = []  # list ของ book_id
        self.max_books = max_books

    def can_borrow(self):
        """Check if the member can borrow more books."""
        return len(self.borrowed_books) < self.max_books

    def borrow_book(self, book_id):
        """Add a book to the member's borrowed list."""
        if self.can_borrow():
            self.borrowed_books.append(book_id)
            return True
        return False

    def return_book(self, book_id):
        """Remove a book from the borrowed list."""
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True
        return False

    def get_borrowed_books(self):
        """Return all borrowed book IDs."""
        return self.borrowed_books

    def __str__(self):
        return f"Member: {self.name} ({self.id}) - Borrowed: {len(self.borrowed_books)} books"


books = []
members = []
borrowed_books = []


def add_book(book_id, title, author, available_copies):
    """Add a new book to the library"""
    book = Book(book_id, title, author, available_copies)
    books.append(book)
    print(f"Book '{title}' added successfully!")


def add_member(member_id, name, email):
    """Register a new library member"""
    member = Member(member_id, name, email)
    members.append(member)
    print(f"Member '{name}' registered successfully!")


def find_book(book_id):
    """Find a book by ID"""
    for book in books:
        if book.id == book_id:
            return book
    return None


def find_member(member_id):
    """Find a member by ID"""
    for member in members:
        if member.id == member_id:
            return member
    return None


def borrow_book(member_id, book_id):
    """Process a book borrowing transaction"""
    member = find_member(member_id)
    book = find_book(book_id)

    if not member:
        print("Error: Member not found!")
        return False

    if not book:
        print("Error: Book not found!")
        return False

    if not book.can_borrow():
        print("Error: No copies available!")
        return False

    if not member.can_borrow():
        print("Error: Member has reached borrowing limit!")
        return False

    # Process the borrowing
    if not member.borrow_book(book_id):
        print("Error: Could not add book to member record!")
        return False

    book.borrow_one()

    transaction = {
        'member_id': member_id,
        'book_id': book_id,
        'member_name': member.name,
        'book_title': book.title
    }
    borrowed_books.append(transaction)

    print(f"{member.name} borrowed '{book.title}'")
    return True


def return_book(member_id, book_id):
    """Process a book return transaction"""
    member = find_member(member_id)
    book = find_book(book_id)

    if not member or not book:
        print("Error: Member or book not found!")
        return False

    if book_id not in member.get_borrowed_books():
        print("Error: This member hasn't borrowed this book!")
        return False

    # Process the return
    if not member.return_book(book_id):
        print("Error: Could not update member record!")
        return False

    book.return_one()

    # Remove from borrowed_books list
    for i, transaction in enumerate(borrowed_books):
        if transaction['member_id'] == member_id and transaction['book_id'] == book_id:
            borrowed_books.pop(i)
            break

    print(f"{member.name} returned '{book.title}'")
    return True


def display_available_books():
    """Display all books with available copies"""
    print("\n=== Available Books ===")
    for book in books:
        if book.available_copies > 0:
            print(f"{book.title} by {book.author} - {book.available_copies} copies available")


def display_member_books(member_id):
    """Display books borrowed by a specific member"""
    member = find_member(member_id)
    if not member:
        print("Error: Member not found!")
        return

    print(f"\n=== Books borrowed by {member.name} ===")
    if not member.get_borrowed_books():
        print("No books currently borrowed")
    else:
        for book_id in member.get_borrowed_books():
            book = find_book(book_id)
            if book:
                print(f"- {book.title} by {book.author}")