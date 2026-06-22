from database import create_tables
from operations import (
    add_book, list_books, update_book, delete_book,
    add_member, list_members, update_member, delete_member,
    add_loan, list_loans, return_book, delete_loan
)


def book_menu():
    while True:
        print("\n--- Kitap İşlemleri ---")
        print("1- Kitap ekle")
        print("2- Kitap listele")
        print("3- Kitap güncelle")
        print("4- Kitap sil")
        print("0- Ana menü")

        secim = input("Seçiminiz: ")

        if secim == "1":
            add_book()
        elif secim == "2":
            list_books()
        elif secim == "3":
            update_book()
        elif secim == "4":
            delete_book()
        elif secim == "0":
            break
        else:
            print("Hatalı seçim yaptınız.")


def member_menu():
    while True:
        print("\n--- Üye İşlemleri ---")
        print("1- Üye ekle")
        print("2- Üye listele")
        print("3- Üye güncelle")
        print("4- Üye sil")
        print("0- Ana menü")

        secim = input("Seçiminiz: ")

        if secim == "1":
            add_member()
        elif secim == "2":
            list_members()
        elif secim == "3":
            update_member()
        elif secim == "4":
            delete_member()
        elif secim == "0":
            break
        else:
            print("Hatalı seçim yaptınız.")


def loan_menu():
    while True:
        print("\n--- Ödünç Alma İşlemleri ---")
        print("1- Kitap ödünç ver")
        print("2- Ödünç kayıtlarını listele")
        print("3- Kitap teslim al")
        print("4- Ödünç kaydı sil")
        print("0- Ana menü")

        secim = input("Seçiminiz: ")

        if secim == "1":
            add_loan()
        elif secim == "2":
            list_loans()
        elif secim == "3":
            return_book()
        elif secim == "4":
            delete_loan()
        elif secim == "0":
            break
        else:
            print("Hatalı seçim yaptınız.")


def main():
    create_tables()

    while True:
        print("\n===== Kütüphane Yönetim Sistemi =====")
        print("1- Kitap işlemleri")
        print("2- Üye işlemleri")
        print("3- Ödünç alma işlemleri")
        print("0- Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            book_menu()
        elif secim == "2":
            member_menu()
        elif secim == "3":
            loan_menu()
        elif secim == "0":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Hatalı seçim yaptınız.")


main()
