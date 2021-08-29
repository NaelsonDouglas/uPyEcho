import time
import gc
from helpers import dbg
from app import App

from pump_control import pump_control

def thread_echo(args):
    dbg('Entering main loop\n')
    alexa = App()
    while True:
        try:
            pump_control()
            alexa.poller.poll(10)
            time.sleep(0.2)
            gc.collect()
        except Exception as e:
            dbg(e)
            break
