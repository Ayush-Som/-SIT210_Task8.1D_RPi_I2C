'''
Task 7.3D Raspberry Pi PWM
Student ID - 2110994802
Name - Ayush Kumar Som 
'''
from signal import signal, SIGTERM, SIGHUP, pause
from time import sleep
from threading import Thread
from gpiozero import DistanceSensor
from rpi_lcd import LCD

running = True
message = ""

lcd = LCD()
sensor = DistanceSensor(echo = 20, trigger = 21)

def safe_exit():
    exit(1)

def read_distance():
    global message
    while running:
        lcd.text(message, 1)
        sleep(0.25)

def main():
    try:
        signal(SIGTERM, safe_exit)
        signal(SIGHUP, safe_exit)
        reader = Thread(target=read_distance, daemon=True)
        display = Thread(target=update_display, daemon=True)
        reader.start()
        display.start()
        pause()
    except KeyboardInterrupt:
        pass
    finally:
        global running
        running = False
        reader.join()
        lcd.clear()
        sensor.close()

if __name__ == '__main__':
    main()
