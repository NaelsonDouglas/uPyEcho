from pins import pin_empty_pump, pin_full_pump, pin_pump_control
import time
from helpers import clock, dbg

MINUTE_MS = 60000
COOLDOWN = 1 * MINUTE_MS
class PlumbingSystem:
    def __init__(self):
        self.tank  = Tank()
        self.pump  = Pump()
        self.last_activation = time.ticks_ms() - MINUTE_MS

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PlumbingSystem, cls).__new__(cls)
        return cls.instance

    def on(self):
        now = time.ticks_ms()
        time_diff = time.ticks_diff(now, self.last_activation)
        dbg('TIME_DIFF %s'% time_diff)
        if  time_diff >= COOLDOWN:
            self.last_activation = now
            self.pump.on()
            dbg('LOW! pump -> on.')
        else:
            dbg('In Cooldown!')
        return True

    def pump_state(self):
        state = 'desligada'
        if self.pump.is_on:
            state = 'ligada'
        return state

    def off(self):
        return self.pump.off()

    def control_water_level(self):
        if self.tank.is_controled():
           pass
        elif self.tank.is_low():
            self.on()
        elif self.tank.is_overflown():
            dbg('OVERFLOW! pump -> off.')
            self.off()
        elif self.tank.is_invalid_state():
            dbg('INVALID_STATE')
            self.off()
            pass #TODO implement Alarm

class Tank:
    def __init__(self):
        self.empty_pin = pin_empty_pump

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Tank, cls).__new__(cls)
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
        self.last_activation = time.ticks_ms() - MINUTE_MS

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Pump, cls).__new__(cls)
        return cls.instance

    def on(self):
        if not self.is_on:
            self.is_on = True
            self.command()
        return True

    def off(self):
        if self.is_on:
            self.is_on = False
            self.command()
        return True

    def command(self):
        self.control_pin.on()
        time.sleep(0.35)
        self.control_pin.off()