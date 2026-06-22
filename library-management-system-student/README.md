# Kütüphane Yönetim Sistemi

Bu proje Python ve SQLite kullanılarak yapılmış basit bir kütüphane yönetim sistemidir.  
Proje veritabanı dersi için hazırlanmıştır.

## Projenin Amacı

Bu sistemde kitaplar, üyeler ve ödünç alma kayıtları tutulur.  
Kullanıcı komut satırından seçim yaparak kayıt ekleyebilir, listeleyebilir, güncelleyebilir ve silebilir.

## Kullanılanlar

- Python
- SQLite
- SQL
- Git / GitHub

## Dosyalar

- `main.py`: Programın ana menüsü
- `operations.py`: Kitap, üye ve ödünç alma işlemleri
- `database.py`: Veritabanı bağlantısı
- `schema.sql`: Tabloların oluşturulduğu SQL dosyası
- `sample_data.sql`: Örnek veriler
- `test_library.py`: Basit testler
- `README.md`: Proje açıklaması

## Veritabanı Tabloları

Projede 3 tablo vardır:

1. books
2. members
3. loans

`loans` tablosunda kitap ve üye bilgileri foreign key ile bağlanmıştır.

## Programı Çalıştırma

Önce proje klasörüne girilir:

```bash
cd library-management-system
```

Sonra program çalıştırılır:

```bash
python main.py
```

## Testleri Çalıştırma

```bash
python -m unittest test_library.py
```

## GitHub Kullanımı

Projeyi GitHub'a yüklerken kullandığım genel commit mesajları:

```text
Initial project setup
Add database files
Add book operations
Add member operations
Add loan operations
Add test file
Update README
```

## Not

Bu proje temel CRUD işlemlerini ve SQL tablo ilişkilerini göstermek için yapılmıştır.
