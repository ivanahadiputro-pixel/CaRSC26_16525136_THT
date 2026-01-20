import threading
import time
import pathlib


def Video_Capture():
    a = 0
    while a == 0:
        time.sleep(2)
        print("Recieving Video Frame...")
        

def Telemetry():
    with open("telemetry.txt", "r") as file:
        for line in file:
            time.sleep(3)
            print(line.rstrip())
            


thread1 = threading.Thread(target=Video_Capture)
thread1.start()

thread2 = threading.Thread(target=Telemetry)
thread2.start()