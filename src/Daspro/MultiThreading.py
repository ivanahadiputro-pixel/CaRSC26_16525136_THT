import threading
import time
from pathlib import Path


def Video_Capture():
    a = 0
    while a == 0:
        time.sleep(2)
        print("Recieving Video Frame...")
        

def Telemetry():
    src_dir = Path(__file__).resolve().parent
    
    telemetry_path = src_dir.parent.parent / "lampiran" / "telemetry.txt"

    print(f"Reading telemetry from: {telemetry_path}")

    with telemetry_path.open("r") as file:
        for line in file:
            time.sleep(3)
            print(line.rstrip())
            


thread1 = threading.Thread(target=Video_Capture)
thread1.start()

thread2 = threading.Thread(target=Telemetry)
thread2.start()