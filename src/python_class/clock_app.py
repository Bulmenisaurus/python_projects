# Features:
# 1. stopwatch (multi-threading, press stop )
# 2. Alarm (it is currently 13:15. What time do you want the alarm to sound?)
# 3. Timer (how long should the timer last? Example: 4m 49s
#
import time
import threading


class Timer:
    def __init__(self, duration, name):
        self.duration = duration
        self.name = name

    def __call__(self):
        print('Created timer', self.name)
        time.sleep(self.duration)
        print('Timer', self.name, 'has ended.')


class ClockManager:
    def __init__(self):
        """
        Class for the Clock app.
        where string is the name of the action and integer is the time since epoch
        when something expires or when it was created

        """
        self.alarms = {}
        self.timers = {}
        self.stopwatch = None

    @staticmethod
    def decode_duration(duration_string):
        """
        Converts string like 15m 10s to int(15*60 + 10)
        :return: the time in seconds
        """
        time_s = duration_string.lower().replace('m', 'm ').replace('s', 's ').replace('h', 'h ')
        time_s = ' '.join(time_s.split()).split()  # removes duplicate spaces, then splits into args
        totaltime = 0

        for arg in time_s:
            if arg.endswith('s'):
                totaltime += int(arg[:-1]) * 1
            elif arg.endswith('m'):
                totaltime += int(arg[:-1]) * 60
            elif arg.endswith('h'):
                totaltime += int(arg[:-1]) * 60 * 60
        return totaltime

    def spawn_timer(self, duration, name):
        self.timers[name] = Timer(duration, name)


def dostuff():
    while True:
        time.sleep(1.5)
        print('')


def inp():
    input('Waddya want')


thread = threading.Thread(target=dostuff)
thread.start()
inp()

