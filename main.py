from machine import Pin
from time import sleep

def dot():
    print('.')

def main():
    while True:
        r1 = btn_red.value()
        sleep(.01)
        r2 = btn_red.value()
        if r1 and not r2:
            dot()

if __name__ == "__main__":
    try:
        btn_red = Pin(18, Pin.IN, Pin.PULL_UP)
        main()
    finally:
        print('goodbye')
