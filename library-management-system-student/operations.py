from datetime import date
from database import connect_db


# Kitap ekleme
def add_book():
    title = input("Kitap adı: ")
    author = input("Yazar adı: ")
    isbn = input("ISBN: ")
    year = input("Yayın yılı: ")
    quantity = int(input("Stok adedi: "))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO books (title, author, isbn, year, quantity) VALUES (?, ?, ?, ?, ?)",
        (title, author, isbn, year, quantity)
    )

    conn.commit()
    conn.close()
    print("Kitap eklendi.")


def list_books():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    print("\nKitap Listesi")
    for book in books:
        print(book)

    conn.close()


def update_book():
    book_id = int(input("Güncellenecek kitap ID: "))
    title = input("Yeni kitap adı: ")
    author = input("Yeni yazar adı: ")
    isbn = input("Yeni ISBN: ")
    year = input("Yeni yayın yılı: ")
    quantity = int(input("Yeni stok adedi: "))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE books SET title=?, author=?, isbn=?, year=?, quantity=? WHERE id=?",
        (title, author, isbn, year, quantity, book_id)
    )

    conn.commit()
    conn.close()
    print("Kitap güncellendi.")


def delete_book():
    book_id = int(input("Silinecek kitap ID: "))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM books WHERE id=?", (book_id,))

    conn.commit()
    conn.close()
    print("Kitap silindi.")


# Üye işlemleri
def add_member():
    name = input("Üye adı soyadı: ")
    email = input("E-posta: ")
    phone = input("Telefon: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO members (name, email, phone) VALUES (?, ?, ?)",
        (name, email, phone)
    )

    conn.commit()
    conn.close()
    print("Üye eklendi.")


def list_members():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()

    print("\nÜye Listesi")
    for member in members:
        print(member)

    conn.close()


def update_member():
    member_id = int(input("Güncellenecek üye ID: "))
    name = input("Yeni ad soyad: ")
    email = input("Yeni e-posta: ")
    phone = input("Yeni telefon: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE members SET name=?, email=?, phone=? WHERE id=?",
        (name, email, phone, member_id)
    )

    conn.commit()
    conn.close()
    print("Üye güncellendi.")


def delete_member():
    member_id = int(input("Silinecek üye ID: "))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM members WHERE id=?", (member_id,))

    conn.commit()
    conn.close()
    print("Üye silindi.")


# Ödünç alma işlemleri
def add_loan():
    book_id = int(input("Kitap ID: "))
    member_id = int(input("Üye ID: "))
    today = date.today().isoformat()

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT quantity FROM books WHERE id=?", (book_id,))
    book = cursor.fetchone()

    if book is None:
        print("Bu ID ile kitap bulunamadı.")
    elif book[0] <= 0:
        print("Bu kitaptan stokta yok.")
    else:
        cursor.execute(
            "INSERT INTO loans (book_id, member_id, loan_date, status) VALUES (?, ?, ?, ?)",
            (book_id, member_id, today, "borrowed")
        )
        cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE id=?", (book_id,))
        conn.commit()
        print("Kitap ödünç verildi.")

    conn.close()


def list_loans():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT loans.id, books.title, members.name, loans.loan_date, loans.return_date, loans.status
        FROM loans
        INNER JOIN books ON loans.book_id = books.id
        INNER JOIN members ON loans.member_id = members.id
    """)

    loans = cursor.fetchall()

    print("\nÖdünç Kayıtları")
    for loan in loans:
        print(loan)

    conn.close()


def return_book():
    loan_id = int(input("Teslim alınacak ödünç kayıt ID: "))
    today = date.today().isoformat()

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT book_id, status FROM loans WHERE id=?", (loan_id,))
    loan = cursor.fetchone()

    if loan is None:
        print("Kayıt bulunamadı.")
    elif loan[1] == "returned":
        print("Bu kitap zaten teslim edilmiş.")
    else:
        book_id = loan[0]
        cursor.execute(
            "UPDATE loans SET return_date=?, status=? WHERE id=?",
            (today, "returned", loan_id)
        )
        cursor.execute("UPDATE books SET quantity = quantity + 1 WHERE id=?", (book_id,))
        conn.commit()
        print("Kitap teslim alındı.")

    conn.close()


def delete_loan():
    loan_id = int(input("Silinecek ödünç kayıt ID: "))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM loans WHERE id=?", (loan_id,))

    conn.commit()
    conn.close()
    print("Ödünç kaydı silindi.")
