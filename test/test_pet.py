from pet.pet import Pet

def test():
    my_pet = Pet("Judy")
    print(f"{my_pet.name} starts with happiness: {my_pet.get_happiness()}")

    my_pet.increase_happiness(10)
    print(f"After focusing: {my_pet.get_happiness()}")

    my_pet.decrease_happiness(30)
    print(f"After neglecting: {my_pet.get_happiness()}")

if __name__ == "__main__":
    test()
    print("\n All tests passed!")