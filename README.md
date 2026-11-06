# Sistem Pelaporan Kendala IT (IT Ticketing System)

Aplikasi *web* sederhana untuk melaporkan kendala IT dan menampilkannya pada *dashboard*. Proyek ini dibangun untuk mendemonstrasikan pemahaman *Full-Stack Development* dasar.

## Tech Stack
* **Front-End:** HTML, CSS, Vanilla JavaScript
* **Back-End:** Python (Flask)
* **Database:** MySQL

## Fitur
* Form pelaporan kendala (Create)
* Dashboard daftar tiket (Read)
* Integrasi *Front-End* dan *Back-End* menggunakan REST API (Fetch API)

## Cara Menjalankan Aplikasi Lokal
1. Pastikan Anda telah menginstal Python dan MySQL (XAMPP).
2. Buat database di MySQL dengan nama `it_support_db` dan *import* tabel `tickets`.
3. Buka terminal dan instal *library* yang dibutuhkan:
   `pip install flask mysql-connector-python flask-cors`
4. Jalankan server Back-End:
   `python app.py`
5. Buka file `index.html` di *browser* untuk menggunakan aplikasi.