# Toy Storey
PWS Link http://ariq-maulana-toystorey.pbp.cs.ui.ac.id/
## Tugas 3
### Pertanyaan-pertanyaan:
#### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery adalah elemen fundamental dalam pengimplementasian platform karena memastikan bahwa data dikirim dengan cepat, akurat, dan aman. Data delivery memastikan bahwa informasi dapat dikirimkan dari atau ke server, klien, maupun antar aplikasi. Tanpa adanya sistem data delivery, sebuah platform tidak dapat berfungsi secara optimal, karena pertukaran data yang diperlukan untuk berbagai tugas tidak dapat dilakukan dengan benar.
#### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON lebih populer dibandingkan XML terutama karena kesederhanaan, ringkas, dan integrasi langsung dengan JavaScript, yang membuatnya ideal untuk aplikasi web dan API modern. Meskipun XML masih memiliki kekuatan dalam hal schema dan validasi data yang kompleks, JSON sering kali dipilih karena efisiensi dan kemudahan penggunaannya dalam lingkungan pengembangan modern.

#### Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Metode `is_valid()` pada form Django adalah alat penting untuk memastikan bahwa data yang dikirim oleh pengguna memenuhi aturan validasi yang ditetapkan. Ini membantu dalam menjaga keamanan dan integritas data, meningkatkan pengalaman pengguna, dan mempermudah proses pengolahan data dengan memastikan bahwa hanya data yang valid yang diproses lebih lanjut.

#### Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` adalah komponen penting dalam melindungi aplikasi web Django dari serangan Cross-Site Request Forgery (CSRF). Tanpa token ini, aplikasi akan rentan terhadap eksploitasi yang dapat merusak data, melanggar privasi, dan menyebabkan kerusakan keamanan. Penyerang dapat membuat pengguna yang telah login di situs dan mengirimkan permintaan berbahaya, seperti mengubah pengaturan akun, melakukan transfer dana, atau menghapus data, tanpa sepengetahuan pengguna tersebut.

### Step-by-step Implementasi Checklist
#### Membuat input `form` untuk menambahkan objek model pada app sebelumnya.
1. Membuat file `forms.py` untuk menambahkan objek model dengan ModelForm

   ```
   from django.forms import ModelForm
   from main.models import Product

   class ProductForm(ModelForm):
       class Meta:
           model = Product
           fields = ['name', 'price', 'description', 'stock', 'image']
   ```
2. Menambahkan function `create_product_entry` untuk menghasilkan form yang dapat menambahkan data Product Entry secara otomatis ketika data di-submit dari form.

    ```
    def create_product_entry(request):
    form = ProductForm(request.POST, request.FILES)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
    ```
3. Membuat direktori template pada direktori utama dan menambahkan `base.html` untuk template dasar yang dapat digunakan sebagai kerangka umum untuk halaman web lainnya di dalam proyek.
   ```
   {% load static %}
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <meta name="viewport" content="width=device-width, initial-scale=1.0" />
       {% block meta %} {% endblock meta %}
     </head>
   
     <body>
       {% block content %} {% endblock content %}
     </body>
   </html>
   ```
4. Menambahkan import dan urlpatterns pada `urls.py`
   ```
   from main.views import show_main, create_product_entry
   ...
   urlpatterns = [
      path('', show_main, name='show_main'),
      path('create-product-entry', create_product_entry, name='create_product_entry'),
      ...
   ]
#### Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
Menambahkan fungsi views pada `views.py`
   Format XML:
   
   ```
   def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
   ```
   Format JSON:
   
   ```
   def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```
   Format XML by ID:

   ```
   def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
   ```
   Format JSON by ID;

   ```
   def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```
#### Membuat routing URL untuk masing-masing views yang telah ditambahkan
Menambahkan routing URL untuk masing-masing format views XML dan JSON pada `urls.py` dalam direktori `main`.
```
from django.urls import path
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```

## Tugas 2
### Step-by-step Implementasi Checklist
#### Membuat sebuah proyek Django baru
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
   
#### Membuat aplikasi dengan nama `main` pada proyek tersebut.
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

#### Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`.
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

#### Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib `name`, `price`, `description`
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

#### Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
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
#### Membuat sebuah routing pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.
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

#### Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat
1. Akses dan _login_ pada halaman PWS pada https://pbp.cs.ui.ac.id
2. Buat proyek baru dengan nama toystorey dengan menekan tombol `Create New Project`
3. Simpan credentials di tempat yang aman
4. Pada `settings.py` di direktori proyek `toy_storey`, tambahkan URL deployment PWS pada ALLOWED_HOSTS.
   
   ```
   ...
   ALLOWED_HOSTS = ["localhost", "127.0.0.1", "ariq-maulana-toystorey.pbp.cs.ui.ac.id"]
   ...
   ```
5. Jalankan perintah yang terdapat pada informasi _Project Command_ pada halaman PWS.
   
   ```
   git remote add pws http://pbp.cs.ui.ac.id/ariq.maulana/toystorey
   git branch -M master
   git push pws master
   ```
6. Tunggu sampai project selesai di_build_ dan project dapat dilihat di PWS

### Bagan _request client_ ke Web Aplikasi Berbasis Django
![image](https://github.com/user-attachments/assets/8b920369-750a-4ecf-aa9a-469c1a1e8b9d)

### Fungsi `git` dalam Pengembangan Perangkat Lunak
Git adalah sistem kontrol versi terdistribusi yang digunakan dalam pengembangan perangkat lunak untuk melacak perubahan kode, memfasilitasi kolaborasi tim, dan mengelola versi dengan efisien. Git memungkinkan pengembang untuk bekerja pada berbagai cabang secara bersamaan, menggabungkan perubahan, dan menyimpan riwayat versi secara lokal, sehingga memudahkan pengembalian ke versi sebelumnya dan memungkinkan kerja offline.

### Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Karena kemudahan penggunaannya, dokumentasi yang komprehensif, dan filosofi _batteries-included_ yang menyediakan fitur bawaan seperti autentikasi, manajemen database, dan panel admin, sehingga mengurangi kebutuhan untuk integrasi eksternal. Dengan komunitas yang aktif dan dukungan keamanan yang solid, Django memudahkan pemula untuk mempelajari pengembangan web dengan cepat dan efektif, sambil membangun aplikasi yang aman dan terstruktur dengan baik.

### Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena ia mengimplementasikan konsep Object-Relational Mapping, yang menghubungkan model objek dalam kode Python dengan tabel-tabel di database relasional. ORM memungkinkan pengembang untuk bekerja dengan data dalam bentuk objek Python, tanpa perlu menulis query SQL secara langsung. Ini mempermudah interaksi dengan database dan memungkinkan pengembang untuk fokus pada logika aplikasi daripada pada detail implementasi database.
