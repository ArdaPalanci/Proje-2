import os
import unittest
from database import create_tables, connect_db


class LibraryTest(unittest.TestCase):

    def setUp(self):
        if os.path.exists("library.db"):
            os.remove("library.db")
        create_tables()

    def test_book_insert(self):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO books (title, author, isbn, year, quantity) VALUES (?, ?, ?, ?, ?)",
            ("Test Kitap", "Test Yazar", "123456", 2024, 2)
        )

        conn.commit()

        cursor.execute("SELECT title FROM books WHERE isbn='123456'")
        result = cursor.fetchone()

        conn.close()

        self.assertEqual(result[0], "Test Kitap")

    def test_member_insert(self):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO members (name, email, phone) VALUES (?, ?, ?)",
            ("Test Üye", "test@test.com", "05550000000")
        )

        conn.commit()

        cursor.execute("SELECT name FROM members WHERE email='test@test.com'")
        result = cursor.fetchone()

        conn.close()

        self.assertEqual(result[0], "Test Üye")

    def test_loan_insert(self):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO books (title, author, isbn, year, quantity) VALUES (?, ?, ?, ?, ?)",
            ("Deneme Kitap", "Yazar", "999999", 2023, 1)
        )
        cursor.execute(
            "INSERT INTO members (name, email, phone) VALUES (?, ?, ?)",
            ("Deneme Üye", "deneme@test.com", "05551111111")
        )

        book_id = cursor.lastrowid - 1
        member_id = cursor.lastrowid

        cursor.execute(
            "INSERT INTO loans (book_id, member_id, loan_date, status) VALUES (?, ?, ?, ?)",
            (book_id, member_id, "2026-06-22", "borrowed")
        )

        conn.commit()

        cursor.execute("SELECT status FROM loans")
        result = cursor.fetchone()

        conn.close()

        self.assertEqual(result[0], "borrowed")


if __name__ == "__main__":
    unittest.main()
