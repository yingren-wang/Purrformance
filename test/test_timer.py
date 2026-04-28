import pytest
from timer.timer import Timer

class TestTimer:
    def test_creation(self):
        timer = Timer(5)
        assert timer.duration_seconds == 300
        assert timer.remaining_seconds == 300
        assert timer.is_completed == False
        assert timer.is_paused == False
        assert timer.is_running == False
    
    def test_creation_with_short_duration(self):
        timer = Timer(0.1)
        assert timer.duration_seconds == 6
        assert timer.remaining_seconds == 6
        assert timer.is_completed == False
        assert timer.is_paused == False
        assert timer.is_running == False
    
    def test_creation_with_invalid_duration(self):
        with pytest.raises(ValueError):
            Timer(0)
        with pytest.raises(ValueError):
            Timer(-5)
        with pytest.raises(ValueError):
            Timer(0.0000000000000001)
    
    def test_start(self):
        timer = Timer(5)
        timer.start()
        assert timer.is_running == True
    
    def test_tick(self):
        timer = Timer(5)
        timer.start()
        timer.remaining_seconds = 10
        timer.tick()
        assert timer.remaining_seconds == 9
        assert timer.is_running == True
        assert timer.is_completed == False
    
    def test_completion(self):
        timer = Timer(5)
        timer.start()
        timer.remaining_seconds = 1
        timer.tick()
        assert timer.remaining_seconds == 0
        assert timer.is_completed == True
        assert timer.is_running == False
    
    def test_pause(self):
        timer = Timer(5)
        timer.start()
        timer.pause()
        assert timer.is_running == False
        assert timer.is_paused == True

    def test_continue(self):
        timer = Timer(5)
        timer.start()
        timer.pause()
        timer.start()
        assert timer.is_running == True
        assert timer.is_paused == False

    def test_display(self):
        timer = Timer(5)
        timer.start()
        assert timer.get_display_time() == "05:00"
        timer.tick()
        assert timer.get_display_time() == "04:59"
        timer.remaining_seconds = 0
        assert timer.get_display_time() == "00:00"

    def test_reset(self):
        timer = Timer(5)
        timer.start()
        timer.tick()
        timer.reset()
        assert timer.remaining_seconds == 300
        assert timer.is_completed == False
        assert timer.is_paused == False
        assert timer.is_running == False
    
    def test_cancel(self):
        timer = Timer(5)
        timer.start()
        timer.tick()
        timer.cancel()
        assert timer.remaining_seconds == 0
        assert timer.is_completed == False
        assert timer.is_paused == False
        assert timer.is_running == False