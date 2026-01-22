# JAWABAN SOAL B
## Ivan, 16525136

### Jawaban Soal Daspro
1. Pemograman Berorientasi Objek
    - Penjelasan konsep dasar
        - Class: Merupakan dasar untuk tiap kali merancang object, di dalam class, didefiniskan data dan sebuah pemrosesan atau fungsi dari data-data tersebut
        - Object: Hasil nyata dari sebuah class, fungsi yang dirancang didalam class akhirnya dijalankan pada suatu object
        - Abstraction: Berufngsi untuk menutup detail kompleks dan hanya menampilkan hal yang penting untuk pengguna, sehingga pengguna tahu apa yang dilakukan, bukan caranya
        - Encapsulation: Penggabungan data dan/atau fungsi dalam suatu class serta membatasi akses terhadap data tersebut
        - Inheritance: Memungkinkan suatu class anak untuk mewarisi atribut dan _method_ dari class induk. Berguna untuk desain sistem yang lebih rapih dan mudah menambah fitur
        - Polymorphism: Karakteristik dalam fungsi yang mengakibatkan objek yang berbeda untuk merespons fungsi yang sama dengan cara yang berbeda. 
2. Bahasa C++
    - #include <file_name> dan #include "file name", keduanya digunakna untuk menyertakan isi file lain ke dalam file sumber. Perbedaannya adalah penggunaan <file_name> akan mengakibatkan sistem untuk mencari di _file system directories_ sementara penggunaan tanda petik "file_name" mengakibatkan sistem untuk mencari di direktori lokal terlebih dahulu, lalu sistem
    - Penggunaan #ifdef, #ifndef, #endif dan #pragma once dalam header file: Menentukan subprogram atau blok kode mana yang dijalankna berdasarkan tipe header yang telah terdefinisi. Contoh : #ifdef Header_Ex, apabila Header_Ex terdefinisi maka blok kode di antara #ifdef dan #endif akan terjalani, apabil abelum terdefinisi, maka blok kode di antara #ifndef dan #endif akn terjalani
    - Penggunaan namespace dan scope resolution operator (::)

        Namespace digunakan untuk mengelompokkan nama agar tidak terjadi konflik, semnetara :: digunakan untuk mengakses anggota namespace ataupun class

    - Perbedaan #define dan using: #define merupakan direktif untuk mengarahkan preprocessor untuk mengganti semua kemunculan makro (objek, fungsi) dengan token pengganti yang sudah ditentukan, sementara using merupakan kata kunci untuk membawa anggota namespace ke dalam scope program tanpa harus menuliskan kembali scope resolution operator yang bergantung pada using yang telah terdefinisikan
    - Cara kerja pointer (*) dan address of (&): Pointer merupakan operator untuk menyimpan memori address dari variabel yang setipe, sementara address of akan mengembalikan nilai dari lokasi dalam memori dimana variabel tersebut tersimpan\
    - Konsep pass by value dan pass by reference dalam definisi variabel dan fungsi: pass by value akan membuat kopi dari fungsi atau variabel sehingga definisi variabel awal tidak akan berubah saat dalam fungsi, sementara pass by reference akan membuat ikatan langsung dengan variabel awal, sehingga dapat dirubah-rubah dalam fungsi
    - Perbedaan std::unique_ptr dan std::shared_ptr: std::unique_ptr memiliki kepemilikan tunggal terhadap objeknya, sehingga responsi tinggi dan prosesnya cepat, namun tidak dapat menambah pemilik, hany adapat ditransfer melalui unique_ptr lainnya. std::shared_ptr memiliki kepemilikan yang lebih banyak sehingga lebih dari satu shared_ptr dapat menuju sebuah objek yang sama 


3. Multithreading
    - Multithreading merupakan model dalam pemrograman untuk menjalankan 2 subprogram atau _thread_ secara bersamaan tanpa mengganggu satu sama lain
    - Tampilan layar terminal:
    ![alt text](<../lampiran/Screenshot 2026-01-20 182147.png>)
    _source code_ berada dalam folder "src" dengan nama "MultiThreading.py"

4. Header

### Jawaban Soal Firmware
1. Firmware
    
    a. _firmware_ merupakan sebuah perangkat lunak yang tertanam secara permanen pada perangkat keras untuk menjalankan operasi dasar. Secara umum, _firmware_ hanya mengandung instruksi sederhana dan berperan sebagai jembatan antara perangkat keras (_hardware_) dan perangkat lunak (_software_), perbedaan _firmware_ dengan perangkat lunak pada umumnnya adalah _firmware_ didesain agar pernawgkat keras dapat menjalankan fungsi utamanya, seperti memori dan juga _booting_ sementara, perangkat lunak pada umumnya didesain untuk berinteraksi langsung dengan pengguna, sehingga mengutamakan fleksibilitas dan mudah unutk menambah fitur ataupun perbaikan. Peran _firmware_ pada UAV terdiri atas berbagai aspek. Dari segi kontrol, _firmware_ menerjemahkan input dari pilot, dari segi sensor, _firmware_ juga berperan dalam membaca data sensor, dan menggunakannya untuk navigasi.
    
    b. RTOS adalah OS terkhusus untuk sistem yang memiliki karakteristik _time sensitive_, RTOS memprioritaskan efek jeda yang singkat, manajemen data yang efisien, dan memiliki sistem prioirtas untuk tiap kerjaan yang dilakukan

    c. Protokol Komunikasi Serial
    - UART: Universal Asynchronus Reciever Transmitter atau UART Merupakan sirkuit fisik dalam mikrokontroller antara 2 _device_ UART yang mengirim data secara langsung. Tipe data yang dikirim berupa paket, dimana paket tersebut memiliki _start bit_, _parity bit_, dan _end bit_. Ketiga kommponen ini berguna unutk mengetahui kapan data memulai dan berakhir, dan memastikan integritas dari data yang terkirim. UART merupakan protokol yang beroperasi tanpa clock sehingga _baud rates_ dari kedua _device_ UART harus mirip ataupun sama untuk meminimalisir kehilangan data
    - SPI: Serial Peripheral Interface atau SPI merupakan protokol komunikasi antara _device_ yang memiliki hubungan _master-slave_ yang menggunakan 4 kabel yaitu CS, SCLK, MISO, dan MOSI. CS (Chip Select) mengatur interkoneksi antara _device slave_ dan _master_ yang berfungsi untuk _master_ memilih mau berkomunikasi dengan _slave device_ yang mana. SCLK berfungsi untuk _master device_ mengirimkan _clock_ yang diatur sehingga _slave device_ tidak memerlukan _clock_ mereka sendiri. _Clock_ mengindikasikan kapan data akan ter-_sampled_. MOSI (Master Out Slave In) merupakan sarana untuk _master device_ mengirimkan data kepada _slave device_. MISO (Master In Slave Out) merupakan sarana untuk _slave device_ mengirimkan data kepada _master device_. Apabila _slave device_ melebihi satu, terdapat 2 rangkaian umum yang digunakan, yang pertama adalah _independent slaves_ dan yang kedua adalah _cooperative slaves_ atau _daisy chain_. 
    - I2C: Inter-integrated Circuit atau I2C merupakan protokol komunikasi antara _device_ yang memiliki hubungan _master-slave_ yang menggunakan 2 kabel yaitu SDA dan SCL. Pengiriman data menggunakan I2C memiliki template atau _frame_ yang terkhusus melalui kedua kabel ini. Dimulai dari _master devvice_ mengambil alih bus dengan memicu sebuah _start condition_ lalu _master device_ akan mengirim sebuah _slave address_ untuk memilih _slave device_ apa yang akan dituju, lalu _master device- memilih untuk antara _read_ dari _slave device_ atau _write_ data dari _slave device_. Setelah itu, _slave device_ akan _acknowledge_ keberadaan dari _master device_ lalu pengiriman data dimulai lalu di-_acknowledge_ setelah itu _master device_ akan mengirim sebuah _stop condition_ untuk menandakan bahwa pengiriman data selesai.
### Jawaban Soal ConCept
1. ROS
    - Nodes : Program yang berjalan di dalam suatu sistem ROS, tiap node memiliki kodingan sendiri dan bertujuan untuk satu proses atau satu tugas spesifik
    - Topic : Jalur komunikasi data satu arah antar node menggunakan publisher-subscriber, dimana publisher akan mengirim data dan subscriber akan menerima data
    - Services : Jalur komunikasi dua arah antar node atau sering disebut sebagai _request-response_
    - Parameter : Merupakan nilai konfigurasi yang dapat diakses suatu node, atau sebagai variabel global konfigurasi
    - Actions : Mekanisme komunikasi dalam ROS, yang memakan waktu yang lama, membutuhkan _progress-feedback_, dan bisa di-_cancel_. Actions memiliki struktur umum: goal, feedback, result, dengan goal merupakan perintah awal dari mekanisme, feedback menyediakan _progress report_ yang berkala, dan result merupakan hasil akhir  
    - Analogi: Misal sebuah node adalah rumah dan nodes adalah rumah-rumah, topic merupakan surat dari rumah ketua RT yang merupakan _publisher_ dengan rumah di RT yang sama yang merupakan _subscriber_. Lalu, _services_ adalah jalur telepon yang memungkinkan tiap rumah untuk saling berkomunikasi, dan _parameter_ merupakan aturan-aturan dalam RT yang dapat diubah secara berkala. Lalu, _Actions_ adalah acara yang dilakukan oleh RT dimana setiap rumah atau _node_ saling bekerja sama
2. Publisher & Subscriber: Terlampir dalam src
3. Service & Client
4. Pinhole Camera Model
    - Sebuah model matematis yang menunjukkan hubungan antara koordinat tiga-dimensi dengan projeksinya terhadap suatu layar 2 dimensi mellaui sebuah lubang kecil atau _pinhole_, diagram:
    ![alt text](<../lampiran/WhatsApp Image 2026-01-22 at 18.55.35.jpeg>)
    - Homogenous Coordinates dan rigid transformations
        - Homogenous Coordinates merupakan penambahan satu dimensi ekstra agar translasi bisa direpresentasikan melalui perkalian, karena bilamana translasi direpresentasikan sebagai penambahan, akan rumit bagi sistem apabila ingin menggabungkan banyak transformasi
        - Rigid Transformations merupakan transformasi yang tidak mengubah bentuk ataupun ukuran dari sistem awal, rigid transformations terdiri dari translasi dan rotasi.
    - Parameter Kamera:
        - Intrinsik: Merupakan karakteristik internal dari suatu kamera, mencakup hal-hal seperti _focal length_ atau jarak fokus, _principal point_ atau titik utama kamera, _pixel scale_ yang mengatur faktor skala pada sumbu u dan v, dan _distortion coefficients_ yang mengoreksi distorsi dari lensa
        - Ekstrinsik: Merupakan parameter lokasi dan posisi dari kamera di dunia nyata, secara umum terdiri dari 2 komponen, yaitu translasi, vektor yang menentukan posisi kamera relatif terhadap dunia, dan rotasi, yaitu matriks yang menentukan orientasi kamera (pitch roll yaw) relatif terhadap dunia
        - Perbedaan: intrinsik megatur geometri dari lensa dan sensro sementara ekstrinsik menjelaskan lokasi dan posisi kamera di dunia nyata
    - Perspective projection matrix merupakan metode untuk memproyeksikan sebuah obyek tiga dimensi kepada sebuah layar dua dimensi dengan memperhitungkan kedalaman (_depth_) sebagai faktor nonlinear yang menghasilkan proyeksi yang akurat, obyek lebih jauh menghasilkan gambar yang lebih ekcil. Weak perspective projection marix memperhitungkan _depth_ sebagai faktor yang linear, sehingga menghasilkan gambar secara mudah dan murah, namun keakuratan yang rendah apabila dilihat secara dekat
    - Kalibrasi
        - Kalibrasi Linear: Kalibrasi yang mencakup penyesuaian sederhana, umumnya digunakan untuk fokus manual dan juga zoom. Penyesuaian parameter didasarkan deviasi/ketidaksesuaian yang terjadi, dengan proses penghitungan yang lebih sederhana
        - Kalibrasi Nonlinear: Model matematis yang mengatasi distorsi geometri lensa yang rumit, melalui proses pendeteksi titik-titik sudut pada grid 2d, lalu mencocokkannya terhadap koordinat 3d untuk memperbaiki parameter intrinsik.
5. OpenCV
6. Tracking