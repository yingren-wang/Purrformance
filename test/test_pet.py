from pet.pet import Pet

def test_pet_creation():
    pet = Pet("Fluffy")
    assert pet.name == "Fluffy"
    assert pet.get_happiness() == 70
    assert pet.get_growth() == 70
    assert pet.get_health() == 70

def test_pet_increase_happiness():
    pet = Pet("Fluffy")
    pet.increase_happiness(10)
    assert pet.get_happiness() == 80

def test_pet_decrease_happiness():
    pet = Pet("Fluffy")
    pet.decrease_happiness(30)
    assert pet.get_happiness() == 40

def test_pet_happiness_bounds():
    pet = Pet("Fluffy")
    pet.increase_happiness(200)
    assert pet.get_happiness() == 100
    pet.decrease_happiness(200)
    assert pet.get_happiness() == 0
    pet.decrease_happiness(10)
    assert pet.get_happiness() == 0

def test_pet_increase_growth():
    pet = Pet("Fluffy")
    pet.increase_growth(10)
    assert pet.get_growth() == 80

def test_pet_decrease_growth():
    pet = Pet("Fluffy")
    pet.decrease_growth(30)
    assert pet.get_growth() == 40

def test_pet_growth_bounds():
    pet = Pet("Fluffy")
    pet.increase_growth(200)
    assert pet.get_growth() == 100
    pet.decrease_growth(200)
    assert pet.get_growth() == 0
    pet.decrease_growth(10)
    assert pet.get_growth() == 0

def test_pet_increase_health():
    pet = Pet("Fluffy")
    pet.increase_health(10)
    assert pet.get_health() == 80

def test_pet_decrease_health():
    pet = Pet("Fluffy")
    pet.decrease_health(30)
    assert pet.get_health() == 40

def test_pet_health_bounds():
    pet = Pet("Fluffy")
    pet.increase_health(200)
    assert pet.get_health() == 100
    pet.decrease_health(200)
    assert pet.get_health() == 0
    pet.decrease_health(10)
    assert pet.get_health() == 0