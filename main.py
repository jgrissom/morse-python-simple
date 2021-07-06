from machine import Pin
from time import sleep

def dot():
    print('.')
    
def dash():
    print('-')

def main():
    while True:
        g1 = btn_green.value()
        r1 = btn_red.value()
        sleep(.01)
        g2 = btn_green.value()
        r2 = btn_red.value()
        if r1 and not r2:
            dot()
        elif g1 and not g2:
            dash()

if __name__ == "__main__":
    try:
        btn_red = Pin(18, Pin.IN, Pin.PULL_UP)
        btn_green = Pin(5, Pin.IN, Pin.PULL_UP)
        main()
    finally:
        print('goodbye')
