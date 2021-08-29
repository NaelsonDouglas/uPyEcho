import time
import gc
from helpers import dbg
from app import App

#from pins import pin_pump_empty

def thread_echo(args):
    dbg('Entering main loop\n')
    alexa = App()
    while True:
        try:
            #print(pin_pump_empty.value())
            alexa.poller.poll(10)
            time.sleep(0.2)
            gc.collect()
        except Exception as e:
            dbg(e)
            break
