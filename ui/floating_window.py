import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, QTimer
import time

class FloatingWindow(QWidget):
    def __init__(self, pet, timer):
        super().__init__()
        
        self.pet = pet
        self.timer = timer

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.Window |
            Qt.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(100, 100, 280, 220)
        
        self.drag_pos = None
        self.countdown_timer = None
        
        self.setup_ui()
        self.update_stats_display()
    
    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Pet emoji
        self.pet_label = QLabel("🐱")
        self.pet_label.setStyleSheet("font-size: 60px;")
        self.pet_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.pet_label)
        
        # Pet name
        self.name_label = QLabel(self.pet.name)
        self.name_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.name_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.name_label)
        
        # Stats display
        self.stats_label = QLabel()
        self.stats_label.setStyleSheet("font-size: 11px; font-family: 'Apple Color Emoji', 'Segoe UI Emoji', 'Noto Color Emoji', monospace; padding: 4px;")
        self.stats_label.setAlignment(Qt.AlignCenter)
        self.stats_label.setWordWrap(True)
        self.stats_label.setMinimumHeight(50)
        self.stats_label.adjustSize()
        layout.addWidget(self.stats_label)
                                        
        # Timer display
        self.timer_label = QLabel("25:00")
        self.timer_label.setStyleSheet("font-size: 24px; font-family: monospace;")
        self.timer_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.timer_label)
        
        # Buttons
        self.start_button = QPushButton("Start Focus")
        self.start_button.clicked.connect(self.start_focus)
        layout.addWidget(self.start_button)
        
        # self.feed_button = QPushButton("🍗 Feed")
        # self.feed_button.clicked.connect(self.feed_pet)
        # layout.addWidget(self.feed_button)
        
        # self.play_button = QPushButton("🎾 Play")
        # self.play_button.clicked.connect(self.play_with_pet)
        # layout.addWidget(self.play_button)
        
        self.setLayout(layout)
    
    def update_stats_display(self):
        """Update the stats label with current pet values"""
        self.stats_label.setText(
            f"❤️ Happiness: {self.pet.get_happiness()}\n "
            f"🌱 Growth: {self.pet.get_growth()}\n "
            f"💪 Health: {self.pet.get_health()}"
            # f"🪙 Coins: {self.pet.get_coins()}"
        )
        self.stats_label.repaint()
    
    def start_focus(self):
        """Start a focus session"""
        minutes = 0.1  # You can make this user-selectable later
        self.timer = type(self.timer)(minutes)  # Create new timer
        self.timer.start()
        
        self.start_button.setEnabled(False)
        self.start_button.setText("Focusing...")
        
        # Create a QTimer that ticks every second
        self.countdown_timer = QTimer()
        self.countdown_timer.timeout.connect(self.update_timer)
        self.countdown_timer.start(1000)  # 1000 ms = 1 second
    
    def update_timer(self):
        """Called every second during focus"""
        display_time = self.timer.get_display_time()
        self.timer_label.setText(display_time)
        
        self.timer.tick()
        
        if self.timer.is_completed:
            self.countdown_timer.stop()
            self.start_button.setEnabled(True)
            self.start_button.setText("Start Focus")
            self.timer_label.setText("25:00")
            
            self.pet.increase_growth(10)
            # self.pet.add_coins(5)
            self.update_stats_display()
            
            print("🎉 Focus complete! Pet growth increased!")
    
    # def feed_pet(self):
    #     """Feed the pet"""
    #     if self.pet.feed():
    #         self.update_stats_display()
    #         print("🍗 Pet fed! Happiness increased.")
    #     else:
    #         print("❌ Not enough coins! Complete a focus session first.")
    
    # def play_with_pet(self):
    #     """Play with the pet"""
    #     if self.pet.play():
    #         self.update_stats_display()
    #         print("🎾 Pet played! Happiness increased.")
    #     else:
    #         print("❌ Not enough coins! Complete a focus session first.")
    
    # Drag window functionality
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.drag_pos is not None:
            self.move(event.globalPos() - self.drag_pos)
            event.accept()
    
    def mouseReleaseEvent(self, event):
        self.drag_pos = None

    def showEvent(self, event):
        """Keep window on top by constantly raising it"""
        super().showEvent(event)
        self.raise_()
        self.activateWindow()

    def enterEvent(self, event):
        """Raise window when mouse enters"""
        self.raise_()
        self.activateWindow()