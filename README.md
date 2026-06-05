# Pencak Silat:Hokya

Pencak Silat : Hokya adalah sebuah game 2D Action-Platformer bertema ninja modern yang menggabungkan kelincahan seni bela diri tradisional dengan pertempuran senjata api taktis. Pemain akan mengendalikan seorang pesilat tangguh yang dibekali kemampuan bergerak cepat untuk menembus barikade musuh di berbagai level yang menantang.
Game ini menonjolkan atmosfer visual yang estetis melalui penggunaan sistem siluet peta yang dinamis, pergerakan awan, dan partikel daun berguguran yang interaktif. Fokus utama dari gameplay ini adalah memberikan sensasi bermain yang bertenaga (juicy gameplay) melalui efek getaran layar (screenshake) dan cipratan percikan api (sparks particle) setiap kali terjadi pertempuran sengit.

Kelompok 9:
1. Rihhadatul Aisyikin Mardhiyyah (25051204042)
2. Azizah Fairuz Dzakiyya (25051204137)
3. Rivana Adinda Putri (25051204185)
4. Shinta Nur Rahma (25051204136)

Fitur Utama
1. Advanced Ninja Movement (Mekanik Pergerakan Ninja)
Karakter utama memiliki kontrol pergerakan yang sangat responsif, meliputi kemampuan berlari (running), melompat (jumping), meluncur kebal (dashing/sliding), serta merayap di dinding (wall-sliding).
2. Smart Auto-Tiling System
Sistem pemetaan dunia berbasis grid (16x16 piksel) yang secara otomatis dapat mendeteksi dan merapikan tepian tekstur tanah atau batu berdasarkan ubin (tile) tetangganya, memastikan desain level terlihat organik dan rapi.
3. Built-in Level Editor (Alat Desain Level internal)
Game dilengkapi dengan program Editor khusus untuk memudahkan developer merancang, mengedit, menghapus, menaruh titik spawn karakter/musuh, dan menyimpan cetak biru peta langsung ke dalam file penyimpanan secara visual (on-grid maupun off-grid).
4. Juicy Combat & Visual Effects
Pertempuran yang terasa dinamis dengan adanya partikel peluru proyektil, puluhan sistem partikel percikan berlian (Spark) saat peluru menghantam dinding/karakter, serta efek getar layar (screenshake) yang adaptif.
5. Smooth Camera Tracking & Layering Render
Kamera game bergerak secara halus menggunakan efek redaman (easing damping) mengikuti posisi pemain. Visual game juga dioptimalkan menggunakan teknik Frustum Culling (hanya menggambar objek yang terlihat di layar) serta sistem layering masking untuk menciptakan efek bayangan siluet pada peta.
6. Dynamic Level Progression
Game mendukung transisi antar-level otomatis menggunakan efek lingkaran (circular transition) yang akan memuat map berbeda setiap kali pemain berhasil menyapu bersih seluruh musuh di area tersebut.

Cara menjalankan project (langkah menjalankan)
1. Mulai Level 
2. Hancurkan Semua Enemy dengan Dash (X)
Jalan & Lompat Menuju Ubin Spawners/Portal 
Kamu tidak bisa langsung masuk portal begitu saja. Kamu harus memanfaatkan kelincahan gerakan untuk menghindari tembakan senapan musuh, lalu menabrak mereka dengan Dash sampai daftar musuh di map kosong (len(enemies) == 0). 
3. Level Terbuka 
4. Hitbox Player Menyentuh Portal 
Setelah area map aman dan bersih dari musuh, kamu tinggal menggerakkan karakter berjalan atau melompat menuju koordinat ubin spawners (Portal) yang sudah kamu letakkan di ujung peta saat mendesainnya di Level Editor. 
5. Pindah ke File map.json Berikutnya 
Begitu kotak fisik karaktermu menabrak kotak portal tersebut, program game akan langsung menutup map saat ini, membaca file data JSON berikutnya, dan kamu pun masuk ke tantangan baru.

Penerapan Pilar Utama PBO
1. Class dan Object (Kelas dan Objek)
Class adalah cetak biru (blueprint) atau kerangka kerja, sedangkan Object adalah wujud nyata yang dibuat berdasarkan blueprint tersebut.

a. Class
class Game:
class Editor:
class Cloud:
class Clouds:
class PhysicsEntity:
class Enemy(PhysicsEntity):
class Player(PhysicsEntity):
class Particle:
class Spark:
class Tilemap:
class Animation:

b. Object
Game().run()
Editor().run()

2. Inheritance (Pewarisan) 
Sebuah kelas anak (subclass) dapat mewarisi seluruh properti (atribut) dan perilaku (method) dari kelas induk (superclass). Ini mencegah penulisan kode yang berulang (code redundancy). 
a. Superclass
PhysicsEntity yang menampung semua logika umum fisika (posisi, ukuran, kecepatan, gravitasi, dan deteksi tabrakan ubin). 
b. Subclass
Player dan Enemy mewarisi kemampuan PhysicsEntity
class Enemy(PhysicsEntity):
   #konstruktor
   def __init__(self, game, pos, size):
       super().__init__(game, 'enemy', pos, size)

class Player(PhysicsEntity):
   #konstruktor
   def __init__(self, game, pos, size):
       super().__init__(game, 'player', pos, size)

3. Polymorphism (Polimorfisme) 
Konsep di mana beberapa kelas memiliki method dengan nama yang sama, tetapi cara kerja atau perilakunya berbeda (Overriding). 
Baik kelas PhysicsEntity, Player, maupun Enemy sama-sama memiliki method def update() dan def render().
Ketika game memanggil player.update(), yang diproses adalah input keyboard dan mekanik dash. Namun, ketika game memanggil enemy.update(), yang berjalan adalah AI patroli mendeteksi jurang dan logika menembak.
Mereka tetap memanfaatkan kode induknya dengan memanggil super().update(), lalu menimpanya (override) dengan logika unik masing-masing di bawahnya.

4. Encapsulation (Pengkapsulan) 
Membungkus data (atribut) dan fungsi (method) menjadi satu kesatuan unit di dalam kelas, serta menyembunyikan detail proses internal dari luar. 
Seluruh status pemain (seperti self.air_time, self.jumps, self.dashing) dikapsulkan di dalam class Player. 
Dunia luar atau kelas lain tidak boleh mengubah koordinat posisi pemain secara sembarangan. Jika ingin menggerakkan pemain, kelas lain harus berinteraksi lewat method yang sudah disediakan, yaitu update(tilemap, movement).

5. Abstraction (Abstraksi)
a. Abstraksi Pengelolaan Peta (Tilemap) 
Detail yang disembunyikan: Logika pembacaan file cetak biru berbasis json (data/maps/), algoritma ekstraksi koordinat ubin solid, pembatasan dinding pembatas, serta kalkulasi viewport kamera saat proses rendering dunia game.

self.tilemap.load('data/maps/' + str(map_id) + '.json')
self.tilemap.render(self.display, offset=render_scroll)

Kelas Game cukup memanggil perintah sederhana berikut untuk merakit dan menampilkan seluruh isi peta.
b. Abstraksi Objek dan Entitas (Player & Enemy) 
Detail yang disembunyikan: Kalkulasi vektor fisika seperti gaya gravitasi, waktu melayang di udara, akselerasi kecepatan lari, penanganan hitbox deteksi tabrakan, serta patroli musuh. 

self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
enemy.update(self.tilemap, (0, 0))

Di dalam Game Loop, pusat kendali cukup memicu pergerakan karakter menggunakan satu baris perintah eksekusi tanpa perlu tahu bagaimana otot internal karakter bekerja. 
c. Abstraksi Latar Belakang dan Lingkungan (Clouds) 
Detail yang disembunyikan: Rumus matematika efek gerak semu latar belakang, pengacakan properti visual menggunakan modul random, serta rumus sisa bagi atau modulo (%) untuk melakukan manipulasi teleportasi koordinat gambar agar awan tidak habis.

self.clouds.update()
self.clouds.render(self.display_2, offset=render_scroll)

Kelas Clouds menyembunyikan semua kerumitan tersebut sehingga Game Loop cukup memanggil perintah pembaruan visual secara instan
d. Abstraksi Modul Utilitas (Animation & Gambar)   
Detail yang Disembunyikan: Manipulasi sistem operasi untuk membaca file system laptop, proses penghapusan latar warna hitam menjadi transparan (set_colorkey), serta pembagian indeks waktu internal (stopwatch frame) untuk menahan pergantian gambar agar animasi berjalan halus. 

'player/run': Animation(load_images('entities/player/run'), img_dur=4),

Objek luar tinggal mendaftarkan alamat folder dan memanggil fungsi pembungkus yang telah disediakan.


<img width="960" height="766" alt="Screenshot 2026-06-04 231244" src="https://github.com/user-attachments/assets/22980b04-70d5-4808-9d13-42b23164d6d9" />
Gambar Level 0

<img width="962" height="762" alt="Screenshot 2026-06-04 231329" src="https://github.com/user-attachments/assets/70d4f2bd-f67b-406f-bf2f-27a6fa2d1f01" />
Gambar Level 1

<img width="967" height="760" alt="Screenshot 2026-06-04 231634" src="https://github.com/user-attachments/assets/3916261c-3053-4328-9177-676f12c969a8" />
Gambar Level 2

<img width="959" height="770" alt="Screenshot 2026-06-04 231932" src="https://github.com/user-attachments/assets/ac5e200d-b27b-441d-a35b-93f1fe89b07e" />
Gambar Menang
