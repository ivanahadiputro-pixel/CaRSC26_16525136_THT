# JAWABAN SOAL BAGIAN A
## Ivan, 16525136
### Jawaban
1. Analisis Kondisi, Email: ivan.a.hadiputro@gmail.com
2. Source Control Management

    a. Command-Command dalam git.
    - Git Commit: Berfungsi untuk merekam _staged changes_ dari pemrograman dan berfungsi untuk membuat perubahan bersifat tetap dalam repositori
    - Git Branch: Berfungsi untuk membuat sebuah branch baru pada git, berguna untuk membuat perubahan yang bisa di _test_ kembali dengan metode _trial and error_, tanpa membuat perubahan pada branch utama (origin, main)
    - Git Merge: Berfungsi untuk menggabungkan satu branch dengan branch utamanya, sistem mendeteksi perubahan atau _delta_ dari kedua pemrograman tersebut, dan branch akan menghilang lalu hanya tersisa branch utama
    - Git Pull: Berfungsi untuk men-_download_ item dari _remote branch_ dan secara otomatis akan merge branch hasil downloadan dan pemrograman dapat di edit secara lokal
    - Git Push: Berfungsi untuk meng-_upload_ hasil pemrorgraman dari _local branch_ pada _remote branch_

    b. Tangkapan layar "Source Control"
    ![2b](<../lampiran/Screenshot 2026-01-19 002759.png>)
    c. Tangkapan layar "learngitbranching"
    ![2c pic 1](<../lampiran/Screenshot 2026-01-18 145712.png>)
    ![2C PIC 2](<../lampiran/Screenshot 2026-01-18 150909.png>)
   
    d. Tangkapan layar "Git SSH Security"
    ![2d](<../lampiran/Screenshot 2026-01-18 170845.png>)
    e. Branch History
    ![alt text](<../lampiran/Screenshot 2026-01-22 214418.png>)
3. Pengenalan Ground Control Station

    a. Tangkapan layar utama Mission Planner
    ![3a](<../lampiran/Screenshot 2026-01-19 014235.png>)
    b. 4 fitur utama pada mission planner
    - Data: Memantau kondisi UAV secara _real time_, mengandung informasi seperti posisi UAV, _roll pitch yaw_, kecepatan, dan kondisi baterai dari UAV
    - Plan: Membuat dan mengatur misi terbang secara otomatis, merancang jalur UAV sebelum penerbangan melalui waypoints, takeoff dan landing, dan sebagainya
    - Setup/Config: Konfigurasi awal dan kalibrasi sistem pada UAV sebelum penerbangan dengan tujuan UAV siap terbang secara aman
    - Simulation: Simulasi dan analisis penerbangan, digunakan untuk uji coba dan evaluasi misi penerbangan tanpa adanya risiko
    
    c. Tangkapan layar _"mapping mission"_
    ![3c](<../lampiran/Screenshot 2026-01-18 173652.png>)
4. Development Environment
    
    Instalasi Ubuntu 22.04 LTS menggunakan Orcale VM VirtualBox
    - Instalation 
    ![alt text](<../lampiran/Screenshot 2026-01-19 164837.png>)
    - Talker Listener
    ![alt text](<../lampiran/Screenshot 2026-01-19 163626.png>)
    ![alt text](<../lampiran/Screenshot 2026-01-19 163651.png>)


5. Dasar-Dasar UAV
   
    a. Cara Terbang 
    - VTOL/Rotary Wing

         Mekanisme: 
        - Menggunakan rotor atau baling-baling yang menghasilkan gaya angkat
        - Perbedaan kecepatan putar motor menentukan besar gaya angkat
     
         Karakteristik:
         - Presisi dalam geraknya
         - Dapat diam di udara / _hover_
         - Konsumsi energi besar yang menghasilkan waktu terbang relatif singkat
    
         Contoh: Helicopter Drone, Quadcopter

    - HTOL/Fixed Wing

        Mekanisme:
        - Gaya angkat dihasilkan oleh sayap akibat aliran udara saat UAV bergerak ke depan
        - Memiliki kecepatan minimal untuk tetap terbang di udara

        Karakteristik:
        - Efisiensi energi tinggi
        - Jangkauan pemetaan yang luas
        - Tidak bisa _hover_

        Contoh: Skywalker X8

    b. 
    - Perbedaan Gerak:
        - Roll: Rotasi terhadap sumbu tubuh memanjang atau sumbu x, yang menghasilkan UAV/pesawat untuk miring ke kanan atau ke kiri
        - Pitch: Rotasi terhadap sumbu tubuh lateral atau sumbu y, yang menghasilkan hiung dari UAV / pesawat untuk naik atau turun
        - Yaw: Rotasi terhadap sumbu tubuh vertikal atau sumbu z, yang menghasilkan UAV / pesawat untuk belok ke kanan atau ke kiri
    - Speed:
        - Air Speed: Kecepatan relatif terhadap udara di sekitarnya dan secara umum digunakan untuk menjaga gaya angkat terutama pada model _fixed wing_
        - Ground Speed: Kecepatan relatif terhadap permukaan bumi dan diukur menggunakan GPS
        - Hubungan: Ground Speed = Air Speed + Kecepatan angin. Dalam pemetaan _ground speed_ memengaruhi _overlap_ foto pesawat pada peta
    - HDOP dalam GPS: Indikator dari kualitas satelit GPS dalam menentukan posisi horizontal (Nilai yang kebih kecil mengartikan kualitas yang lebih baik)
    - RSSI dalam Telekomunikasi: Indikator kuatnya sinyal yang diterima, diukur dalam dBm (desibel terhadap miliwatt) nilai RSSI yang mendekati 0 menandakan sinyal yang lebih kuat. Dalam aplikasi UAV, terutama digunakan untuk monitoring ikatan komunikasi UAV-GCS
    
    c. Komponen dalam UAV:
    - Airframe: Kerangka atau model fisik dari UAV
    - Motor: Menghasilkan gaya dorong dan angkat
    - Flight Controller: Otak dari UAV, berfungsi untuk mengontrol stabilisasi dan juga navigasi
    - GPS Module: Menentukan posisi dan kecepatan dari UAV
    - Power System: Menyimpan daya yang tersisa pada UAV, secara umum berbentuk baterai
    - Telemetry: Komunikasi data antara UAV dan GCS
    - Ground Control Station: Monitoring dan kendali misi / _mission_
    - ESC: Mengatur kecepatan dari motor
    - Diagram Block: 
    ![alt text](<../lampiran/WhatsApp Image 2026-01-22 at 18.46.41.jpeg>)
    
    d. Jurnal Mengenai UAV
    - Konten: Komunikasi seluler pada UAV. Perkembangan UAV / _Drone_ yang tersedia untuk konsumen umum menghasilkan adanya kesempatan bisnis bagi para operator telekomunikasi contohnya, UAV yang terhubung dengan jaringan seluler dapat menjadi alat tambahan bagi pengguna yang dapat menghasilkan _revenue_ bagi perusahaan yang memiliki layanan untuk penggunaan UAV. Terdapat juga kesempatan untuk meletakkan _node_ telekomunikasi pada UAV sehingga dapat beradaptasi seusia kondisi dan meningkatkan jangkauan dari jaringan.
    Saya memilih jurnal ini karena jurnal ini menyadarkan saya bahwa dampak dari UAV di dunia bukan sekedar perkembangan teknologi dari UAV itu sendiri, melainkan manfaat dari UAV sebagai sarana bisnis B2B (Business to Business) memiliki potensi yang sangat besar, sehingga dampak pada masyarakat juga terasa lebih luas dan mendalam.
    - Sumber: [Link Sumber](https://arxiv.org/pdf/1809.01752)

6. Algoritma
    - A-Star (A*) & D-Star (D*):
        - A*: A* Merupakan algoritma _pathfinding_ yang dikembangkan dari algortima _Djikstra_, keunggulan algoritma A* dibanding _Djikstra_ adalah algoritma A* menambah variabel lain selain jarak ke noda tetangga, yaitu jarak antara noda dengan tujuan akhir yang disebut sebagai _heuristic_. Dengan menggunakan algoritma A*, algoritma menentukan jalur yang paling sesuai dengan menambahkan jarak yang ditempuh dengan _heuristic_-nya. Pada algoritma ini, _heuristic_ berfungsi sebagai penanda kasaran "arah" yang sesuai
        - D*: Merupakan perkembangan dari algortima A*, namun dirancang untuk dapat melampaui peta yang dinamis atau berubah-berubah, hal ini dilakukan dengan memperbarui jalur secara inkremental saat informasi baru terrekam, dan tidak perlu mennghitung total. Keunggulan D* dibanding A* adalah algoritma D* efisien dalam beradaptasi
    - Proportional Integral-Derivative (PID): Proportional Integral Derivative atau PID adalah sebuah algortima kendali / _control_ yang didesain untuk regulasi sebuah sistem secara otomatis agar _output_ yang dihasilkan memenuhi sebuah hasil yang diinginkan. Pada algoritma PID, terdapat 3 komponen utama yaitu, Proportional, Integral, dan Derviative

        - Proportional: Berfungsi untuk menghasilkan output sesuai dengan _error_ atau ketidaksesuaian yang terjadi, komponen ini memiliki responsi yang sangat tinggi, namun tidak stabil sehingga memiliki risiko untuk menghasilkan osilasi
        - Integral: Menghitung _error_ secara kumulatif sepanjang suatu rentang waktu, komponen integral sangat baik untuk stabilitas jangka panjang dan akurasi, namun memiliki responsi yang relatif lambat
        - Derivative: Menghitung _error_ berdasarkan laju perubahan _error_ tersebut, komponen _derivative_ ini berfungsi untuk memperlambat output ketika _error_ menuju 0

        Ketiga komponen ini pada akhirnya saling membantu dan menutupi kelemahan komponen lain sehingga hasil yang diperoleh meraih _value_ yang diinginkan. Hal ini menyebabkan PID menjadi algoritma kendali yang _reliable_ dan konsisten.
    - Kalman Filter & Extended Kalman Filter: 
    
        - Kalman Filter: Merupakan model estimasi yang rekursif, dengan memprediksi sistem yang linear menggunakan model matematis dan juga pengukuran gangguan / _noise_ dengan mengasumsi sebuah _gaussian noise_ atau gangguan yang modelnya mengikuti pola distribusi normal
        - Extended Kalman Filter: Merupakan perkembangan dari kalman filter yang lebih tepat digunakan untuk model yang _nonlinear_, hal ini dilakukan dengan melinearisasikan kondisi-kondisi atau model sekitar hasil estimasi menggunakan standard kalman filter.

        EKF lebih cocok digunakan untuk aplikasi teknis yang real, seperti UAV dan robotika, hal ini disebabkan tidak ada model teknis real yang sepenuhnya linear.  


sumber:

- https://learngitbranching.js.org
- https://youtu.be/i0oL5wek-c4?si=KKEgFC6mq-GbyQYI
- https://www.faa.gov/regulations_policies/handbooks_manuals
- https://youtu.be/ySN5Wnu88nE?si=FdbdeYEfvw-e-RL7
- https://fbswiki.org/wiki/index.php/Main_Page
- https://www.cs.unc.edu/~welch/media/pdf/kalman_intro.pdf



