from machine import Pin

PINS ={
    'pump_full': 21
    'pump_empty' : 23
    'pump_power' : 22,
    'pump_control': 2
}

pin_empty_pump = Pin(PINS['pump_full'], Pin.IN)
pin_full_pump = Pin(PINS['pump_empty'], Pin.IN)
pin_pump_power = Pin(PINS['pump_power'], Pin.OUT, value=0)
pin_pump_control = Pin(PINS['pump_control'], Pin.OUT, value=0)