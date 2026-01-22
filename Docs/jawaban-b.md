# JAWABAN SOAL B
## Ivan, 16525136

### Jawaban Soal Utama
1. Pemograman Berorientasi Objek
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
5. Firmware
    
    a. _firmware_ merupakan sebuah perangkat lunak yang tertanam secara permanen pada perangkat keras untuk menjalankan operasi dasar. Secara umum, _firmware_ hanya mengandung instruksi sederhana dan berperan sebagai jembatan antara perangkat keras (_hardware_) dan perangkat lunak (_software_), perbedaan _firmware_ dengan perangkat lunak pada umumnnya adalah _firmware_ didesain agar pernawgkat keras dapat menjalankan fungsi utamanya, seperti memori dan juga _booting_ sementara, perangkat lunak pada umumnya didesain untuk berinteraksi langsung dengan pengguna, sehingga mengutamakan fleksibilitas dan mudah unutk menambah fitur ataupun perbaikan. Peran _firmware_ pada UAV terdiri atas berbagai aspek. Dari segi kontrol, _firmware_ menerjemahkan input dari pilot, dari segi sensor, _firmware_ juga berperan dalam membaca data sensor, dan menggunakannya untuk navigasi.
    
    b. RTOS adalah OS terkhusus untuk sistem yang memiliki karakteristik _time sensitive_, RTOS memprioritaskan efek jeda yang singkat, manajemen data yang efisien, dan memiliki sistem prioirtas untuk tiap kerjaan yang dilakukan

    c. Protokol Komunikasi Serial
    - UART: Universal Asynchronus Reciever Transmitter atau UART Merupakan sirkuit fisik dalam mikrokontroller antara 2 _device_ UART yang mengirim data secara langsung. Tipe data yang dikirim berupa paket, dimana paket tersebut memiliki _start bit_, _parity bit_, dan _end bit_. Ketiga kommponen ini berguna unutk mengetahui kapan data memulai dan berakhir, dan memastikan integritas dari data yang terkirim. UART merupakan protokol yang beroperasi tanpa clock sehingga _baud rates_ dari kedua _device_ UART harus mirip ataupun sama untuk meminimalisir kehilangan data
    - SPI: Serial Peripheral Interface atau SPI merupakan protokol komunikasi antara _device_ yang memiliki hubungan _master-slave_ yang menggunakan 4 kabel yaitu CS, SCLK, MISO, dan MOSI. CS (Chip Select) mengatur interkoneksi antara _device slave_ dan _master_ yang berfungsi untuk _master_ memilih mau berkomunikasi dengan _slave device_ yang mana. SCLK berfungsi untuk _master device_ mengirimkan _clock_ yang diatur sehingga _slave device_ tidak memerlukan _clock_ mereka sendiri. _Clock_ mengindikasikan kapan data akan ter-_sampled_. MOSI (Master Out Slave In) merupakan sarana untuk _master device_ mengirimkan data kepada _slave device_. MISO (Master In Slave Out) merupakan sarana untuk _slave device_ mengirimkan data kepada _master device_. Apabila _slave device_ melebihi satu, terdapat 2 rangkaian umum yang digunakan, yang pertama adalah _independent slaves_ dan yang kedua adalah _cooperative slaves_ atau _daisy chain_. 
    - I2C: Inter-integrated Circuit atau I2C merupakan protokol komunikasi antara _device_ yang memiliki hubungan _master-slave_ yang menggunakan 2 kabel yaitu SDA dan SCL. Pengiriman data menggunakan I2C memiliki template atau _frame_ yang terkhusus melalui kedua kabel ini. Dimulai dari _master devvice_ mengambil alih bus dengan memicu sebuah _start condition_ lalu _master device_ akan mengirim sebuah _slave address_ untuk memilih _slave device_ apa yang akan dituju, lalu _master device- memilih untuk antara _read_ dari _slave device_ atau _write_ data dari _slave device_. Setelah itu, _slave device_ akan _acknowledge_ keberadaan dari _master device_ lalu pengiriman data dimulai lalu di-_acknowledge_ setelah itu _master device_ akan mengirim sebuah _stop condition_ untuk menandakan bahwa pengiriman data selesai.
### Jawaban Soal ConCept
1. ROS
    - Nodes
    - Topic
    - Services
    - Parameter
    - Actions

2. Publisher & Subscriber
3. Service & Client
4. Pinhole Camera Model
5. OpenCV
6. Tracking