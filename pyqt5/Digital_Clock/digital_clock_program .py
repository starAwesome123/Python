# PyQt5
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import Qt, QTimer,QTime
from PyQt5.QtGui import QFont, QFontDatabase, QIcon
import sys


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digital Clock")
        self.time_label=QLabel(self)
        self.timer=QTimer(self)

# Load the window icon with error handling
        try:
            self.setWindowIcon(QIcon("OIP.jpg"))
        except Exception as e:
            print(f"Warning: Could not load window icon 'OIP.jpg'. Error: {e}")
         


        
        
        self.initUT()


    def initUT(self):
        # Set the geometry of the window
        self.setGeometry(0, 0, 500, 300)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        try:
            font_id = QFontDatabase.addApplicationFont("DIGITALDREAM.ttf")
            if font_id != -1:
                font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
                my_font = QFont(font_family, 90)
                self.time_label.setFont(my_font)
                self.time_label.setStyleSheet("color: green; background-color: black;")
            else:
                print("Warning: Could not load custom font. Falling back to default.")
                self.time_label.setStyleSheet("font-family: Arial; font-size: 90px; color: green; background-color: black;")
        except Exception as e:
            print(f"Error loading font: {e}. Falling back to default.")
            self.time_label.setStyleSheet("font-family: Arial; font-size: 90px; color: green; background-color: black;")
        

        self.setStyleSheet("background-color: black;")

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()


    def update_time(self):
        current_time=QTime.currentTime().toString("hh:mm:ss") #for pm/am add AP IN THE string
        self.time_label.setText(current_time)


def main():
    app=QApplication(sys.argv)
    clock=DigitalClock()
    clock.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()
