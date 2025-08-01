# PyQt5 Weather App ☀️

A simple and elegant desktop application built with PyQt5 and the OpenWeatherMap API to get real-time weather information for any city in the world.

## ✨ Features

* **Real-time Weather Data:** Get temperature, weather description, and a corresponding emoji.

* **Modern UI:** A clean, stylish interface with dynamic resizing.

* **Robust Error Handling:** Alerts the user to common issues like network errors or city not found.

## 🛠️ Installation

### Prerequisites

* Python 3.6 or higher

* An API key from [OpenWeatherMap](https://openweathermap.org/api)

### Steps

1. **Clone the repository:**

   ```
   git clone https://github.com/starAwesome123/Python/edit/main/pyqt5/weather%20app
   ```

2. **Install the required libraries:**

   ```
   pip install PyQt5
   ```

   This will install `PyQt5` and `requests`.

3. **Set your API key as an environment variable:**
   For security, the API key is not stored in the code. You must set it as an environment variable named `OPENWEATHER_API_KEY`.

   **On Windows:**

   ```
   set OPENWEATHER_API_KEY=YOUR_API_KEY
   ```

   **On macOS and Linux:**

   ```
   export OPENWEATHER_API_KEY="YOUR_API_KEY"
   ```

   Replace `YOUR_API_KEY` with the key you obtained from OpenWeatherMap.

## 🚀 Usage

Run the application from your terminal:

```
python main.py
```

The app window will open. Simply type a city name into the input box and click "Get Weather" to see the current conditions.

## 📁 Project Structure

```
pyqt5-weather-app/
├── main.py               # The main application code
├── weather.png           # The application window icon
├── requirements.txt      # List of project dependencies
└── README.md             # This file
```

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
