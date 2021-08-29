from pins import pin_empty_pump, pin_pump_power
from helpers import dbg

ACTIVATION_TIME = 2

def pump_control():
    dbg('The value of the pump sensor is %s' % pin_empty_pump.value())
    dbg('The value of the pump power is %s' % pin_pump_power.value())
    dbg('\n\n')
    if pin_empty_pump.value():
        pin_pump_power.on()
    else:
        pin_pump_power.off()
