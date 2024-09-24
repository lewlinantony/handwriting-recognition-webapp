# Handwritten Text Recognition Web App

This web application uses Flask as the backend framework and Tesseract OCR to convert handwritten text from an HTML canvas into digital text.

## Features

- Draw handwritten text on a canvas using the web interface.
- Convert the handwritten text to digital text using Tesseract OCR.
- Responsive web design.
- Easy-to-use interface.

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS, JavaScript (with canvas support)
- **OCR Engine**: Tesseract OCR
- **Others**: Bootstrap for styling, Jinja2 for templating

## Prerequisites

To run this application, you'll need to have the following installed:

- Python 3.x
- Flask
- Tesseract OCR
- OpenCV (for image processing)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/handwritten-text-recognition-webapp.git
    cd handwritten-text-recognition-webapp
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # For Linux/macOS
    venv\Scripts\activate      # For Windows
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Install Tesseract OCR**:
    - For **Windows**: [Download Tesseract Installer](https://github.com/tesseract-ocr/tesseract)
    - For **macOS**: Use Homebrew
      ```bash
      brew install tesseract
      ```
    - For **Linux**:
      ```bash
      sudo apt-get install tesseract-ocr
      ```

5. **Run the application**:
    ```bash
    flask run
    ```

6. Open your browser and navigate to `http://127.0.0.1:5000`.


## Future Enhancements

- Implement different font styles or colors for drawing.
- Improve OCR accuracy with custom Tesseract training.
- Add support for multiple languages.

## Acknowledgements

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Flask Framework
