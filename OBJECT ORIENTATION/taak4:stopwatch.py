import time

class StopWatch:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        #de stopwatch start automatisch door de functie start() op te roepen
        self.start()

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return self.end_time

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    #tijd verstreken tussen starten en stoppen in milliseconden
    def get_elapsed_time(self):
        elapsed_time = self.end_time - self.start_time
        elapsed_time_milli = int(elapsed_time * 1000)
        return elapsed_time_milli