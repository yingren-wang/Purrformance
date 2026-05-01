class Timer:
    def __init__(self, duration_minutes=25):
        self.duration_seconds = int(duration_minutes * 60)
        if self.duration_seconds < 1:
            raise ValueError(f"Duration must be at least 1 second, got {self.duration_seconds} seconds")
        self.remaining_seconds = self.duration_seconds
        self.is_running = False
        self.is_paused = False
        self.is_completed = False

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
        print("Timer stopped")

    def get_display_time(self):
        mins, secs = divmod(self.remaining_seconds, 60)
        return f"{mins:02d}:{secs:02d}"
    
    # def pause(self):
    #     if self.is_running:
    #         self.is_running = False
    #         self.is_paused = True
    #     print("Timer is paused")

    # def cancel(self):
    #     self.is_running = False
    #     self.is_paused = False
    #     self.remaining_seconds = 0
    #     print("Timer is canceled")

    # def reset(self):
    #     self.is_running = False
    #     self.is_paused = False
    #     self.is_completed = False
    #     self.remaining_seconds = self.duration_seconds
    #     print("Timer is reset")