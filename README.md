# Tugas 2
PWS Link http://ariq-maulana-toystorey.pbp.cs.ui.ac.id/
## Step-by-step Implementasi Checklist
### Membuat sebuah proyek Django baru
1. Buat direktori baru bernama `toy-storey`, ini adalah direktori utama
2. Buat _virtual environment_ dengan menjalankan perintah berikut di _command prompt_ yang sudah berada di dalam direktori `toy-storey`.
   
   ```
   python -m venv env
   ```
   Nyalakan _virtual environment_ dengan menjalankan perintah berikut
   
   ```
   env\Scripts\activate
   ```
3. Di dalam direktori utama tersebut, buat file txt baru bernama `requirements.txt` yang berisi beberapa _dependencies_ berikut.
   
   ```
   django
   gunicorn
   whitenoise
   psycopg2-binary
   requests
   urllib3
   ```
4. Install _dependencies_ tersebut dengan menjalankan perintah berikut di _command prompt_.

   ```
   pip install -r requirements.txt
   ```
5. Buat proyek Django bernama `toy-storey` dengan menjalankan perintah berikut di _command prompt_.
   
   ```
   django-admin startproject toy_storey .
   ```
   Subdirektori proyek Django bernama `toy_storey` akan muncul di dalam direktori utama.
   
### Membuat aplikasi dengan nama `main` pada proyek tersebut.
1. Jalankan perintah berikut di _command prompt_ untuk membuat aplikasi baru.

   ```
   python manage.py startapp main
   ```
   Subdirektori baru dengan nama main akan terbentuk.
3. Daftarkan `main` ke dalam proyek dengan cara membuka file `settings.py` dalam direktori utama `toy-storey`, lalu tambahkan `'main'` sebagai elemen paling terakhir di dalam `INSTALLED_APPS`.

   ```
   INSTALLED_APPS = [
    ...,
    'main'
   ]
   ```

### Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`.
1. Buka `urls.py` yang ada di dalam direktori utama `toy_storey`.
2. Tambahkan import fungsi include dari django.urls.

   ```
   ...
   from django.urls import path, include
   ...
   ```
4. Di dalam variabel `urlpatterns` tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan main.

   ```
   urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
   ]
   ```

### Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib `name`, `price`, `description`
1. Buka berkas `models.py` pada aplikasi `main`, lalu isi dengan kode berikut.

   ```
   from django.db import models
   class Product(models.Model):
      name = models.CharField(max_length=255)
      price = models.IntegerField()
      description = models.TextField()
      aura = models.IntegerField()
      playability = models.FloatField()
   ```
2. Buat migrasi model dengan cara menjalankan perintah berikut di _command prompt_ di dalam direktori utama `toy-storey`.

   ```
   python manage.py makemigrations
   ```
   Jalankan perintah berikut untuk menerapkan migrasi.
   
   ```
   python manage.py migrate
   ```
   Setiap kali melakukan perubahan pada model, seperti menambahkan atau mengubah atribut, WAJIB melakukan migrasi untuk merefleksikan perubahan tersebut.

### Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
1. Buka file `views.py` pada aplikasi `main`, kemudian tambahkan import fungsi render dari django.shortcuts.

   ```
   from django.shortcuts import render
   ```
3. Tambahkan fungsi `show_main` di bawah `import`.

   ```
    def show_main(request):
        context = {
            'app_name' : 'Toy Storey',
            'name': 'Ariq Maulana Malik Ibrahim',
            'class': 'PBP D'
        }
    return render(request, "main.html", context)
   ```
### Membuat sebuah routing pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.
1. Buat file `urls.py` di dalam direktori `main`.
2. Isi file tersebut dengan kode berikut.

   ```
   from django.urls import path
   from main.views import show_main
    
   app_name = 'main'
    
   urlpatterns = [
        path('', show_main, name='show_main'),
   ]
   ```
   Kode tersebut menggunakan fungsi show_main dari modul main.views sebagai tampilan yang akan ditampilkan ketika URL terkait diakses.

### Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat
(Belum dilakukan karena ada kendala teknis)

## Bagan _request client_ ke Web Aplikasi Berbasis Django

## Fungsi `git` dalam Pengembangan Perangkat Lunak


## Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

## Mengapa model pada Django disebut sebagai ORM?
