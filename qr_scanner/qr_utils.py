# This module contains functions for QR and barcode detection and display.
import cv2
from pyzbar import pyzbar
import numpy as np


def detect_codes(frame):
    """
    Detect and decode QR codes and barcodes in the given frame.
    Args:
        frame (numpy.ndarray): The video frame.
    Returns:
        codes (list): List of detected code objects with type, data, and bounding box.
    """
    decoded_objects = pyzbar.decode(frame)
    codes = []
    for obj in decoded_objects:
        code = {
            'type': obj.type,
            'data': obj.data.decode('utf-8', errors='replace'),
            'rect': obj.rect,
            'polygon': obj.polygon
        }
        codes.append(code)
    return codes


def display_results(frame, codes):
    """
    Draw rectangles and display decoded text for each detected code on the frame.
    Args:
        frame (numpy.ndarray): The video frame.
        codes (list): List of detected code objects.
    Returns:
        frame (numpy.ndarray): The frame with drawings and labels.
    """
    for code in codes:
        # Draw polygon if available, else use rect
        pts = code['polygon']
        if pts and len(pts) > 3:
            pts = [(pt.x, pt.y) for pt in pts]
            pts = cv2.convexHull(np.array(pts, dtype=np.int32))
            cv2.polylines(frame, [pts], isClosed=True, color=(0, 255, 0), thickness=2)
        else:
            x, y, w, h = code['rect']
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Prepare label
        label = f"{code['type']}: {code['data']}"
        x, y, w, h = code['rect']
        # Draw label background
        (text_width, text_height), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
        cv2.rectangle(frame, (x, y - text_height - baseline - 4), (x + text_width, y), (0, 255, 0), cv2.FILLED)
        # Put label text
        cv2.putText(frame, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
    return frame
