import time
from timer.timer import Timer

def test_timer():
    print("=== Timer Test ===\n")
    
    timer = Timer(0.1) # 0.1 minute = 6 secs used to test
    timer.start()
    
    while timer.is_running:
        timer.tick()
        time.sleep(1)
        print(f"\rTime left: {timer.get_display_time()}", end='')
    
    print("\n\n✅ Timer completed!")

if __name__ == "__main__":
    test_timer()