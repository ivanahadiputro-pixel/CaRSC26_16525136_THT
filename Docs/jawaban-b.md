# JAWABAN SOAL B
## Ivan, 16525136

### Jawaban Soal Utama
1. Pemograman Berorientasi Objek
2. Bahasa C++
    - #include <file_name> dan #include "file name", keduanya digunakna untuk menyertakan isi file lain ke dalam file sumber. Perbedaannya adalah penggunaan <file_name> akan mengakibatkan sistem untuk mencari di _file system directories_ sementara penggunaan tanda petik "file_name" mengakibatkan sistem untuk mencari di direktori lokal terlebih dahulu, lalu sistem
    - Penggunaan #ifdef, #ifndef, #endif dan #pragma once dalam header file: Menentukan subprogram atau blok kode mana yang dijalankna berdasarkan tipe header yang telah terdefinisi. Contoh : #ifdef Header_Ex, apabila Header_Ex terdefinisi maka blok kode di antara #ifdef dan #endif akan terjalani, apabil abelum terdefinisi, maka blok kode di antara #ifndef dan #endif akn terjalani
    - Penggunaan namespace dan scope resolution operator (::)

        Namespace digunakna untuk mengelompokkan nama agar tidak terjadi konflik, semnetara :: digunakan untuk mengakses anggota namespace ataupun class

    - Perbedaan #define dan using: #define merupakan direktif untuk mengarahkan preprocessor untuk mengganti semua kemunculan makro (objek, fungsi) dengan token pengganti yang sudah ditentukan, sementara using merupakan kata kunci untuk membawa anggota namespace ke dalam scope program tanpa harus menuliskan kembali scope resolution operator yang bergantung pada using yang telah terdefinisikan
    - Cara kerja pointer (*) dan address of (&): Pointer merupakan operator untuk menyimpan memori address dari variabel yang setipe, sementara address of akan mengembalikan nilai dari lokasi dalam memori dimana variabel tersebut tersimpan\
    - Konsep pass by value dan pass by reference dalam definisi variabel dan fungsi


3. Multithreading
    - Multithreading merupakan model dalam pemrograman untuk menjalankan 2 subprogram atau _thread_ secara bersamaan tanpa mengganggu satu sama lain
    - 
4. Header
5. Firmware
    
    a. _firmware_ merupakan sebuah perangkat lunak yang tertanam secara permanen pada perangkat keras untuk menjalankan operasi dasar. Secara umum, _firmware_ hanya mengandung instruksi sederhana dan berperan sebagai jembatan antara perangkat keras (_hardware_) dan perangkat lunak (_software_), perbedaan _firmware_ dengan perangkat lunak pada umumnnya adalah _firmware_ didesain agar pernawgkat keras dapat menjalankan fungsi utamanya, seperti memori dan juga _booting_ sementara, perangkat lunak pada umumnya didesain untuk berinteraksi langsung dengan pengguna, sehingga mengutamakan fleksibilitas dan mudah unutk menambah fitur ataupun perbaikan. Peran _firmware_ pada UAV terdiri atas berbagai aspek. Dari segi kontrol, _firmware_ menerjemahkan input dari pilot, dari segi sensor, _firmware_ juga berperan dalam membaca data sensor, dan menggunakannya untuk navigasi.
    
    b. RTOS adalah OS terkhusus untuk sistem yang memiliki karakteristik _time sensitive_, RTOS memprioritaskan efek jeda yang singkat, manajemen data yang efisien, dan memiliki sistem prioirtas untuk tiap kerjaan yang dilakukan

    c. Protokol Komunikasi Serial
    - UART
    - SPI
    - I2C
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