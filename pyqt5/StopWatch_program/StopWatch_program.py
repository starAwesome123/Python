# PyQt5
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QVBoxLayout, QPushButton, QHBoxLayout)
from PyQt5.QtCore import Qt, QTimer, QTime

class StopWatch(QWidget):
    """
    A simple digital stopwatch application with start, stop, and reset functionality.
    This version includes a clean layout and visual feedback for button states.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stop Watch")
        
        # Initialize instance variables
        self.time = QTime(0, 0, 0, 0)
        self.is_running = False
        
        # Initialize UI elements
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        
        # Initialize the user interface
        self.init_ui()

    def init_ui(self):
        """
        Sets up the application's layout, styling, and signal-slot connections.
        """
        # Set a fixed size for the window
        self.setFixedSize(500, 300)
        
        # Create main vertical layout
        main_vbox = QVBoxLayout()
        main_vbox.addWidget(self.time_label, alignment=Qt.AlignCenter)

        # Create a horizontal layout for the buttons
        button_hbox = QHBoxLayout()
        button_hbox.addWidget(self.start_button)
        button_hbox.addWidget(self.stop_button)
        button_hbox.addWidget(self.reset_button)
        
        # Add the button layout to the main vertical layout
        main_vbox.addLayout(button_hbox)
        self.setLayout(main_vbox)

        # --- Initial Button State ---
        # Stop and Reset buttons are initially disabled because the timer isn't running.
        self.stop_button.setDisabled(True)
        self.reset_button.setDisabled(True)

        # --- Styling ---
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f4f8;
            }
            QLabel {
                font-family: 'Courier New', Courier, monospace;
                font-size: 70px;
                font-weight: bold;
                color: #2c3e50;
            }
            QPushButton {
                font-family: Arial;
                font-size: 24px;
                font-weight: bold;
                padding: 10px 20px;
                border-radius: 5px;
                border: none;
                color: white;
            }
            #start_button { background-color: #27ae60; }
            #start_button:hover { background-color: #229954; }
            #start_button:disabled { background-color: #81c784; }
            
            #stop_button { background-color: #e74c3c; }
            #stop_button:hover { background-color: #c0392b; }
            #stop_button:disabled { background-color: #e57373; }
            
            #reset_button { background-color: #3498db; }
            #reset_button:hover { background-color: #2980b9; }
            #reset_button:disabled { background-color: #64b5f6; }
        """)

        # Set object names for targeted styling
        self.start_button.setObjectName("start_button")
        self.stop_button.setObjectName("stop_button")
        self.reset_button.setObjectName("reset_button")

        # --- Signal-Slot Connections ---
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_time)

    def start(self):
        """Starts the timer and updates button states."""
        if not self.is_running:
            self.timer.start(10)
            self.is_running = True
            self.start_button.setDisabled(True)
            self.stop_button.setDisabled(False)
            self.reset_button.setDisabled(False)

    def stop(self):
        """Stops the timer and updates button states."""
        if self.is_running:
            self.timer.stop()
            self.is_running = False
            self.start_button.setDisabled(False)
            self.stop_button.setDisabled(True)

    def reset(self):
        """Resets the timer and updates button states."""
        self.timer.stop()
        self.is_running = False
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))
        self.start_button.setDisabled(False)
        self.stop_button.setDisabled(True)
        self.reset_button.setDisabled(True)
    
    def update_time(self):
        """Updates the time every 10 milliseconds."""
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))
    
    def format_time(self, time):
        """Formats a QTime object into a string with milliseconds."""
        return time.toString("hh:mm:ss.zz")

def main():
    """Main function to run the application."""
    app = QApplication(sys.argv)
    clock = StopWatch()
    clock.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
