from library_oop import Library

# Test Code for OOP Library System
def test_library_system():
    """Comprehensive test of all library functions"""

    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - COMPREHENSIVE TEST")
    print("=" * 60)

    # สร้างห้องสมุดก่อน
    lib = Library("City Library")

    # Test 1: Add Books
    print("\n--- TEST 1: Adding Books ---")
    lib.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    lib.add_book(2, "Clean Code", "Robert Martin", 2)
    lib.add_book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
    lib.add_book(4, "Design Patterns", "Gang of Four", 2)

    # Test 2: Add Members
    print("\n--- TEST 2: Registering Members ---")
    lib.add_member(101, "Alice Smith", "alice@email.com")
    lib.add_member(102, "Bob Jones", "bob@email.com")
    lib.add_member(103, "Carol White", "carol@email.com")

    # Test 3: Display Available Books
    print("\n--- TEST 3: Display Available Books ---")
    lib.display_available_books()

    # Test 4: Successful Book Borrowing
    print("\n--- TEST 4: Successful Borrowing ---")
    lib.borrow_book(101, 1)  # Alice borrows Python Crash Course
    lib.borrow_book(101, 2)  # Alice borrows Clean Code
    lib.borrow_book(102, 1)  # Bob borrows Python Crash Course

    # Test 5: Display Member's Borrowed Books
    print("\n--- TEST 5: Display Member's Books ---")
    lib.display_member_books(101)  # Alice's books
    lib.display_member_books(102)  # Bob's books
    lib.display_member_books(103)  # Carol's books (none)

    # Test 6: Display Available Books After Borrowing
    print("\n--- TEST 6: Available Books After Borrowing ---")
    lib.display_available_books()

    # Test 7: Borrow Last Available Copy
    print("\n--- TEST 7: Borrowing Last Copy ---")
    lib.borrow_book(103, 3)  # Carol borrows the only copy of Pragmatic Programmer
    lib.display_available_books()

    # Test 8: Try to Borrow Unavailable Book
    print("\n--- TEST 8: Attempting to Borrow Unavailable Book ---")
    lib.borrow_book(102, 3)  # Bob tries to borrow unavailable book

    # Test 9: Borrowing Limit Test
    print("\n--- TEST 9: Testing Borrowing Limit (3 books max) ---")
    lib.borrow_book(101, 4)  # Alice's 3rd book
    lib.display_member_books(101)
    lib.borrow_book(101, 3)  # Alice tries to borrow 4th book (should fail)

    # Test 10: Return Books
    print("\n--- TEST 10: Returning Books ---")
    lib.return_book(101, 1)  # Alice returns Python Crash Course
    lib.return_book(102, 1)  # Bob returns Python Crash Course
    lib.display_member_books(101)
    lib.display_available_books()

    # Test 11: Try to Return Book Not Borrowed
    print("\n--- TEST 11: Attempting Invalid Return ---")
    lib.return_book(102, 2)  # Bob tries to return book he didn't borrow

    # Test 12: Return and Borrow Again
    print("\n--- TEST 12: Return and Re-borrow ---")
    lib.return_book(103, 3)  # Carol returns Pragmatic Programmer
    lib.borrow_book(102, 3)  # Bob borrows it
    lib.display_member_books(102)

    # Test 13: Error Cases - Non-existent Member/Book
    print("\n--- TEST 13: Error Handling ---")
    lib.borrow_book(999, 1)   # Non-existent member
    lib.borrow_book(101, 999) # Non-existent book
    lib.return_book(999, 1)   # Non-existent member
    lib.display_member_books(999)  # Non-existent member

    # Test 14: Final Status
    print("\n--- TEST 14: Final Library Status ---")
    print("\nAll Borrowed Books:")
    for transaction in lib.transactions:
        print(f"  {transaction['member_name']} has '{transaction['book_title']}'")

    print("\nAll Members and Their Books:")
    for member in lib.members:
        print(f"\n{member.name} ({member.id}):")
        if member.borrowed_books:
            # ตอนนี้ borrowed_books เก็บ Book object
            for book in member.borrowed_books:
                print(f"  - {book.title}")
        else:
            print("  (No books borrowed)")

    lib.display_available_books()

    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    test_library_system()