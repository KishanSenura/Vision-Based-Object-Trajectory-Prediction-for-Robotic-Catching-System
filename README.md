# Vision-Based Object Trajectory Prediction for Robotic Catching System

## 📌 Project Overview
Developing a computer vision system to detect and track a thrown object in real time and predict its trajectory. The ultimate goal is to direct a robotic system to intercept the object at the predicted position. The current development phase focuses on establishing a robust foundation in core detection and tracking capabilities using OpenCV before integrating trajectory math and robotic control.

## 🚀 Core Tracking Capabilities
*   **Motion-Based Detection (`Object detection 2 .py`):** Implements real-time background subtraction (MOG2) to filter out static elements, applying morphological operations to reduce noise, and drawing bounding boxes around moving targets[cite: 1].
*   **Dynamic Template Matching (`Object detection.py`):** Utilizes multi-scale template matching (`cv.TM_SQDIFF_NORMED`) to localize and track specific objects in a live feed, dynamically adjusting for scale as the object's distance from the camera changes[cite: 2].

## 📂 Repository Structure & Explorations
Alongside the core tracking modules, this repository includes foundational computer vision experiments crucial for building out the robotic vision pipeline:

*   **`Conner.py`:** Feature tracking script that identifies prominent corners in grayscale using `cv2.goodFeaturesToTrack` and visualizes randomized line connections between them[cite: 3].
*   **`Face.py` & `Face1.py`:** Implements Haar Cascade Classifiers for real-time face and eye detection within specific regions of interest[cite: 5, 6].
*   **`Templet matching.py`:** Tests and compares multiple template matching algorithms (e.g., `TM_CCOEFF`, `TM_SQDIFF`) to find the optimal method for static image localization[cite: 7].
*   **`Color.py`:** Demonstrates real-time color isolation using HSV color space masking to track specific color profiles (e.g., blue objects)[cite: 9].
*   **`Camera.py`:** Manipulates active video captures by resizing, rotating 180 degrees, and mapping them into a 2x2 grid layout[cite: 8].
*   **`Draw.py`:** Displays geometric overlays, bounding boxes, and UI text rendering over active video frames[cite: 4].

## 🛠️ Prerequisites & Installation
To run the scripts in this repository, ensure you have Python installed along with the following dependencies:

```bash
pip install numpy opencv-python
