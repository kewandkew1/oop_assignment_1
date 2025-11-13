📚 Library Management System (OOP Version)

This project is an Object-Oriented refactoring of a procedural library management system.
It demonstrates class-based design using Book, Member, and Library objects, and includes a comprehensive test suite that verifies both basic operations and edge cases.

📌 Project Overview

The Library Management System allows users to:

Add books and register members

Borrow and return books

Track all borrowed books

Display available books and each member’s borrowed list

The system enforces important rules, including:

A member may borrow up to 3 books

A book cannot be borrowed if no copies are available

A member cannot return a book that they did not borrow

Borrowing/returning operations update both the book inventory and member record

This project illustrates clean class design, encapsulation, and real-world OOP behavior.

📁 Project Structure
project/
│
├── library_oop.py        # Main implementation (Book, Member, Library classes)
├── test_oop.py           # Full test suite covering operations and edge cases
└── README.md             # Project documentation

🧩 Design Overview

The system is built using three main classes:

🔹 Class: Book

Represents a single book in the library.

Attributes

id — Unique ID of the book

title — Book title

author — Author name

available_copies — Number of copies available

total_copies — Total number of copies originally added

Key Methods

borrow_book()

Decreases available copies by 1

Prevents borrowing if no copies remain

return_book()

Increases available copies by 1

Prevents returning above total stock

display_book(show_copies)

Prints book information, optionally including available copies

🔹 Class: Member

Represents a library member.

Attributes

id — Unique member ID

name — Member full name

email — Contact email

borrowed_books — List of Book objects currently borrowed

Key Methods

borrow(book)

Adds a book to the member’s borrowed list

Enforces the 3-book borrowing limit

return_book(book)

Removes the book from the member’s borrowed list

Prevents returning if the member never borrowed the book

display_books()

Shows all books borrowed by this member

🔹 Class: Library

Central manager of books, members, and transactions.

Attributes

name — Library name

books — List of Book objects

members — List of Member objects

transactions — List of borrowing records

Key Methods

add_book(id, title, author, copies)

Creates and stores a new Book

add_member(id, name, email)

Registers a new Member

find_book(id) / find_member(id)

Retrieves objects by ID

borrow_book(member_id, book_id)

Member borrows a book (validates all conditions)

return_book(member_id, book_id)

Member returns a book

display_available_books()

display_member_books(member_id)

display_all_members_and_books()

🧪 Testing

All testing is performed in test_oop.py, which includes both basic functionality tests and edge case handling.

✔️ Basic Operations Covered

Adding books

Registering members

Borrowing books

Returning books

Displaying:

Available books

Borrowed books

Member-specific book lists

✔️ Edge Cases Covered

Borrowing a book with no copies left

Member exceeding borrowing limit (3 books)

Returning a book that was not borrowed

Borrowing or returning using invalid member/book IDs

The testing script outputs step-by-step details to the console, making it easy to verify system behavior.

✅ Summary

This project demonstrates a clean OOP-based system with:

Strong class encapsulation

Clear responsibilities for each component

A robust and readable test suite

Error handling for real-world usage scenarios

It is fully functional, extensible, and structured for academic or production use.