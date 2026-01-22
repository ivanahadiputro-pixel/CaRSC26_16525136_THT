# Header untuk import object-object yang dibutuhkan
import threading
import time
from pathlib import Path

# Fungsi Pertama untuk print "Recieving Video Frame..." setiap 2 detik
def Video_Capture():
    a = 0
    while a == 0:
        time.sleep(2)
        print("Recieving Video Frame...")
        
# Fungsi kedua untuk print tiap baris dalam "telemetry.txt" satu per satu setiap 3 detik
def Telemetry():
    src_dir = Path(__file__).resolve().parent
    
    telemetry_path = src_dir.parent.parent / "lampiran" / "telemetry.txt"

    with telemetry_path.open("r") as file:
        for line in file:
            time.sleep(3)
            print(line.rstrip())
            

# Program utama, masing-masing thread/fungsi dijalankan secara bersamaan tanpa memengaruhi satu sama lain
thread1 = threading.Thread(target=Video_Capture)
thread1.start()

thread2 = threading.Thread(target=Telemetry)
thread2.start()