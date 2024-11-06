
<h1> Tugas 2</h1>

<h2> 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). </h2>
   Jawab :
   1. Saya membuat folder dengan virtual environment baru agar tidak mengganggu versi library di global pada local saya.
   2. Menggunakan CMD saya membuat project django baru dengan meng run "django-admin startproject suiseishop .", saya menggunakan titik agar folder tidak terbuat 2 kali.
   3. Pindah ke vs code saya langsung me run python manage.py runserver untuk membuat proyek dengan python manage.py startapp main untuk membuat aplikasi bernama main.
   4. Saya langsung melakukan setup host dan mengubah settings.py pada bagian installed apps dan menambahkan 'main'.
   5. Saya langsung membuat template html dan membuat html sedemikian rupa sehingga nanti value pada views.py bisa di terapkan di html.
   6. Kemudian saya menambahkan fungsi dari library berupa include di urls proyek utama dan menambahkan path baru tanpa url ("") agar mainpage langsung tertuju ke main.urls.
   7. Sama halnya dengan urls pada proyek utama, proyek pada main juga menggunakan url kosong agar fungsi pada views langsung ditampilkan.
   8. Views yang sudah dikaitkan ke html menggunakan fungsi show_att (atribut) akan mereturn hasil render yang berupa HttpsResponse yang berisi templates pada html.

<h2>2. Bagan dari client hingga html </h2>

                    Client (Browser)
                            |
                            |
    1. Client membuat HTTP request (misal, membuka URL)
                            |
                            v
                    Django URLs (urls.py)
                            |
                            |
    2. Django memeriksa `urls.py` untuk mencocokkan URL request 
            dengan pattern / aplikasi yang ada
                    contoh urls.py :

                    "app_name = 'main'

                    urlpatterns = [
                        path('', views.show_att)
                    ]"
                            |
                            |
        pada contoh ini apabila user hanya membuka link 
        awal (tanpa /"***" lain) maka fungsi show_att akan ter trigger
                            |
                            |
                            v
                Django Views (views.py)
                            |
                            |
    3. `views.py` menerima request dan memberikan response pada client 
       tergantung dari penggunaan fungsi yang telah ditentukan sesuai request yang masuk
       pada kasus ini views.py akan menyediakan fungsi show_att pada user:
                            |
                            |
       contoh views.py :
            def show_att(request):
            att = {
                'nama_apk' : 'Suisei Shop',
                'nama' : "Christian Yudistira Hermawan",
                'kelas' : "PBP F"
            }
            return render(request, 'att.html', att)
                            |
                            |
        fungsi ini akan menerima request dan memberikan render 
            berupa httpresponse dengan html
                            |   
                            v
                Django Models (models.py)
                            |
                            |
    4. Jika perlu, `views.py` mengambil/memodifikasi data dari/ke database menggunakan `models.py`
                            |
                            |
            contoh models.py:
            class ProductEntry(models.Model):
                name = models.CharField(max_length=255)
                price = models.IntegerField()
                stock = models.IntegerField()
                description = models.TextField()
                category = models.TextField()
                            |
                            v
                Django Templates (HTML)
                            |
                            |
    5. Data dari view atau model di-passing ke template HTML untuk dirender
                            |
                            v
                        Response
                            |
                            |
    6. Django mengirimkan HTML yang telah dirender sebagai HTTP response
                            |
                            v
                    Client (Browser)
                            |
                            v
    7. Client menerima dan menampilkan hasil response

<h2>3. Kegunaan git dalam pengembangan perangkat lunak ialah </h2>
Dalam pengembangan perangkat lunak pasti terdapat berbagai aspek yang harus diperhatikan dan disimpan pengembangannya. Dalam hal ini, git membantu user untuk mengontrol versi dalam pengembangan kode dan mampu melacak perkembangannya. Git juga mampu mengkolaborasikan berbagai branch sebagai sarana multideveloper untuk memperbaiki bug atau memperbanyak fitur secara terpisah tanpa mengganggu kode utamanya. Salah satu fungsi terpenting git juga ialah untuk me reverse versi kode apabila terjadi kesalahan. Secara keseluruhan git mempermudah akses user ke dalam versi pengembangan perangkat lunak.

<h2>4. Mengapa django menjadi permulaan pengembangan perangkat lunak? </h2>
Hal ini berkaitan dengan konsep MVT. Konsep MVT ini sangat berkaitan dengan framework dari Django itu sendiri, framework Django berbasis pada model view dan template yang memberikan pengguna kesempatan untuk mengalokasikan model, memberikan view sesuai dengan request dan memberikan response sesuai dengan yang dibutuhkan user, dan juga template sebagai sarana antarmuka pengguna yang dapat dikosutmisasi. Pembagian tugas ini terpidah dan user dapat memberikan kendali yang lebih spesifik pada bagian tertentu sejalan dengan MVT.

<h2>5. Mengapa model pada django disebut dengan ORM?</h2>
ORM(Object Relational Mapping) merupakan konsep yang berfungsi untuk menghubungkan objek python dengan tabel yang ada dalam database. Dengan ORM, pengembang software mammpu mengeksekusi operasa secara langsung pada database tanpa menulis ataupun mengakses SQL. Implementasi model pada django juga mewakili setiap jenis atribut tabel di database seperti charfield, integerfield, dll yang dalam kata lain mampu mempermudah interaksi dengan database dan mendukung jenis jenisnya secara abstrak.

<h1>Tugas 3</h1>

<h2>1. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?</h2>
Data delivery diperlukan dalam pengimplementasian platform karena memungkinkan pertukaran informasi antara berbagai sistem atau komponen dalam arsitektur yang terdistribusi. Dengan data delivery, platform dapat mengirim dan menerima data secara efisien, baik antar server, klien, atau antar aplikasi. Hal ini sangat penting untuk memastikan integritas, efektivitas akses data. Tanpa adanya data delivery yang baik, mungkin aplikasi tidak mampu berfungsi dengan baik, terutama dalam hal real-time processing, dan sinkronisasi data.

<h2>2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?</h2>
Menurut saya, JSON lebih baik dari XML dalam lingkup keterbacaan. Meskipun kedua format ini mendukung penyampaian informasi yang baik, JSON dalam hal ini dapat lebih mudah dibaca dengan penggunaan "label" : value apabila dibandingkan dengan XML yang menggunakan field dan bahasa penyampaian yang lebih teknis. Secara langsung JSON juga mempercepat proses distribusi karena kesederhanaannya dan meningkatkan performa pada database besar.

<h2>3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?</h2>
Method isvalid yang digunakan pada fungsi di views merupakan cara bagaimana django memvalidasi format data yang dimasukan ke dalam form/model. Dengan menggunakan is_valid(), django akan mengecek apakah input user sesuai dengan type yang ditentukan dengan yang telah di define pada spesifikasi database model. Hal ini penting untuk diterapkan karena format yang salah pada input data akan mengganggu proses distribusi data dan berpotensi untuk memberikan threat lebih lanjut pada sistem yang tidak di inginkan.

Bentuknya seperti berikut:

```bash
    def create_show_form(request):
    form = SuiseiMainForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_att')
    
    context = {'form': form}
    return render(request, "create_show_form.html", context)
```

<h2>4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?</h2>

`% csrf_token %`

csrf_token merupakan token unik yang di generalize oleh Django untuk melindungi aplikasi dari CSRF attack (Cross Site Request Forgery). Serangan ini terjadi ketika penyerang membuat permintaan yang terlihat sah dari pengguna yang telah terautentikasi pada aplikasi, hal ini terjadi melalui pengiriman formulir atau permintaan POST tanpa sepengetahuan pengguna.

Jika kita tidak menambahkan csrf_token pada form Django, aplikasi kita akan rentan terhadap serangan ini. Penyerang dapat memanfaatkan sesi pengguna yang valid untuk menjalankan aksi yang tidak diinginkan, seperti mengubah data pengguna, melakukan pembelian tanpa izin, atau menghapus data.

<h2>5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</h2>
Saya mengimplementasikan checklist dengan menambahkan beberapa hal pada aplikasi saya. Pertama-tama saya membuat base.html untuk mempermudah setup html dan menambahkan block untuk template lanjutannya. Setelah melakukan hal tersebut saya membuat html untuk menyesuaikan pembuatan form dan mengatur tinggi serta lebar tabel agar lebih estetik. 

`{% block meta %} {% endblock meta %}`

```bash
    table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        td {
            padding: 12px;
            vertical-align: top;
        }
        td:first-child {
            text-align: right;
            font-weight: bold;
            width: 30%;
            padding-right: 20px;
        }
```

Setelah sedikit adjust pada templates, saya mulai membuat forms.py yang berisikan class yang berbasis pada model utama, saya mengintegrasikan fields sesuai dengan kebutuhan input user. Setelah ini, saya juga meng-update models.py dan menambahkan id pada setiap submisi data untuk mempermudah identifikasi data.
```bash
    class SuiseiMainForm(ModelForm):
        class Meta:
            model = ProductEntry
            fields = ["name", "price", "stock", "description", "category"]
```
Kemudian untuk melakukan routing, saya menambahkan fungsi membuat form baru pada views.py yang juga menerima request user dan mengembalikan Https Response berupa render sesuai dengan html dan urls yang sudah saya sesuaikan kembali.

Contoh return value:

`return render(request, "create_show_form.html", context)`

Terakhir saya menambahkan fungsi untuk menampilkan data dalam format JSON atau XML, baik dengan id atau tanpa id untuk menampilkan data.
```bash
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<str:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', views.show_json_by_id, name='show_json_by_id')
```

![WhatsApp Image 2024-09-18 at 10 05 14_615cda77](https://github.com/user-attachments/assets/428d18cd-588b-42b2-94b1-84598ae35120)

![WhatsApp Image 2024-09-18 at 10 05 40_c5a367b6](https://github.com/user-attachments/assets/39b0a52b-768e-41ad-892b-fc2a2d7e8ddc)

![WhatsApp Image 2024-09-18 at 10 06 06_241e3d2b](https://github.com/user-attachments/assets/d954d0fd-e5ac-4b91-8041-cba30cd352be)

![WhatsApp Image 2024-09-18 at 10 06 52_5c9e580d](https://github.com/user-attachments/assets/d400296c-6467-4120-9f13-daed54db5c17)


<h1>Tugas 4</h1>

<h2>1. Apa perbedaan antara `HttpResponseRedirect()` dan redirect()</h2>

```bash
    HttpResponseRedirect()
```
Ini merupakan kelas django yang secara manual bisa membuat response untuk melakukan pengalihan (redirect) ke URL lain.

Kelas ini dapat menerima satu parameter yaitu URL dengan contoh:
 ```bash
    HttpResponseRedirect('/sebuah-url/')
 ```

Sementara untuk `redirect()` merupakan shortcut django yang lebih sederhana untuk membuat redirect.

Fungsi ini lebih fleksibel dibandingkan dengan `HttpResponseRedirect` karena dapat menerima berbagai parameter fungsi, seperti URL nama fungsi view ataupun objek lain.

Pada akhirnya `redirect()` ini juga menggunakan `HttpResponseRedirect` di proses latar belakangnya, namun fleksibilitas ini yang memberikan perbedaan.

<h2>2. Jelaskan cara kerja penghubungan model Product dengan User</h2>

Dalam menghubungkan model product dan user pertama tama kita harus melihat `models.py`. Pada bagian models ini kita harus menyambungkan satu key ke beberapa product yang ada pada model.

```bash
    class ProductEntry(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        stock = models.IntegerField()
        description = models.TextField()
        category = models.TextField()
    
```


`ForeignKey(User, on_delete=models.CASCADE)` menghubungkan setiap produk ke satu user. Relasi ini membuat satu pengguna dapat memiliki banyak produk (one-to-many relationship).

Di sini parameter models.CASCADE memberikan korelasi kuat dengan data dan user, fungsi ini memastikan bahwa user dihapus produk yang terhubung dengan user tersebut juga terhapus.

Setelah inisiasi model ini dan migrate, model akan memiliki foreign key dari objek User yang mengepass id_unique user ke dalam model untuk mengidentifikasi user per submisi pada formnya

<h2>3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.</h2>

<h5>Authentication (Autentikasi):</h5>
Proses ini bertujuan untuk memverifikasi identitas pengguna. Dalam konteks ini (saat login), autentikasi terjadi saat pengguna memberikan data login/kredensial user (seperti username dan password) untuk membuktikan bahwa mereka adalah siapa yang mereka klaim. Jika kredensial tersebut valid, pengguna dianggap "terautentikasi" dan dapat melanjutkan ke sistem.

<h5>Authorization (Otorisasi):</h5>
Setelah pengguna terautentikasi, otorisasi menentukan apa yang diizinkan untuk dilakukan pengguna tersebut. Otorisasi terkait dengan perizinan (permissions), seperti akses ke halaman tertentu atau kemampuan untuk melakukan tindakan tertentu (misalnya mengedit atau menghapus data menggunakan request PATCH atau DELETE).

<h5>Proses Login:</h5>
Saat pengguna login, sistem pertama kali melakukan autentikasi untuk memastikan bahwa kredensial pengguna benar dan sah, apabila masih salah maka akan ada error dan pengguna tidak akan masuk. Setelah berhasil, sistem kemudian menggunakan otorisasi untuk memutuskan akses apa saja yang diberikan kepada pengguna tersebut berdasarkan peran (role) atau izin (permissions) yang telah ditetapkan pada aplikasi.

<h5>Implementasinya di Django:</h5>
Authentication: Django menyediakan modul autentikasi melalui django.`contrib.auth` . Django menggunakan middleware dan views khusus seperti LoginView untuk menangani proses login. Kredensial pengguna (username dan password) dicocokkan dengan data pengguna yang tersimpan dalam database. Pengguna yang terautentikasi kemudian disimpan dalam sesi (session), sehingga mereka tidak perlu login lagi dalam setiap permintaan (request).

Authorization: Django menggunakan sistem permissions yang terkait dengan pengguna atau grup pengguna. Setiap pengguna dapat memiliki peran tertentu (seperti admin, editor, atau pengguna biasa), dan otorisasi dilakukan melalui decorator seperti `@login_required` dan `@permission_required`. Selain itu, Django juga menyediakan kontrol akses berbasis grup (group-based permissions) untuk mengatur hak akses pada level lebih tinggi.

Contoh aplikasi :

```bash
    @login_required(login_url='/login')
    def show_att(request):
        item = ProductEntry.objects.filter(user=request.user)
        
        att = {
            'name': request.user.username,
            'nama_apk' : 'Suisei Shop',
            'nama' : "Christian Yudistira Hermawan",
            'kelas' : "PBP F",
            'item' : item,
            'last_login': request.COOKIES['last_login'],
        }
        return render(request, 'att.html', att)
```

Untuk fungsi di views ini dibutuhkan login untuk menggunakan show_att. Ketika url default memberikan path `path('', views.show_att, name = "show_att"),`, maka akan me redirect ke /login bagi pengguna yang belum login, namun apabila pengguna sudah login maka redirect ke login tidak terjadi.


<h2>4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?</h2>

Django mengingat pengguna yang telah login dengan menggunakan sesi (session) dan cookies. Ketika pengguna berhasil login, Django menciptakan sesi untuk pengguna tersebut dan menyimpan informasi sesi di server, sementara sebuah cookie untuk mencatat sesi (session cookie) disimpan di sisi klien (browser). Cookie ini berisi ID unik yang mengacu pada sesi di server. Jadi singkatnya cookie menjadi sebuah identifier yang dipass dari browser pengguna.

```bash
    @login_required(login_url='/login')
    def show_att(request):
        item = ProductEntry.objects.filter(user=request.user)
        
        att = {
            'name': request.user.username,
            'nama_apk' : 'Suisei Shop',
            'nama' : "Christian Yudistira Hermawan",
            'kelas' : "PBP F",
            'item' : item,
            'last_login': request.COOKIES['last_login'],
        }
        return render(request, 'att.html', att)
```

Di sini ada penggunaan `'last_login': request.COOKIES['last_login']` yang meretrieve atribut cookies (last login) yang telah diaplikasikan ke dalam function pada `views.py`


Sementara itu kegunaan lain dari cookies dapat dilihat berdasarkan definisinya sendiri, cookie adalah data kecil yang disimpan di browser pengguna. Data ini mampu memberikan informasi seperti:


- Menyimpan Preferensi Pengguna: Misalnya, bahasa yang dipilih atau mode tampilan (gelap/terang) di situs web.
- Pelacakan Pengguna (Tracking): Cookies bisa digunakan untuk melacak aktivitas pengguna di situs web, sering kali untuk tujuan analitik atau iklan.
- Keranjang Belanja (Shopping Cart): Dalam e-commerce, cookies bisa digunakan untuk menyimpan barang-barang yang ditambahkan pengguna ke keranjang belanja meskipun belum login.
- Token CSRF: Django juga menggunakan cookie untuk mengelola token CSRF (Cross-Site Request Forgery), guna melindungi dari serangan CSRF.

Cookies sendiri dibagi menjadi 2, yaitu cookies yang dikonsiderasi sebagai cookies aman dan tidak aman

Beberapa kriteria yang mungkin dikategorikan aman adalah sebagai berikut

<h4>Cookies Aman:</h4>

- Secure Flag: Jika cookie ditandai dengan Secure, cookie tersebut hanya akan dikirim melalui koneksi HTTPS yang terenkripsi, sehingga lebih aman dari penyadapan.
- HttpOnly Flag: Cookie dengan HttpOnly flag tidak dapat diakses oleh JavaScript, sehingga mencegah risiko serangan Cross-Site Scripting (XSS), di mana script jahat mencoba mencuri informasi dari cookies.
- SameSite Flag: Membatasi pengiriman cookies dalam konteks lintas situs, sehingga membantu mencegah serangan CSRF. Pengaturan ini memastikan cookies hanya dikirim dalam permintaan yang berasal dari domain yang sama.

<h4>Cookies Tidak Aman:</h4>

- Cookies Tanpa Enkripsi: Jika cookie dikirim melalui HTTP (bukan HTTPS), data cookie dapat disadap oleh pihak ketiga di jaringan (man-in-the-middle attack).
- Cookies Tanpa HttpOnly: Cookies yang dapat diakses oleh JavaScript rentan terhadap serangan XSS, di mana kode jahat dapat mencuri data dari cookies.
- Cookies dengan Data Sensitif: Cookies seharusnya tidak digunakan untuk menyimpan informasi sensitif seperti password atau data pribadi, karena cookies berada di sisi klien dan lebih mudah untuk disalahgunakan.

<h2>5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</h2>

Pada Tugas 4 ini terdapat beberapa modifikasi yang berarti bagi aplikasi ini. Aplikasi ini mendapatkan fitur untuk login, verivikasi login, penggunaan cookie dan penentuan foreign key yang mengatur hubungan user dan isi dari aplikasi.

Pertama - tama saya mencoba membuat model dengan mengintegrasikannya dengan user. Saya mengimport library ini

`from django.contrib.auth.models import User`

Library ini merupakan library autentikasi user yang merupakan bawaan dari django. Di sini saya menggunakan User sebagai foreign key pada model. Menurut teori basis data, foreign key merupakan primary key user (id) yang dipass ke dalam model dalam bentuk `user_id`. Karena id pada user merupakan primary key, maka user dapat dibedakan berdasarkan id tersebut atau dapat disebut user_id adalah unique value yang dipass ke dalam tabel pada model. Berikut merupakan implementasinya :

```bash
    from django.contrib.auth.models import User

    class ProductEntry(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        stock = models.IntegerField()
        description = models.TextField()
        category = models.TextField()
```

`on_delete=models.CASCADE` ini merupakan cara agara apabila sebuah user di delete dari database, maka data yang terhubung dengan id user tersebut akan ikut ter delete dari database.

Untuk mengintergrasikan user ini ke fungsi, pada show_att/fungsi utama di aplikasi ini ditambahkan filter by user

```bash
    @login_required(login_url='/login')
    def show_att(request):
        item = ProductEntry.objects.filter(user=request.user)
        
        att = {
            'name': request.user.username,
            'nama_apk' : 'Suisei Shop',
            'nama' : "Christian Yudistira Hermawan",
            'kelas' : "PBP F",
            'item' : item,
            'last_login': request.COOKIES['last_login'],
        }
        return render(request, 'att.html', att)
```

pada `item` disini diterapkan hasil product entry yang sudah di integrasikan menginput data ke model dengan form

```bash
    def create_show_form(request):
        form = SuiseiMainForm(request.POST or None)
        
        if form.is_valid() and request.method == "POST":
            item_entry = form.save(commit=False)
            item_entry.user = request.user
            item_entry.save()
            return redirect('main:show_att')
        
        context = {'form': form}
        return render(request, "create_show_form.html", context)
```
Di fungsi ini form akan dibuat dan selalu dicek apakah form ini sudah berbentuk POST atau apakah sudah valid. Apabila form belum memenuhi keduanya atau salah satu dari kedua kondisi itu, form akan di render dan akan di direct ke html yang akan menampilkan form kembali. Bentuknya ialah seperti berikut:

```bash
    <form method="POST">
            {% csrf_token %}
            <table>
                {{ form.as_table }}
                <tr>
                    <td colspan="2">
                        <input type="submit" value="Create Show Form" />
                    </td>
                </tr>
            </table>
    </form>
```

Apabila user mengklik tombol submit, maka form akan me direct ulang ke url yang sama (pada kasus ini ke url yang menuju create_show_form) dan fungsi akan mengecek data yang dikirim di parameter `request` pada fungsi dan kembali memeriksa form. Apabila submisi valid dan typenya sudah `POST` maka form akan dicoba disave

```bash
    item_entry = form.save(commit=False)
    item_entry.user = request.user
    item_entry.save()
    return redirect('main:show_att')
```
Di sini form akan melakukan temporary save `commit = False` lalu menginput user menjadi foreign keynya baru disave permanen ke database model. Setelah berhasil maka akan kembali redirect ke halaman utama yang sudah menampilkan data terbaru.

Terdapat perubahan juga pada fungsi `show_att` di dalam views.py. Terdapat pengunaan cookies di sini, penjelasan mengenai cookies sudah dijelaskan di nomor sebelumnya dan pengaplikasiannya adalah sebagai berikut :

```bash
    @login_required(login_url='/login')
    def show_att(request):
        item = ProductEntry.objects.filter(user=request.user)
        
        att = {
            'name': request.user.username,
            'nama_apk' : 'Suisei Shop',
            'nama' : "Christian Yudistira Hermawan",
            'kelas' : "PBP F",
            'item' : item,
            'last_login': request.COOKIES['last_login'],
        }
        return render(request, 'att.html', att)
```

Di sini last login merupakan pengunaan awal pada cookies yang selanjutnya akan digunakan pada fungsi `login` dan `register`

```bash
    <form method="POST" action="">
        {% csrf_token %}
        <label for="username">Username :</label>
        <input type="text" id="username" name="username" required>
        
        <label for="password">Password :</label>
        <input type="password" id="password" name="password" required>

        <input class="btn login_btn" type="submit" value="Login">
    </form>
```

Berikut merupakan penerapan post pada form login, html ini dikoneksikan ke fungsi berikut :

```bash
    def login_user(request):
    if request.method == 'POST':
        form = AuthenticationFor(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_att"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
```
Built in function `AuthenticationForm` membuat form khusus untuk login pada user sekaligus mengecek validitasnya. Apabila user belum meregistrasikan akun, maka user dapat membuat akun dari fungsi berikut

```bash
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
```
Samahalnya dengan auth `UserCreationForm` merupakan fungsi bawaan yang dapat meregistrasikan django ke user. Fungsi login dan register ter afiliasi dengan tabel/model user secara otomatis di database. Model ini berisika user_id, username dan password yang dimiliki user. Database inilah juga yang terkoneksi menjadi foreign key pada model utama kita.

Terakhir, ada fungsi baru untuk logout yang mampu meremore authenticated user yang ada pada request dan menghapus session user. Berikut merupakan implementasinya:

```bash
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
```

Fungsi `logout(request)` ini memberikan kemudahan user untuk logout dari akun yang digunakan dan mematikan sesi mereka saat itu. Seiringan dengan hal ini, sessionid yang sudah otomatis di save dan di inisiasi django pada cookies memberikan user keuntungan karena user tidak perlu repot login ke web lagi karena request selalu mendeteksi sessionid ini dan mengepass ke `@login_required(login_url='/login')` untuk mengecek sesi user.

<img width="552" alt="image" src="https://github.com/user-attachments/assets/9c19ce6e-8050-46f1-981a-49c07442ea40">
<img width="634" alt="image" src="https://github.com/user-attachments/assets/2b3cc9dc-f75a-4f5d-be72-bfe97061b99c">


<h1>Tugas 5</h1>

<h2>Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!</h2>

CSS Selector pada suatu element HTML memiliki beberapa aturan/urutan penerapan dalam selector tersebut, hal ini bertujuan untuk memberikan kemampuan elemen untuk memiliki spesifikasi khusus dan lebih mendetail.

Ada beberapa urutan CSS selector, berikut adalah urutanya : 

<h5>Inline styles (langsung pada elemen dengan atribut style) memiliki prioritas tertinggi.</h5>
<h5>ID selectors (#id) memiliki prioritas lebih tinggi daripada class, pseudo-class, atau attribute selectors.</h5>
<h5>Class selectors, pseudo-class selectors, dan attribute selectors memiliki prioritas lebih tinggi daripada element selectors.</h5>
<h5>Element selectors (misalnya, p, div) memiliki prioritas paling rendah.</h5>
<h5>Jika ada dua atau lebih selector dengan prioritas yang sama, maka aturan CSS yang muncul terakhir dalam urutan file yang akan digunakan.</h5>
<h5>!important dapat mengesampingkan semua aturan di atas, meskipun penggunaannya tidak direkomendasikan.</h5>

Dari contoh urutan ini kita dapat mengambil beberapa contoh

```bash
    #myDiv { color: red; } /* ID selector */
    .myClass { color: blue; } /* Class selector */
    div { color: green; } /* Element selector */

```

di sini karena id selector didahulukan, class dan element selector diabaikan dan warna teks akan menjadi warna merah.

<h2>Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!</h2>

Responsive design memungkinkan tampilan web menyesuaikan dengan ukuran layar perangkat yang berbeda, seperti desktop, tablet, atau smartphone. Ini penting karena pengguna mengakses web dari berbagai perangkat, sehingga pengalaman pengguna perlu optimal di semua ukuran layar, dengan adanya responsive design sebuah aplikasi menjadi mampu mengakomodasi lebih banyak user dan membuatnya lebih fleksibel.

Beberapa contoh aplikasi web yang sudah menerapkan responsive design adalah
- Google
- Twitter
- Facebook
- dll

Adapun beberapa aplikasi web yang masih belum menerapkan konsep ini
- MySpace
- Friendster
- https://demos.vlsm.org

<h2>Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!</h2>

Margin, border dan padding merupakan salah satu komponen penting dan dasar pada CSS. Implikasi dan penerapan ketiga hal ini sangatlah penting dalam dinamikalitas suatu aplikasi web agar tampilannya lebih menarik dan tertata sebagaimana mestinya. Berikut definisi dari ketiga hal tersebut.

- Margin: Ruang kosong di luar elemen, mendorong elemen lain di sekitarnya. Digunakan untuk memberi jarak antar elemen.
- Border: Garis yang mengelilingi elemen, berada di antara margin dan padding. Border dapat diatur dengan ketebalan, warna, dan jenis garis.
- Padding: Ruang kosong di dalam elemen, di antara konten elemen dan border-nya. Padding mengatur jarak antara konten dan tepi elemen.

Cara mengimplementasikan ketiga hal tersebut dapat dilakukan melalui 2 cara yaitu:
- Melalui Framework : Framework seperti tailwind memungkinkan pengguna untuk menerapkan inline adjustment pengguna dengan singkat menggunakan beberapa kode pendek, dan framework ini akan mentranslasikan kode tadi ke CSS asalnya

```bash
    <div class="p-4 m-2 border border-gray-400 rounded-lg">
```

- Manual menggunakan CSS : Melalui CSS manual, kita dapat mendefine ketiga style ini pada kolom style pada html webnya, kita juga dapat menerapkan CSS selector untuk mengatur elemen spesifik pada aplikasi web. Berikut merupakan contoh class selector yang menerapkan margin border dan padding.

```bash
    .box {
    margin: 10px; /* Jarak di luar elemen */
    border: 2px solid black; /* Garis tebal di sekeliling elemen */
    padding: 15px; /* Jarak di dalam elemen */
    }

```

[![0_QFVzwn5M81QunEUX](https://github.com/user-attachments/assets/a19fde27-9a2f-47ea-96a4-1f0f020d18e2)](https://github.com/Nadekoooo/SuiseiShop/issues/3#issue-2560670299)
Berikut merupakan visualisasinya


<h2>Jelaskan konsep flex box dan grid layout beserta kegunaannya!</h2>

Secara general Flexbox dan grid layout merupakan cara untuk mengatur tata letak dari suatu div ataupun section yang ingin diberikan styling khusus. Ada beberapa perbedaan definisi dan kegunaannya: 

- Flexbox: Digunakan untuk tata letak satu dimensi (horizontal atau vertikal). Flexbox mempermudah penataan elemen dalam satu baris atau kolom dengan distribusi ruang yang dinamis.

* Kegunaan: Ideal untuk menyusun elemen seperti navbar, card layout, atau item list yang perlu dirapikan secara horizontal atau vertikal.

```bash
    .container {
    display: flex;
    justify-content: space-between; /* Membagi elemen dengan jarak yang sama */
    }

```

- Grid Layout: Digunakan untuk tata letak dua dimensi (baris dan kolom). Grid memungkinkan pembagian area yang lebih kompleks dengan kontrol pada baris dan kolom.

* Kegunaan: Cocok untuk desain tata letak halaman yang kompleks seperti dashboard atau galeri foto.

```bash
    .grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* Membagi dalam 3 kolom */
    }

```
Grid sendiri disini menggunakan 1fr yang berarti membagi sisa halaman menjadi 1 bagian, grid ini secara spesifik mendefinisikan ukuran asli dari cakupannya, maka lebih cocok untuk desain yang fixed/tetap.

<h2>Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!</h2>

Untuk task pertama dalam menghapus dan mengedit produk, seperti biasa saya mengedit views.py sehingga terdapat fungsi yang mengakomodir kedua kebutuhan ini

```bash
    def edit_product(request, id):
    # Get mood entry berdasarkan id
    product = ProductEntry.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = SuiseiMainForm(request.POST or None, instance = product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_att'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

    def delete_product(request, id):
        # Get mood berdasarkan id
        product = ProductEntry.objects.get(pk = id)
        # Hapus mood
        product.delete()
        # Kembali ke halaman awal
        return HttpResponseRedirect(reverse('main:show_att'))
```

Kedua fungsi ini menerima id yang merupakan primary key dari objek untuk mengambil bagian spesifik/tuple data yang sesuai dengan kebutuhan edit/delesi.

Pada edit product saya memastikan bahwa fort edit itu valid dan melakukan re.save() pada produk yang sudah dalam tampilan form. Untuk delete saya mendelete instansi tersebut agar data hilang dari model/db kita.

Setelah menerapkan fungsi, saya akan membuat link pada urls.py agar pengguna dan operasi selanjutnya dipermudah melalui pemanggila redirect link.

```bash
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product')
```

Di sini saya menyeleksi id dari produk yang akan saya edit dan delete, pemanggil href pada html akan me redirect ke link di atas dan fungsi pada views.py bersangkutan akan berjalan.

Setelah itu, saya membuat instansi html agar seluruh pengaturan ini terhubung dan user dapat mengakses fitur baru ini.

Setelah itu, saya memberikan CSS related element seperti navbar, card info atau card product. Untuk navbar saya menggunakan CSS yang sudah diintegrasikan oleh penggunaan tailwind, namun untuk card info dan product saya langsung memasukannya di att.html dan langsung menggunakan tailwind untuk stylingnya. 

Pada navbar terdapat verifikasi user

```bash
    <div class="hidden md:flex items-center">
              {% if user.is_authenticated %}
              <span class="text-gray-300 mr-4">Welcome, {{ user.username }}</span>
              <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                  Logout
              </a>
              {% else %}
              <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">
                  Login
              </a>
              <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                  Register
              </a>
              {% endif %}
    </div>
```

verifikasi ini akan menentukan kemunculan tombol pada navbar, apabila sudah ada user, maka user akan diwelcome dan apabila belum akan diminta register (Untuk kasus sekarang masih belum bisa diakses karena redireksi show_att)

kemudian saya memberikan fleksibilitas untuk navbar pada tampilan mobile dengan beberapa syntax js

```bash
    <div class="mobile-menu hidden md:hidden px-4 w-full md:max-w-full">
        <div class="pt-2 pb-3 space-y-1 mx-auto">
            <a href="{% url 'main:show_att' %}" class="block text-white hover:bg-blue-700 px-3 py-2 rounded-md">Home</a>
            <a href="{% url 'main:show_att' %}" class="block text-white hover:bg-blue-700 px-3 py-2 rounded-md">Products</a>
            <a href="{% url 'main:show_att' %}" class="block text-white hover:bg-blue-700 px-3 py-2 rounded-md">Categories</a>
            <a href="{% url 'main:show_att' %}" class="block text-white hover:bg-blue-700 px-3 py-2 rounded-md">Cart</a>
            {% if user.is_authenticated %}
            <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
            <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                Logout
            </a>
            {% else %}
            <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
                Login
            </a>
            <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                Register
            </a>
            {% endif %}
        </div>
    </div>
    <script>
        const btn = document.querySelector("button.mobile-menu-button");
        const menu = document.querySelector(".mobile-menu");

        btn.addEventListener("click", () => {
            menu.classList.toggle("hidden");
        });
    </script>
```

Karena fleksibilitas dan responsive design penting, saya mencoba menambahkan beberapa adjustment pada aplikasi seperti 

`<h1 class="text-3xl sm:text-[60px] md:text-[80px] lg:text-[120px] font-bold text-white">Suisei Shop</h1>`

Saya meng-adjust ini dengan tailwind dan memberikan default text sebesar 3xl dan berbagai kasus ukurang layar.

Sisa html lain dapat diliat pada file commit dan html tambahan yang saya buat kebanyakan menggunakan tailwind untuk CSSnya dan beberapa adjustment baru dibanding tugas sebelumnya.


<h1>Tugas 6</h1>

<h2> Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!</h2>

JavaScript merupakan bahasa pemrograman dinamis yang memang sangat berkorelasi dengna pengembangan web, hal ini dikarenakan kepraktisan dalam penggunaannya dan disisi lain adanya kompatibilas yang tidak dimiliki oleh platform atau bahasa pemrograman lainnya.
Beberapa poin penting yang merupakan manfaat dari penggunaan javascript ialah:

- Interaktif dan Dinamis: JavaScript memungkinkan pembuatan elemen interaktif seperti tombol, form, dan animasi tanpa memuat ulang halaman.
- Kemampuan validasi Data di Sisi Klien: Memungkinkan validasi data sebelum dikirim ke server, sehingga mengurangi beban server dan meningkatkan efisiensi.
- Manipulasi DOM: Mempermudah pengubahan elemen HTML dan CSS secara langsung untuk memperbarui tampilan tanpa reload halaman.
- Komunikasi Asinkron (AJAX): Mengizinkan pengambilan data dari server di latar belakang tanpa menyegarkan halaman, meningkatkan pengalaman pengguna.
- Cross-Platform: JavaScript berjalan di semua browser modern dan kompatibel di berbagai perangkat.
- Full-stack Development: Dengan Node.js, JavaScript dapat digunakan di sisi server, memungkinkan pengembangan aplikasi full-stack.
- Real-Time Application: Mendukung pengembangan aplikasi real-time seperti chat dan game online.

Dan masih banyak lagi, pada kasus tugas ini kita sudah menggunakan javascript dalam penggunaan AJAX juga untuk mengatur dinamisme web yang ada.

```bash
function addProductEntry() {
    fetch("{% url 'main:add_product_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#productEntryForm')),
    })
    .then(response => {
        refreshProductEntries();
        // Delay closing the modal to ensure the refresh is done first
        setTimeout(() => {
            hideModal();
        }, 100); // Adjust the timeout if necessary
    });

    document.getElementById("productEntryForm").reset(); 
    document.querySelector("[data-modal-toggle='crudModal']").click();

    return false;
  }
```

Ini adalah salah satu contoh bagaian kegunaan javascript dalam relasi asynchronous web dan mengatur beberapa komponen dinamis dalam add ajax

<h2>Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?</h2>

Sebagaimana dijelaskan pada tutorial mengenai AJAX, fungsi await pada fetch merupakan fungsi yang penting keberadaannya dalam fetch.
Fungsi dari penggunaan await ini ialah agar program mampu menunggu hingga peroses asingkronus selesai terlebih dahulu sebelum dilanjutkan ke kode selanjutnya.
Dengan fungsi `await` ini javascript akan "memberikan masa tunggu" pada kode yang menggunakan `await` sampai kode tersebut selesai.

Salah satu contohnya ialah ini
```bash
    let response = await fetch(url); // Menunggu fetch selesai
    console.log(response); // Akan menampilkan data dari response jika fetch berhasil
```

Di kode ini console log akan menunggu fungsi fetch url sampai selesai terlebih dahulu sebelum memprint valuenya di console.

Apabila `await` tidak digunakan, maka `fetch()` tetap berjalan secara asynchronous, tetapi kode di bawahnya akan langsung dieksekusi tanpa menunggu hasil dari fetch(). Ini bisa menyebabkan masalah, karena data yang diharapkan dari fetch() mungkin belum tersedia saat kita mencoba mengaksesnya.


<h2> Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?</h2>

Kita perlu menggunakan decorator `@csrf_exempt` pada view yang akan digunakan untuk AJAX POST karena Django, secara default, memerlukan token CSRF (Cross-Site Request Forgery) untuk setiap permintaan POST sebagai langkah keamanan untuk mencegah serangan CSRF.

Penggunaan `@csrf_exempt` disini ialah agar Django tidak perlu mengecek keberadaan token pada `POST` request yang dikirimkan ke sebuah fungsi demi menghindari waktu tunggu yang tidak perlu.
Hal ini sebenarnya didukung oleh bagaimana implementasi struktur form dan verifikasi user yang sudah ada. Karena pada kasus tugas ini, form, user dan login activity sudah diverifikasi oleh `{% csrf_token %}` maka tidak perlu melakukan pengecekan csrf lagi di sini.

Implementasi pada fungsinya sendiri dapat dilihat di bagian kode

```bash
    def create_ajax(request):
        
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    stock = strip_tags(request.POST.get("stock"))
    description = strip_tags(request.POST.get("description"))
    category = strip_tags(request.POST.get("category"))
    user = request.user

    new_item = ProductEntry(
        name = name, price = price, stock = stock, description = description, category = category,
        user=user
    )
    new_item.save()

    return HttpResponse(b"CREATED", status=201)
```

Di sini fungsi tidak perlu lagi menerima csrf karena input user sudah dipastikan sebelumnya.

<h2>Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?</h2>

Pada tugas kali ini, pembersihan data dilakukan dari sisi frontend dan juga backend. 
Pembersihan data dilakukan pada backend di fungsi berikut 

```bash
    def clean_name(self):
    return strip_tags(self.cleaned_data["name"])

    def clean_price(self):
    return strip_tags(self.cleaned_data["price"])

    def clean_stock(self):
    return strip_tags(self.cleaned_data["stock"])

    def clean_description(self):
    return strip_tags(self.cleaned_data["description"])

    def clean_category(self):
    return strip_tags(self.cleaned_data["category"])
```

Dan pembersihannya di frontend ada pada att.html di project ini

```bash
    const name = DOMPurify.sanitize(item.fields.name);
    const price = DOMPurify.sanitize(item.fields.price);
    const stock = DOMPurify.sanitize(item.fields.stock);
    const description = DOMPurify.sanitize(item.fields.description);
    const category = DOMPurify.sanitize(item.fields.category);
```

Mengapa perlu pembersihan 2 kali? Hal ini berhubungan dengan konteks interaksi frontend dan backend.
Frontend sebagaimana namanya, bagian ini berinteraksi langsung dengan pengguna pada UI dan hal lainnya, sementara backend bekerja di latas belakang tanpa adanya interaksi dengan pengguna.

Faktor utamanya ialah keamanan, pengguna dapat mengubah kode JavaScript di frontend, yang berarti mereka dapat melewati atau menonaktifkan pembersihan data. Dengan pembersihan di backend, hal ini memastikan bahwa semua data yang masuk ke sistem telah diperiksa dan diolah dengan benar.
Faktor lainnya ialah konsistensi, pada backend, data yang masuk dari sumber manapun akan selalu tersaring dan dibersihkan dengan cara yang sama darimanapun asal datanya.
Berhubungan dengan konsistensi juga backend juga cenderung lebih mudah dimodifikasi mengingat perubahan akan banyak terjadi pada sisi frontend sehingga mempermudah developer.


<h2>Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!</h2>

Pada tugas kali ini inisialisasi AJAX ialah tujuan utama, jadi saya menerapkan beberapa perubahan pada `att.html` yang memberikan fungsi asynchronus dalam operasinya.

```bash
    function hideModal() {
    function showModal() {
    async function refreshProductEntries() {
    function addProductEntry() {
    async function getProductEntries(){
```

berikut ialah beberapa fungsi yang diimplementasikan dalam penggunaan javascript disini.

Pertama tama, saya menginisiasi error message pada views.py tepatnya padafungsi login

`messages.error(request, "Invalid username or password. Please try again.")`

Ini ialah bentuk error yang di return ketika ada form yang tidak valid

Kemudian saya menambahakn fitur pada views.py di sini saya menggunakan `@csrf_exempt` dan `@require_post` agar django mengabaikan csrf dan hanya menerima request post

```bash
    @csrf_exempt
    @require_POST
    def create_ajax(request):
        
        name = strip_tags(request.POST.get("name"))
        price = strip_tags(request.POST.get("price"))
        stock = strip_tags(request.POST.get("stock"))
        description = strip_tags(request.POST.get("description"))
        category = strip_tags(request.POST.get("category"))
        user = request.user
        
        new_item = ProductEntry(
            name = name, price = price, stock = stock, description = description, category = category,
            user=user
        )
        new_item.save()

        return HttpResponse(b"CREATED", status=201)
```

berikut merupakan penerapannya, sebagaimana dijelaskan decorator `csrf_exempt` membuat django tidak men double check csrf.

seperti biasa, kemudian saya juga memberikan direct url dari urls.py namanya

`path('create-ajax', create_ajax, name='create_ajax')`

Hal ini bertujuan agar url pattern terdeteksi oleh django.

Setelah memberikan beberapa adjustment pada views.py (beberapa entry diedit dan difilted), saya mereplace for loop pada `att.html` menjadi div yang nantinya akan diintegrasikan dengan js.

`async function getProductEntries(){` fungsi ini dibuat dan beberapa penyesuaian dibuat di sini.

`async function refreshProcutEntries()` juga saya buat dan dikhususkan pada amodel yang memberikan fungsi refresh agar selalu asynchronous.

Kemudian saya juga menambahkan beberapa adisi di templates atas, saya membuat model crud agar inputasi lebih mudah dilakukan pengguna.

```bash
<div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
    <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
      <!-- Modal header -->
      <div class="flex items-center justify-between p-4 border-b rounded-t">
        <h3 class="text-xl font-semibold text-gray-900">
          Add New Product Entry
        </h3>
        <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
          <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
          </svg>
          <span class="sr-only">Close modal</span>
        </button>
      </div>
      <!-- Modal body -->
      <div class="px-6 py-4 space-y-6 form-style">
    .....
```

Berikut potongan dari kodenya. 

Kemudian dengan menggunakan fungsi javascript saya juga me link button yang telah di buat di `att.html` agar me redirect ke fungsi `showModal()`

```bash
const modal = document.getElementById('crudModal');
  const modalContent = document.getElementById('crudModalContent');

  function showModal() {
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');

      modal.classList.remove('hidden'); 
      setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
      }, 50); 
  }

  function hideModal() {
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');

      modalContent.classList.remove('opacity-100', 'scale-100');
      modalContent.classList.add('opacity-0', 'scale-95');

      setTimeout(() => {
        modal.classList.add('hidden');
      }, 150); 
  }

  document.getElementById("cancelButton").addEventListener("click", hideModal);
  document.getElementById("closeModalBtn").addEventListener("click", hideModal);
```

Terkahir saya memberikan addProductEntry untuk menambahkan produk dan men save langsung ke tampilan utama.

```bash
function addProductEntry() {
    fetch("{% url 'main:create_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#productEntryForm')),
    })
    .then(response => {
        refreshProductEntries();
        
        setTimeout(() => {
            hideModal();
        }, 100); 
    });

    document.getElementById("productEntryForm").reset(); 
    document.querySelector("[data-modal-toggle='crudModal']").click();

    return false;
  }
```

Disini saya meng set timeout agar form tertutup otomatis dan lebih fleksibel.


Terakhir saya menambahkan fungsi keamanan yang memotong data yang sekiranya membahayakan website.
Hal ini saya implementasikan menggunakan `strip_tags` dan `DOMPurify, kedua fungsi ini di import dan di implementasikan di att.html dan forms.py.

