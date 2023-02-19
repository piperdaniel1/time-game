import time
from datetime import datetime as dt, timedelta as td

class PomodoroTimer:
    def __init__(self, work_time=25, break_time=5):
        self.work_time = td(minutes=work_time)
        self.break_time = td(minutes=break_time)
        self.working = True
        self.end_time = dt.now() + self.work_time
        self.paused = True
        self.last_pause_start = dt.now()
    
    def unpause(self):
        self.end_time = dt.now() + self.work_time + (self.last_pause_start - dt.now())
        self.paused = False
    
    def est_time_left(self) -> td:
        if self.paused:
            return self.end_time - dt.now() + (self.last_pause_start - dt.now())
        else:
            if self.end_time - dt.now() < td(seconds=0):
                if self.working:
                    self.working = False
                    self.end_time = dt.now() + self.break_time
                else:
                    self.working = True
                    self.end_time = dt.now() + self.work_time

            return self.end_time - dt.now()
        
    def get_phase(self):
        if self.working:
            return "Working"
        else:
            return "Break"
    
    def pause(self):
        self.last_pause_start = dt.now()
        self.paused = True
    
    def is_paused(self):
        return self.paused