import time
from timer import PomodoroTimer
import colored as cl
import os
import pickle

def fmt_time(time_phase, time_str, time_td):
    if len(time_str) % 2 != len(time_phase) % 2:
        time_str = "0" + time_str
    
    time_str_len = len(time_str)
    width = 36
    if time_str_len % 2 == 1:
        width += 1
    
    text_padding = (width - time_str_len - 2) // 2
    time_phase = time_phase.upper()

    time_phase_len = len(time_phase)
    phase_padding = (width - time_phase_len - 2) // 2

    if time_phase == "WORKING":
        time_phase = cl.fg("red") + time_phase + cl.attr("reset")
    elif time_phase == "BREAK":
        time_phase = cl.fg("green") + time_phase + cl.attr("reset")
    
    if time_td.seconds < 60:
        time_str = cl.fg("red") + time_str + cl.attr("reset")
    elif time_td.seconds < 120:
        time_str = cl.fg("yellow") + time_str + cl.attr("reset")
    else:
        time_str = cl.fg("green") + time_str + cl.attr("reset")
    
    wall_char = "-"
    wall_char = cl.fg("blue") + wall_char + cl.attr("reset")

    print(wall_char * width)
    print(wall_char + " " * (width-2) + wall_char)
    print(wall_char + " " * phase_padding + time_phase + " " * phase_padding + wall_char)
    print(wall_char + " " * text_padding + time_str + " " * text_padding + wall_char)
    print(wall_char + " " * (width-2) + wall_char)
    print(wall_char * width)

def on_press(key):
    print("Key pressed: " + str(key))
    # print(key)
    pass

def on_release(key):
    pass

def pause_timer():
    timer.pause()
    input("Press enter to unpause")
    timer.unpause()

# Create a timer object
if os.path.exists(".timer.pickle"):
    print("Loading timer from file...")
    with open(".timer.pickle", "rb") as f:
        timer = pickle.load(f)
else:
    timer = PomodoroTimer()

if timer.is_paused():
    timer.unpause()

# Main Event Loop
try:
    while True:
        time_left = timer.est_time_left()
        phase = timer.get_phase()

        # from timedelta class code
        mm, ss = divmod(time_left.seconds, 60)
        hh, mm = divmod(mm, 60)
        microseconds = time_left.microseconds

        if hh > 0:
            time_str = "%d:%02d:%02d:%02d" % (hh, mm, ss, microseconds/10000)
        else:
            time_str = "%02d:%02d:%02d" % (mm, ss, microseconds/10000)

        os.system("cls" if os.name == "nt" else "clear")
        fmt_time(phase, time_str, time_left)

        time.sleep(0.11)
except KeyboardInterrupt:
    timer.pause()
    with open(".timer.pickle", "wb") as f:
        pickle.dump(timer, f)