
from microbit import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text

def light():
        l = display.read_light_level()
        pin0.write_analog(1023-l)
        l0 = str(l)
        initialize()
        clear_oled()
        add_text(0, 0, "light level:")
        add_text(0, 1,l0)
        sleep(300)

def temp():
        temp = temperature()
        if temp >= 25:
            pin16.write_digital(0)
            add_text(0, 2, "temp:")
            add_text(0, 3, str(temp))
            sleep(300)
        else:
            pin16.write_digital(1)
            sleep(300)

while True:
     pir = pin2.read_digital()
     if pir == 1:
        light()
        temp()
    
