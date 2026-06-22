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

# Proje Süreci

Bu projede Python ve SQLite kullanılarak basit bir Kütüphane Yönetim Sistemi geliştirilmiştir. İlk olarak veritabanı tasarlanmış ve kitaplar, üyeler ve ödünç alma işlemleri için gerekli tablolar oluşturulmuştur. Daha sonra Python ile SQLite veritabanına bağlantı kurulmuş ve CRUD (Create, Read, Update, Delete) işlemleri geliştirilmiştir. Son aşamada kullanıcıların sistemi kullanabilmesi için komut satırı tabanlı bir menü hazırlanmıştır.

# İzlenen Süreç

1. GitHub üzerinde proje deposu oluşturuldu.
2. Veritabanı tasarımı yapıldı.
3. SQL tabloları ve ilişkileri oluşturuldu.
4. Python ile veritabanı bağlantısı gerçekleştirildi.
5. Kitap işlemleri geliştirildi.
6. Üye işlemleri geliştirildi.
7. Ödünç alma işlemleri geliştirildi.
8. Test senaryoları oluşturuldu.
9. README ve dokümantasyon tamamlandı.

# Zorlandığım Kısımlar

Projede en çok zorlandığım kısım tablolar arasındaki ilişkileri doğru şekilde kurmak ve ödünç alma işlemlerinde kitap stok bilgisini güncel tutmaktı. Ayrıca SQL sorgularının Python içerisinden doğru şekilde çalıştırılması sırasında hata kontrolleri eklemek gerekti.

# Öğrendiklerim

Bu proje sayesinde SQL veritabanı tasarımı, foreign key kullanımı, CRUD işlemleri, Python ile SQLite bağlantısı ve GitHub üzerinden sürüm kontrolü konularında deneyim kazandım. Ayrıca proje geliştirirken düzenli commit atmanın önemini öğrendim.

# Kullanılan Teknolojilerin Rolü

## Python

Programın kullanıcı arayüzünü ve veritabanı işlemlerini gerçekleştirmek için kullanılmıştır.

## SQL

Verilerin saklanması, tabloların oluşturulması ve ilişkilerin kurulması için kullanılmıştır.

## GitHub

Projenin sürüm kontrolünü sağlamak ve geliştirme sürecini takip etmek amacıyla kullanılmıştır.

# Bağımlılıklar

* Python 3.x
* SQLite (Python ile birlikte gelmektedir)

Harici bir kütüphane kullanılmamıştır.
