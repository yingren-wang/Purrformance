#!/usr/bin/env python3
"""
Focus Pet - Main Application
"""

import sys
from PyQt5.QtWidgets import QApplication
from pet.pet import Pet
from timer.timer import Timer
from ui.floating_window import FloatingWindow

def main():
    print("Welcome to Focus Pet!")
    # Create the application
    app = QApplication(sys.argv)
    
    # Create pet and timer
    my_pet = Pet("Lychee")
    my_timer = Timer()
    
    # Create and show the floating window
    window = FloatingWindow(my_pet, my_timer)
    window.show()
    
    # Run the application
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()