import filter
import random
import threading
def fun_timer():
    filter.updateip()
    global timer
    timer = threading.Timer(1800,fun_timer)
    timer.start()

timer = threading.Timer(1,fun_timer)
timer.start()