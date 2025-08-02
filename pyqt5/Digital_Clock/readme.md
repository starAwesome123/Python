# ⏰ PyQt5 Digital Clock

A sleek and minimalist digital clock application built with Python and the PyQt5 framework. This project demonstrates essential GUI development, real-time event handling, and custom font integration.

## ✨ Features

- **Real-time Display:** The clock updates every second, showing the current time in `hh:mm:ss` format.
- **Custom Font:** The app uses a custom font, `DIGITALDREAM.ttf`, to create an authentic retro digital clock aesthetic.
- **Clean Interface:** A minimalist black and green theme provides excellent contrast and a modern feel.
- **Robustness:** Includes error handling to gracefully fall back to a default font if the custom font file or icon image are missing.

## 🛠️ Installation

### Prerequisites

- Python 3.6 or higher
- The PyQt5 library

### Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/starAwesome123/Python/tree/main/pyqt5/Digital_Clock
    ```

2.  **Install the required library:**
    This project only requires PyQt5. If you don't have it, you can install it using pip:
    ```bash
    pip install PyQt5
    ```

3.  **Add the custom font:**
    Ensure that the custom font file, `DIGITALDREAM.ttf`, is located in the same directory as the `main.py` script. The application is designed to function even if this file is not found, but the custom font will not be displayed.

## 🚀 Usage

To run the application, simply execute the Python script from your terminal:
```bash
python main.py
```

## 📁 Project Structure

```
.
├── main.py               # The main application code
├── DIGITALDREAM.ttf      # The custom font file
└── README.md             # This file
```

## 📄 License

This project is licensed under the MIT License.
