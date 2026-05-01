import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
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

        # self.setAttribute(Qt.WA_TranslucentBackground)
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

        interaction_button_layout = QHBoxLayout()
        self.feed_button = QPushButton("🍗 Feed")
        self.feed_button.clicked.connect(self.feed_pet)
        interaction_button_layout.addWidget(self.feed_button)
        self.play_button = QPushButton("🎾 Play")
        self.play_button.clicked.connect(self.play_with_pet)
        interaction_button_layout.addWidget(self.play_button)
        self.focus_button = QPushButton("⏱️ Focus")
        self.focus_button.clicked.connect(self.on_focus_clicked)
        interaction_button_layout.addWidget(self.focus_button)
        layout.addLayout(interaction_button_layout)

        # Timer Widget                         
        self.timer_widget = QWidget()
        self.timer_widget.setFixedHeight(100)
        self.timer_layout = QVBoxLayout(self.timer_widget) 
        self.timer_layout.setSpacing(6)
        
        # Timer Display
        self.timer_label = QLabel()
        self.timer_label.setStyleSheet("font-size: 24px; font-family: monospace;")
        self.timer_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        self.timer_layout.addWidget(self.timer_label)
    
        # Timer Control Buttons
        self.timer_button_widget = QWidget()
        self.timer_button_layout = QHBoxLayout(self.timer_button_widget)
        # Start Button
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.on_focus_start_clicked)
        self.timer_button_layout.addWidget(self.start_button)
        self.pause_button = QPushButton("Pause")
        self.pause_button.clicked.connect(self.on_focus_pause_clicked)
        self.timer_button_layout.addWidget(self.pause_button)
        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.on_focus_stop_clicked)
        self.timer_button_layout.addWidget(self.stop_button)
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.on_focus_reset_clicked)
        self.timer_button_layout.addWidget(self.reset_button)
        
        self.timer_layout.addWidget(self.timer_button_widget)
        self.timer_widget.hide()
        layout.addWidget(self.timer_widget)
        layout.addStretch()

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
        self.timer_widget.show()
        # todo: prompt timer duration input
        self.timer.set_duration(0.1)
        self.timer_label.setText(self.timer.get_display_time())
        print(f"Showing timer widget: {self.timer_widget}")
        print(f"Timer widget parent: {self.timer_widget.parent()}")

    def on_focus_start_clicked(self):
        # todo: prompt timer duration input
        self.timer.start()
        self.clock.start(1000)
    
    def on_focus_pause_clicked(self):
        # todo: change start and pause interactively
        self.timer.pause()
    
    def on_focus_stop_clicked(self):
        self.timer.stop()

    def on_focus_reset_clicked(self):
        self.timer.reset()
        self.update_timer_and_display()
    
    # todo: deal with the transparency LAAAATER
    def _hide_timer_widget_clean(self):
        self.timer_widget.hide()
        self.setAttribute(Qt.WA_TranslucentBackground, False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.update()

    def update_timer_and_display(self):
        if self.timer is None:
            return
        
        if self.timer.is_running:
            self.timer.tick()
            self.timer_label.setText(self.timer.get_display_time())
        elif self.timer.is_completed:
            self.timer_widget.hide()
            self.clock.stop()
            self.timer.reset()
            self.pet.increase_growth(10)
            self.update_stats_display()
            print("🎉 Focus complete! Pet growth increased!")
        else:
            self.clock.stop()
            print("Timer paused or stopped, clock stopped")
            self.timer_label.setText(self.timer.get_display_time())

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