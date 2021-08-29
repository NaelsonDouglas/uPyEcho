from pins import pin_empty_pump, pin_full_pump, pin_pump_power
from time import sleep
from helpers import clock

ACTIVATION_TIME = 10

class PlumbingSystem:
    def __init__(self):
        self.tank  = Tank()
        self.pump  = Pump()

    def on(self):
        return self.pump.on()

    def off(self):
        return self.pump.off()

    def control_water_level(self):
        if self.tank.is_controlled():
           pass
        elif self.tank.is_low():
            dbg('LOW! pump -> on.')
            self.on()
        elif self.tank.is_overflown():
            dbg('OVERFLOW! pump -> off.')
            self.off()
        elif self.tank.is_invalid_state():
            pass #TODO implement Alarm


class Tank:
    def __init__(self):
        self.empty_pin = pin_empty_pump

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Tank, csl).__new__(cls)
        return cls.instance

    def is_full(self):
        return bool(pin_full_pump.value())

    def is_empty(self):
        return bool(pin_empty_pump.value())

    def is_controled(self):
        return not self.is_empty() and not self.is_full()

    def is_low(self):
        return self.is_empty() and not self.is_full()

    def is_overflown(self):
        return not self.is_empty() and self.is_full()

    def is_invalid_state(self):
        return self.is_empty() and self.is_full()


class Pump:
    def __init__(self):
        self.control_pin = pin_pump_control
        self.is_on = False
        self.last_activation = clock.now()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Pump, csl).__new__(cls)
        return cls.instance

    def on(self):
        if not self.is_on:
            self.is_on = True
            self.command()
        return True

    def off(self):
        self.is_on = False
        self.command()
        return True

    def command(self):
        self.control_pin.on()
        sleep(0.25)
        self.control_pin.off()