from machine import Pin
from time import sleep

def dot():
    print('.')
    led_red.on()
    sleep(.1)
    led_red.off()
    
def dash():
    print('-')
    led_red.on()
    sleep(.2)
    led_red.off()

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
        led_red = Pin(26, Pin.OUT)
        main()
    finally:
        print('goodbye')
        led_red.off()
