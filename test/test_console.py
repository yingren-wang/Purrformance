import time
from pet.pet import Pet
from timer.timer import Timer

def test_timer_completion_increases_pet_growth():
    pet = Pet("Hello Kitty")
    initial_growth = pet.get_growth()
    
    timer = Timer(0.1)
    timer.start()
    
    while timer.is_running:
        timer.tick()
    
    assert timer.is_completed == True
    
    # Simulate reward
    if timer.is_completed:
        pet.increase_growth(10)
    
    assert pet.get_growth() == initial_growth + 10