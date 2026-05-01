class Timer:
    def __init__(self):
        self.duration_minites = 25
        self.is_running = False
        self.is_paused = False
        self.is_completed = False

    def set_duration(self, duration_minutes):
        self.duration_minutes = duration_minutes
        duration_seconds = int(duration_minutes * 60)
        if duration_seconds < 1:
            duration_seconds = 1
        self.remaining_seconds = duration_seconds

        print("Timer duration set")   

    def start(self):
        self.is_running = True

    def tick(self):
        if self.is_running and self.remaining_seconds > 0:
            self.remaining_seconds -= 1
        else:
            self.is_completed = True
            self.stop()
    
    def stop(self):
        self.is_running = False
        self.remaining_seconds = 0
        print("Timer stopped")

    def get_display_time(self):
        mins, secs = divmod(self.remaining_seconds, 60)
        return f"{mins:02d}:{secs:02d}"
    
    def pause(self):
        if self.is_running:
            self.is_running = False
            self.is_paused = True
        print("Timer is paused")

    # def cancel(self):
    #     self.is_running = False
    #     self.is_paused = False
    #     self.remaining_seconds = 0
    #     print("Timer is canceled")

    def reset(self):
        self.is_running = False
        self.is_paused = False
        self.is_completed = False
        self.remaining_seconds = int(self.duration_minutes * 60)
        print(f"Timer is reset, remaining seconds: {self.remaining_seconds} ")