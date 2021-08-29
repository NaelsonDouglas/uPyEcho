import time
import gc
from helpers import dbg
from app import App

from pump import PlumbingSystem

def thread_echo(args):
    dbg('Entering main loop\n')
    alexa = App()
    plumbing = PlumbingSystem()
    while True:
        try:
            plumbing.control_water_level()
            dbg('Bomba -> %s' % plumbing.pump_state())
            alexa.poller.poll(10)
            time.sleep(0.2)
            gc.collect()
        except Exception as e:
            dbg(e)
            break
