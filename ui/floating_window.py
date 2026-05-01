import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt, QTimer
import time
from timer.timer import Timer

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
        
        self.setup_ui()
        self.update_stats_display()

        self.clock = QTimer()
        self.clock.timeout.connect(self.update_timer_and_display)
    
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

        button_layout = QVBoxLayout()
        self.feed_button = QPushButton("🍗 Feed")
        self.feed_button.clicked.connect(self.feed_pet)
        button_layout.addWidget(self.feed_button)
        self.play_button = QPushButton("🎾 Play")
        self.play_button.clicked.connect(self.play_with_pet)
        button_layout.addWidget(self.play_button)
        self.focus_button = QPushButton("⏱️ Focus")
        self.focus_button.clicked.connect(self.on_focus_clicked)
        button_layout.addWidget(self.focus_button)
        layout.addLayout(button_layout)

        # Timer Widget                         
        timer_widget = QWidget()
        timer_widget.setFixedHeight(80)
        timer_layout = QVBoxLayout(timer_widget) 
        timer_layout.setSpacing(6)
        
        # Timer Display
        self.timer_label = QLabel()
        self.timer_label.setStyleSheet("font-size: 24px; font-family: monospace;")
        self.timer_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.timer_label.hide()
        timer_layout.addWidget(self.timer_label)
       
        # Start Button
        self.start_button = QPushButton("Start Focus")
        self.start_button.clicked.connect(self.on_focus_start_clicked)
        self.start_button.hide()
        timer_layout.addWidget(self.start_button)
        # todo: start button can be in horizontal layout with pause and cancel buttons, and only show when timer is active

        timer_layout.addStretch()

        layout.addWidget(timer_widget)

        self.setLayout(layout)
    
    def update_stats_display(self):
        """Update the stats label with current pet values"""
        self.stats_label.setText(
            f"💪 Health: {self.pet.get_health()}\n"
            f"❤️ Happiness: {self.pet.get_happiness()}\n "
            f"🌱 Growth: {self.pet.get_growth()}"
            # f"🪙 Coins: {self.pet.get_coins()}"
        )
    
    def on_focus_clicked(self):
        self.start_button.show()
        self.timer_label.show()
        # todo: prompt timer duration input
        self.timer = Timer(0.1)
        self.timer_label.setText(self.timer.get_display_time())
        
    def on_focus_start_clicked(self):
        self.start_button.hide()
        # todo: prompt timer duration input
        self.timer.start()
        self.clock.start(1000)
    
    def update_timer_and_display(self):
        if self.timer is None:
            return
        
        self.timer.tick()
        self.timer_label.setText(self.timer.get_display_time())
        if self.timer.is_completed:
            self.clock.stop()
            self.timer_label.hide()
            self.start_button.hide()
            
            self.pet.increase_growth(10)
            self.update_stats_display()
            print("🎉 Focus complete! Pet growth increased!")

    def update_timer_display(self):
        mins, secs = divmod(self.remaining_seconds, 60)
        self.timer_label.setText(f"{mins:02d}:{secs:02d}")

    def feed_pet(self):
        if self.pet.got_fed():
            self.update_stats_display()
            print("🍗 Pet fed! Happiness increased.")
       
    def play_with_pet(self):
        if self.pet.invited_to_play():
            self.update_stats_display()
            print("🎾 Pet played! Happiness increased.")
        
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