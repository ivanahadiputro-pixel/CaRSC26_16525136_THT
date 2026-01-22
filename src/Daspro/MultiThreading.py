import threading
import time
import os


def Video_Capture():
    a = 0
    while a == 0:
        time.sleep(2)
        print("Recieving Video Frame...")
        

def Telemetry():
    src_dir = os.path.dirname(os.path.abspath(__file__))

    main_folder_dir = os.path.abspath(os.path.join(src_dir, ".."))
    telemetry_path = os.path.join(main_folder_dir, "lampiran", "telemetry.txt")

    print(f"Reading telemetry from: {telemetry_path}")

    with open(telemetry_path, "r") as file:
        for line in file:
            time.sleep(3)
            print(line.rstrip())
            


thread1 = threading.Thread(target=Video_Capture)
thread1.start()

thread2 = threading.Thread(target=Telemetry)
thread2.start()