# Real-Time QR and Barcode Scanner

This project is a real-time QR and barcode scanner using OpenCV and Pyzbar. It captures live video from your webcam, detects and decodes QR codes and barcodes, and displays the results on the video feed.

## Features
- Real-time detection and decoding of QR codes and barcodes
- Handles multiple codes simultaneously
- Draws rectangles and displays decoded text above each code
- Clean exit by pressing 'q'
- Modular code structure
- Cross-platform: Works on Windows and Linux

## Requirements
- Python 3.7+
- OpenCV (`opencv-python`)
- Pyzbar

## Installation

1. (Recommended) Create a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/Mac:
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the scanner:
```bash
python main.py
```

Press 'q' to exit the scanner.

