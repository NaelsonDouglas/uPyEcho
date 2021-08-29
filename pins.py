from machine import Pin

PINS ={
    'pump_empty' : 23
}

pin_pump_empty = Pin(PINS['pump_empty'], Pin.IN)