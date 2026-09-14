# Individual Assignment 2

**Nama:** Kaysan Salman Ali Kusumah
**NPM:** 2506540670
**Kelas:** PBP F

## Deskripsi Proyek

Project ini merupakan website portofolio pribadi yang dikembangkan menggunakan Django. Website menampilkan informasi mengenai diri, pengalaman, kemampuan, pendidikan, kontak, serta project yang telah dikerjakan.

Pada Individual Assignment 2, saya menambahkan fitur **Projects** menggunakan konsep Django MVT. Data project disimpan menggunakan model Django dan database, dapat dikelola melalui Django Admin, kemudian ditampilkan secara dinamis pada halaman Projects.

Fitur yang ditambahkan pada Individual Assignment 2 meliputi:

* Model `Project`
* Django Admin untuk mengelola data project
* View untuk mengambil data project dari database
* URL `/projects/`
* Template `projects.html`
* Navigasi Projects dari halaman utama
* Responsive styling untuk halaman Projects
* Unit test untuk halaman Projects

## Teknologi yang Digunakan

Teknologi yang digunakan dalam project ini adalah:

* Python
* Django
* HTML
* CSS
* SQLite
* Git
* GitHub

## Model Project

Model `Project` digunakan untuk menyimpan informasi mengenai project portofolio. Model ini memiliki beberapa atribut:

* `title` untuk menyimpan nama project.
* `description` untuk menyimpan deskripsi project.
* `project_type` untuk menentukan jenis project.
* `technologies` untuk menyimpan teknologi yang digunakan.
* `github_url` untuk menyimpan link repository GitHub.
* `created_at` untuk mencatat waktu pembuatan data.

Data project dapat ditambahkan, diubah, dan dihapus melalui Django Admin.

## Alur Halaman Projects

Ketika pengguna membuka halaman `/projects/`, request pertama kali diterima oleh `portofolio/urls.py` sebagai URL configuration utama proyek. Request kemudian diteruskan ke `main/urls.py` menggunakan `include()`.

Pada `main/urls.py`, URL `/projects/` diarahkan ke fungsi `show_projects` pada `main/views.py`. View tersebut mengambil seluruh data dari model `Project` menggunakan `Project.objects.all()`.

Data yang diperoleh kemudian dimasukkan ke dalam context dan dikirimkan ke template `projects.html`. Template menggunakan data tersebut untuk menghasilkan HTML secara dinamis. HTML yang dihasilkan Django kemudian dikirim kembali ke browser untuk ditampilkan kepada pengguna.

Secara sederhana, alurnya adalah:

Browser
   ↓
portofolio/urls.py
   ↓
main/urls.py
   ↓
show_projects() pada views.py
   ↓
Project pada models.py
   ↓
Database
   ↓
Data dikembalikan ke View
   ↓
projects.html
   ↓
HTML Response
   ↓
Browser
```

## Setup dan Instalasi

1. Clone Repository
    git clone <URL_REPOSITORY>
    cd myportofolio

2. Membuat Virtual Environment
    Pada Windows PowerShell:
    python -m venv env, Kemudian aktifkan virtual environment: \env\Scripts\Activate.ps1

3. Install Dependencies
    pip install -r requirements.txt

4. Menjalankan Migration
    python manage.py migrate

5. Menjalankan Development Server
    python manage.py runserver


Website dapat diakses melalui: http://127.0.0.1:8000/

Halaman Projects dapat diakses melalui: http://127.0.0.1:8000/projects/

## Django Admin

Untuk mengelola data Project melalui Django Admin, buat superuser dengan:
python manage.py createsuperuser


Kemudian jalankan server: python manage.py runserver

Django Admin dapat diakses melalui: http://127.0.0.1:8000/admin/


Pada halaman admin, terdapat menu **Projects** yang digunakan untuk mengelola data project.

## Tahapan Pengembangan Individual Assignment 2

Pengembangan dilakukan secara bertahap.

### Tahap 1 — Model

Menambahkan model `Project` pada `main/models.py` dengan field yang dibutuhkan untuk menyimpan data project.

Setelah model dibuat, migration dijalankan untuk menerapkan perubahan struktur database.

### Tahap 2 — Backend

Model `Project` didaftarkan ke Django Admin. Kemudian dibuat `show_projects` pada `main/views.py` untuk mengambil data project dari database.

Routing juga ditambahkan pada `main/urls.py` dan dihubungkan dengan URL configuration utama proyek.

### Tahap 3 — Frontend

Membuat `projects.html` untuk menampilkan data project secara dinamis menggunakan template Django.

Halaman homepage juga diperbarui sehingga navigasi **Projects** mengarah ke halaman `/projects/`.

### Tahap 4 — Styling

Menambahkan CSS untuk membuat halaman Projects lebih rapi dan responsif. Project ditampilkan dalam bentuk card dengan layout grid yang menyesuaikan ukuran layar.

### Tahap 5 — Testing

Menambahkan unit test untuk memastikan halaman Projects memenuhi tiga requirement pengujian:

1. URL dapat diakses dan menggunakan template yang tepat.
2. Data model muncul pada halaman HTML ketika terdapat data.
3. Halaman HTML menampilkan pesan kondisi kosong ketika belum terdapat data.

## Unit Test

Unit test dijalankan menggunakan:

python manage.py test

Hasil pengujian:


Found 3 test(s).
Ran 3 tests in 0.073s

OK


Ketiga test berhasil dijalankan tanpa kegagalan.

## Git Development History

Pengembangan Individual Assignment 2 dilakukan secara bertahap menggunakan beberapa commit dengan pesan yang menjelaskan perubahan yang dilakukan.

Commit yang dibuat antara lain:


feat: add Project model for portfolio projects
feat: add project admin, view, and routing
feat: add projects page and homepage navigation
style: add responsive styling forprojects page
test: add project page unit tests


## Pertanyaan Reflektif

### 1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser.

Ketika pengguna membuka halaman `/projects/`, request dari browser pertama kali diterima oleh Django dan diproses melalui `portofolio/urls.py` sebagai URL configuration utama proyek. File tersebut kemudian meneruskan request ke `main/urls.py` menggunakan `include()`.

Pada `main/urls.py`, URL `/projects/` diarahkan ke fungsi `show_projects` pada `main/views.py`. View tersebut mengambil data project dari database melalui model `Project` menggunakan `Project.objects.all()`.

Data yang diperoleh kemudian dimasukkan ke dalam context dan dikirim ke template `projects.html`. Template menggunakan data tersebut untuk menghasilkan HTML secara dinamis. Django kemudian mengirimkan HTML sebagai response kepada browser, dan browser merender HTML tersebut sehingga halaman Projects dapat dilihat oleh pengguna.

Peran masing-masing komponen adalah:

* **`portofolio/urls.py`**: routing utama proyek.
* **`main/urls.py`**: menentukan URL pada aplikasi dan view yang menangani URL tersebut.
* **View**: menjalankan logika aplikasi dan mengambil data dari model.
* **Model**: merepresentasikan data project yang disimpan pada database.
* **Template**: menentukan bagaimana data ditampilkan sebagai HTML.

### 2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template?

Data sebaiknya disimpan pada model karena data project dapat berubah, bertambah, atau dihapus. Dengan menyimpan data pada model dan database, data dapat dikelola melalui Django Admin tanpa harus mengubah kode HTML pada template.

Jika data ditulis langsung pada template, setiap perubahan data mengharuskan developer mengubah file HTML. Hal tersebut akan menyulitkan pemeliharaan ketika jumlah project semakin banyak.

Dengan model, template dapat menampilkan data secara dinamis menggunakan perulangan seperti:


{% for project in projects %}


Ketika project baru ditambahkan ke database, project tersebut dapat langsung ditampilkan oleh template tanpa perlu menambahkan HTML baru secara manual.

Pemisahan antara data, logika, dan tampilan juga membuat aplikasi lebih mudah dipelihara dan dikembangkan. Jika nantinya diperlukan field tambahan seperti kategori, teknologi, atau link repository, perubahan dapat dilakukan pada model dan bagian terkait tanpa harus menulis ulang seluruh data pada template.

### 3. Apa perbedaan fungsi `makemigrations` dan `migrate` pada Django?

`makemigrations` digunakan untuk membuat file migration berdasarkan perubahan yang dilakukan pada model. File migration tersebut berisi instruksi mengenai perubahan struktur database.

Sementara itu, `migrate` digunakan untuk menerapkan migration tersebut ke database.

Alurnya adalah:

Perubahan models.py
       ↓
makemigrations
       ↓
File migration dibuat
       ↓
migrate
       ↓
Perubahan diterapkan ke database


Pada Individual Assignment 2, saya menambahkan model `Project` pada `main/models.py`. Setelah itu saya menjalankan:


python manage.py makemigrations


Django kemudian membuat migration untuk model `Project`.

Selanjutnya saya menjalankan:

python manage.py migrate


Migration tersebut kemudian diterapkan ke database sehingga data `Project` dapat disimpan dan digunakan oleh aplikasi.

## AI Disclosure

Dalam pengerjaan Individual Assignment 2, saya menggunakan **ChatGPT** sebagai alat bantu pembelajaran, pengembangan, debugging, testing, dan dokumentasi.

AI digunakan untuk membantu:

* Memahami requirement Individual Assignment 2.
* Memahami konsep Django MVT.
* Merancang struktur model `Project`.
* Memberikan contoh implementasi model.
* Membantu menyusun view dan URL.
* Membantu menyusun template `projects.html`.
* Membantu menyusun responsive CSS.
* Menganalisis error `NoReverseMatch`.
* Membantu menyusun unit test.
* Menjelaskan hasil unit test.
* Membantu menyusun dokumentasi README.
* Membantu memahami dan mengatur Git commit secara bertahap.

Kode yang diberikan oleh AI tidak langsung dianggap selesai. Kode diterapkan pada project, dijalankan, diperiksa, dan disesuaikan dengan kebutuhan project. Unit test juga dijalankan secara langsung untuk memastikan implementasi berjalan.

### Strategi Prompting

Strategi prompting yang digunakan meliputi:

1. **Prompt eksplorasi**, untuk memahami requirement dan menentukan tahapan pengerjaan.
2. **Prompt implementasi**, untuk mendapatkan contoh implementasi berdasarkan kebutuhan project.
3. **Prompt debugging**, dengan memberikan error atau output terminal agar penyebab masalah dapat dianalisis.
4. **Prompt verifikasi**, untuk memeriksa apakah implementasi dan unit test telah memenuhi requirement.
5. **Prompt dokumentasi**, untuk membantu menyusun README dan menjelaskan proses pengerjaan.

### AI Prompting Log

| No. | Tahap       | Tujuan Prompt                                                   | Bagian yang Dibantu AI                                |
| --- | ----------- | --------------------------------------------------------------- | ----------------------------------------------------- |
| 1   | Requirement | Memahami apa yang perlu dikerjakan pada Individual Assignment 2 | Memecah requirement menjadi beberapa tahap pengerjaan |
| 2   | Model       | Menentukan struktur model `Project`                             | Struktur model dan field                              |
| 3   | Migration   | Memahami proses perubahan database                              | Penjelasan `makemigrations` dan `migrate`             |
| 4   | Admin       | Membuat model dapat dikelola melalui Django Admin               | Registrasi model `Project`                            |
| 5   | Backend     | Menghubungkan model dengan halaman                              | View `show_projects` dan routing                      |
| 6   | Debugging   | Mengatasi `NoReverseMatch`                                      | Analisis namespace URL                                |
| 7   | Template    | Menampilkan data project secara dinamis                         | Struktur `projects.html`                              |
| 8   | Styling     | Membuat halaman Projects responsive                             | Struktur CSS dan responsive layout                    |
| 9   | Testing     | Memenuhi tiga kasus pengujian                                   | Penyusunan `main/tests.py`                            |
| 10  | Verifikasi  | Memastikan test berhasil                                        | Interpretasi hasil `python manage.py test`            |
| 11  | Git         | Membuat riwayat pengembangan bertahap                           | Pembagian commit dan commit message                   |
| 12  | Dokumentasi | Menyusun README dan AI Disclosure                               | Struktur dokumentasi dan log prompting                |
| 13  | Refleksi    | Menjawab pertanyaan reflektif                                   | Penjelasan alur Django, model, dan migration          |

AI digunakan sebagai alat bantu dalam proses pembelajaran dan pengembangan, sedangkan implementasi, eksekusi project, pengujian, dan pemeriksaan hasil dilakukan pada repository project.
