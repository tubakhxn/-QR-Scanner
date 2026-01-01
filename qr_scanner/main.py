"""
main.py - Real-Time QR and Barcode Scanner

This script captures live video from the webcam, detects QR codes and barcodes in real-time using OpenCV and Pyzbar,
decodes their data, and displays the results on the video feed with rectangles and labels.

Author: Tuba Khan
Date: 2025-12-31
"""


import cv2
import sys
from qr_utils import detect_codes, display_results


def start_camera(camera_index=0):
    """
    Initialize and return the video capture object.
    Args:
        camera_index (int): Index of the camera (default 0).
    Returns:
        cap (cv2.VideoCapture): Video capture object.
    Raises:
        SystemExit: If the camera cannot be opened.
    """
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        sys.exit(1)
    return cap



def main():
    import webbrowser
    cap = start_camera()
    print("Press 'q' to exit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame from camera.")
            break
        codes = detect_codes(frame)
        # Check for URLs and open in browser every time detected
        for code in codes:
            data = code['data']
            if data.startswith('http://') or data.startswith('https://'):
                print(f"Opening URL: {data}")
                webbrowser.open(data)
        frame = display_results(frame, codes)
        cv2.imshow('QR & Barcode Scanner', frame)
        # Exit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Unexpected error: {e}")
        cv2.destroyAllWindows()
        sys.exit(1)
