# PyQt5
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QVBoxLayout, QPushButton, QLineEdit, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import os # We'll use this to get the API key from an environment variable

class WeatherApp(QWidget):
    """
    A PyQt5 application that fetches and displays weather information for a given city.
    This version includes an icon, a clean layout, and best practices for security and style.
    """
    def __init__(self):
        super().__init__()
        
        # --- Application Initialization ---
        self.setWindowTitle("Weather App")
        
        # Set the window size and position once
        self.setGeometry(100, 100, 500, 500)
        
        # Load the window icon with error handling
        try:
            self.setWindowIcon(QIcon("weather.png"))
        except Exception as e:
            print(f"Warning: Could not load window icon 'weather.png'. Error: {e}")
            
        # --- UI Element Initialization ---
        self.city_label = QLabel("Enter city name", self)
        self.temp_label = QLabel(" ", self)
        self.emoji_label = QLabel(self) 
        self.desc_label = QLabel(self)
        self.city_input = QLineEdit(self)
        self.weather_button = QPushButton("Get Weather", self)

        # IMPORTANT: Replace 'YOUR_API_KEY' with your actual key from OpenWeather.
        self.api_key = 'OPENWEATHER_API_KEY'  # This should be set in your environment variables

        # --- Set up the user interface ---
        self.init_ui()

    def init_ui(self):
        """
        Sets up the layout and styling of the application's user interface.
        """
        vbox = QVBoxLayout()
        
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.desc_label)
        vbox.addWidget(self.weather_button)

        self.setLayout(vbox)

        # Align all widgets to the center
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.desc_label.setAlignment(Qt.AlignCenter)

        # Assign object names for targeted styling
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.desc_label.setObjectName("desc_label")
        self.weather_button.setObjectName("weather_button")

        self.setStyleSheet("""
            QWidget {
                background-color: #f0f4f8; /* A light, modern background color */
            }
            QLabel, QLineEdit, QPushButton {
                font-family: Arial;
                color: #2c3e50; /* A dark, professional text color */
                text-align: center;
                padding: 5px;
                border-radius: 5px;
            }
            QLabel#city_label {
                font-size: 30px;
                font-weight: bold;
            }
            QPushButton#weather_button {
                font-size: 24px;
                font-weight: bold;
                background-color: #3498db;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                margin-top: 15px;
            }
            QPushButton#weather_button:hover {
                background-color: #2980b9;
            }
            QLineEdit#city_input{
                font-size: 24px;
                padding: 8px;
                border: 1px solid #bdc3c7; /* A subtle border color */
            }
            QLabel#emoji_label {
                font-size: 75px;
            }
            QLabel#temp_label {
                font-size: 60px;
                font-weight: bold;
            }
            QLabel#desc_label {
                font-size: 40px;
                font-style: italic;
            }
        """)
        
        # Connect the button to the get_weather function
        self.weather_button.clicked.connect(self.get_weather)
        
    def get_weather(self):
        """
        Fetches weather data from the OpenWeatherMap API.
        """
        # Check if the API key is set
        if not self.api_key:
            QMessageBox.critical(self, "Error", "API key not set. Please set the 'OPENWEATHER_API_KEY' environment variable.")
            return

        city = self.city_input.text()
        if not city:
            QMessageBox.warning(self, "Input Error", "Please enter a city name.")
            return
            
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        
        try: 
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if data["cod"] == 200:
                self.display_weather(data)
            else:
                self.display_error(f"Error: {data.get('message', 'An unknown error occurred')}")

        except requests.exceptions.HTTPError as http_error:
            self.display_error(f"HTTP Error: {http_error.response.status_code} - {http_error.response.reason}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error: Check your internet connection.")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error: The request timed out.")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error: {req_error}")

    def display_error(self, message):
        """
        Displays an error message using a QMessageBox for a better user experience.
        """
        QMessageBox.critical(self, "Error", message)
        self.temp_label.clear()
        self.emoji_label.clear()
        self.desc_label.clear()

    def display_weather(self, data):
        """
        Updates the UI with the fetched weather data.
        """
        temp_c = data['main']['temp']
        weather = data['weather'][0]['description']
        weather_id = data['weather'][0]['id']

        self.temp_label.setText(f"{temp_c:.02f}°C")
        self.desc_label.setText(weather.title())
        self.emoji_label.setText(self.get_weather_emoji(weather_id))

    @staticmethod
    def get_weather_emoji(weather_id):
        """
        Returns a weather emoji based on the OpenWeatherMap weather ID.
        """
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id < 321:
            return "🌦️"
        elif 500 <= weather_id < 531:
            return "🌧️"
        elif 600 <= weather_id < 622:
            return "🌨️❄️"
        elif 701 <= weather_id < 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪"
        elif weather_id == 800:
            return "🌞"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""

def main():
    """
    Main function to run the application.
    """
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

