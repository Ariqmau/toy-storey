# Toy Storey
PWS Link http://ariq-maulana-toystorey.pbp.cs.ui.ac.id/
## Tugas 5
#### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Dalam CSS, urutan prioritas atau spesifisitas selector sangat penting untuk menentukan mana yang diterapkan pada elemen HTML ketika ada beberapa aturan yang bisa diterapkan. Dalam hal prioritas dari yang paling diprioritaskan:
!important > Inline Styles > ID Selector > Class/Attribute/Pseudo-class Selector > Type Selector > Universal Selector.
#### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design adalah kunci untuk menciptakan aplikasi web yang efektif dan menarik. Dengan semakin banyaknya pengguna yang mengakses internet melalui perangkat mobile, penting bagi pengembang untuk memastikan bahwa aplikasi mereka dapat menyesuaikan diri dengan berbagai ukuran layar dan memberikan pengalaman pengguna yang baik di semua platform. Contoh aplikasi yang suda menerapkan responsive design adalah Amazon dan yang belum adalah situs web pemerintah, terutama yang lebih tua yang belum menerapkan responsive design.
#### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- Margin adalah ruang di luar batas (border) elemen. Margin digunakan untuk mengatur jarak antara elemen satu dengan yang lainnya.
- Border adalah garis yang mengelilingi elemen. Border digunakan untuk memberikan batas visual pada elemen.
- Padding adalah ruang di dalam batas (border) elemen, antara konten dan border. Padding digunakan untuk mengatur ruang di dalam elemen.

Cara implementasi:
- pada file HTML:
```
<div class="box">
    Content goes here.
</div>
```
- pada file css:
```
.box {
    margin: 20px;                /* Jarak antar elemen */
    border: 2px solid blue;      /* Batas elemen */
    padding: 15px;               /* Ruang di dalam elemen */
}
```
#### Jelaskan konsep flex box dan grid layout beserta kegunaannya!
##### Flexbox
Flexbox adalah model tata letak satu dimensi yang memungkinkan elemen di dalam kontainer fleksibel untuk disusun secara horizontal atau vertikal. Ini dirancang untuk memberikan kontrol yang lebih baik atas penyebaran ruang di antara elemen dan penyesuaian ukuran elemen dalam kontainer. Flexbox ideal untuk tata letak yang sederhana, seperti menu navigasi, tombol, atau form. 

Kegunaan:
- Penanganan Ruang: Memudahkan untuk mendistribusikan ruang di antara elemen, baik secara horizontal maupun vertikal.
- Penyesuaian Responsif: Sangat berguna untuk desain responsif, karena elemen dapat dengan mudah menyesuaikan diri saat ukuran layar berubah.

##### Grid Layout
Grid Layout adalah model tata letak dua dimensi untuk menyusun elemen dalam grid. Ini memberikan kontrol yang lebih besar terhadap penyusunan elemen dalam baris dan kolom. Sangat baik untuk membuat tata letak yang lebih kompleks, seperti halaman dengan beberapa kolom dan baris, misalnya, layout dashboard, kartu, atau galeri gambar.

Kegunaan:
- Pengaturan Luas dan Tinggi: Memberikan kemampuan untuk mengatur tinggi dan lebar elemen dengan cara yang lebih terstruktur.
- Pengaturan Responsif: Mudah untuk membuat tata letak responsif dengan menggunakan media queries untuk mengubah ukuran grid berdasarkan ukuran layar.
### Step-by-step Implementasi Checklist
#### Implementasikan fungsi untuk menghapus dan mengedit product.
1. Membuat fungsi `edit_product` dan `delete_product` di dalam `views.py`

```
def edit_product(request, id):
    product = Product.objects.get(pk = id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```
2. add import dan routing url di dalam `main/urls.py`

```
from main.views import ... edit_product, delete_product
...
urlpatterns = [
   ...
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),
]
```
#### Kustomisasi halaman login, register, tambah product, halaman daftar product, navigation bar menjadi menarik dan responsive.
1. Menginisiasi pemanggilan Tailwind melalui CDN (Content Distribution Network) dengan meletakkan CDN di `base.html`.

```
<head>
  ...
  <script src="https://cdn.tailwindcss.com"></script>
  ...
</head>
```
2. Kustomasi menggunakan TailwindCSS
Mencoba-coba style-style yang bagus untuk diterapkan pad alemen-elemen HTML.

## Tugas 4
#### Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`?
   - `HttpResponseRedirect()` adalah kelas yang secara langsung membuat respons HTTP dengan status 302 (Found). Kita harus harus menyebutkan URL secara eksplisit ketika membuat objek ini.
   - `redirect()` adalah fungsi pembungkus yang membuat kode lebih mudah dibaca dan lebih fleksibel. Kita dapat menggunakan URL sebagai string, nama view, atau objek model

#### Jelaskan cara kerja penghubungan `model` Product dengan `User`!
Penghubungan dilakukan dengan cara menambahkan ForeignKey di model Product untuk merujuk ke model User. Dengan cara ini, kita dapat menghubungkan setiap produk dengan satu pengguna.

```
from django.db import models
from django.contrib.auth.models import User
import uuid

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
- ForeignKey: Dengan menambahkan ForeignKey ke model Product, Anda membuat hubungan satu ke banyak (one-to-many), di mana satu pengguna dapat memiliki banyak produk.
- on_delete=models.CASCADE: Ini berarti jika pengguna dihapus, semua produk yang terkait dengan pengguna tersebut juga akan dihapus.

#### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication adalah tentang memverifikasi identitas pengguna, sedangkan Authorization adalah tentang memberikan akses berdasarkan identitas tersebut. Saat pengguna login, Sistem melakukan autentikasi dengan memeriksa kredensial yang diberikan (nama pengguna dan kata sandi) terhadap data yang tersimpan dalam database. Jika kredensial valid, pengguna dianggap terautentikasi, dan sesi pengguna dibuat. Sistem kemudian melakukan otorisasi untuk menentukan halaman atau sumber daya yang dapat diakses oleh pengguna berdasarkan hak akses yang dimiliki. Django memiliki model pengguna (User) dan sistem autentikasi yang menangani login dan logout dengan menggunakan import django.contrib.auth untuk melakukan autentikasi. Django juga memiliki sistem izin (permissions) dan grup untuk mengelola otorisasi.

#### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login dengan menggunakan session dan cookies.

Session:
Ketika pengguna berhasil login, Django membuat sesi untuk pengguna tersebut. Sesi ini menyimpan informasi tentang pengguna di server.
Django secara otomatis memberikan ID sesi yang unik kepada pengguna dan menyimpannya di cookie di browser pengguna.

Cookies:
Cookie ini berisi ID sesi yang digunakan untuk mengidentifikasi sesi pengguna di server.
Setiap kali pengguna mengakses aplikasi, cookie ini dikirim kembali ke server. Django menggunakan ID sesi ini untuk menemukan informasi pengguna yang relevan di sisi server.

Kegunaan lain dari cookies adalah menyimpan preferensi pengguna, tracking dan analytics web, menjaga status login, dan personalisasi konten. Tidak semua cookies aman digunakan, Cookies dapat disalahgunakan jika tidak dikonfigurasi dengan baik. Contohnnya penyerang dapat mencuri cookies pengguna dan menggunakan ID sesi tersebut untuk mengakses akun pengguna.

### Step-by-step Implementasi Checklist
#### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
##### Registrasi
1. Menambahkan import dan fungsi pada 'view.py' untuk registrasi

```
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
...
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
...
```
2. Membuat `register.html` pada `main/templates` yang berisi

```
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```
3. Menambahkan import dan path url pada `url.py` untuk fungsi register yang telah dibuat.

```
from main.views import register
...
urlpatterns = [
    ...
    path('register/', register, name='register'),
    ...
]
```
##### Login
1. Menambahkan import dan fungsi pada 'view.py' untuk login

```
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
...
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
...
```
2. Membuat `login.html` pada `main/templates` yang berisi

```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
3. Menambahkan import dan path url pada `url.py` untuk fungsi login yang telah dibuat.

```
from main.views import login_user
...
urlpatterns = [
   ...
   path('login/', login_user, name='login'),
]
```
4. Merestriksi akses halaman main dengan import dan menambahkan baris kode berikut di atas fungsi show_main pada `views.py`

```
from django.contrib.auth.decorators import login_required
...
...
@login_required(login_url='/login')
def show_main(request):
...
```
##### Logout
1. Menambahkan import dan fungsi pada 'view.py' untuk logout

```
from django.contrib.auth import logout
...
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
2. Menambahkan button logout pada `main.html`.

```
...
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
...
```
3. Menambahkan import dan path url pada `url.py` untuk fungsi logout yang telah dibuat.

```
from main.views import logout_user
...
urlpatterns = [
   ...
   path('logout/', logout_user, name='logout'),
]
```
#### Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
Menambahkan akun dan dummy data

#### Menghubungkan model `Product` dengan `User`.
Menambahkan ForeignKey di pada `models.py` Product untuk merujuk ke model User. Dengan cara ini, kita dapat menghubungkan setiap produk dengan satu pengguna.

```
from django.db import models
from django.contrib.auth.models import User
import uuid

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
#### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
1. Menambahkan username dan last_login pada context dalam fungsi `show_main` di `views.py`.

```
def show_main(request):
    product_entries = Product.objects.filter(user=request.user)

    context = {
        'username': request.user.username,
        ...
        'last_login': request.COOKIES['last_login'],
    }
```
2. Menambahkan kode dalam `main.html` untuk menampilkan username dan last login pada halaman.

```
...
<p>Logged in as {{ username }}</p>
<p>Sesi terakhir login: {{ last_login }}</p>
...
```
## Tugas 3
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
## Screenshot dari hasil akses URL pada Postman
JSON
![image](https://github.com/user-attachments/assets/37e08ff1-7231-48e6-a3eb-c04d111e97e6)
XML
![image](https://github.com/user-attachments/assets/2bd0097f-c0dd-46dc-a2dd-635c87ada93d)
JSON by ID
![image](https://github.com/user-attachments/assets/e0ea5eeb-f6dd-45d6-8c5a-eaef39cead58)
XML by ID
![image](https://github.com/user-attachments/assets/26a8a394-dd9e-4751-9429-e1dc9f4355b3)

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
