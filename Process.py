class Process:
    def __init__(self, arrival_time, burst_time):
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.executed = 0
        self.start_time = None
        self.end_time = None
