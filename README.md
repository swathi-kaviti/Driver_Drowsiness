# Driver_Drowsiness Detection System

### Overview

This project is a real-time driver drowsiness detection system using computer vision and deep learning. It continuously monitors a driver's face through a webcam, detects the eyes' state (open or closed) using a Convolutional Neural Network (CNN), and triggers an alarm if the driver appears drowsy for a prolonged period.

### Features

**Real-Time Eye Detection:** Utilizes Haar Cascade classifiers to detect face and eyes.
**Deep Learning Model:** A CNN trained on eye images to classify whether eyes are open or closed.
**Drowsiness Detection:** Calculates a score based on eye states and sounds an alarm if the score exceeds a threshold.
**Alarm System:** A sound alert warns the driver to wake up when drowsiness is detected.
**Live Video Feed:** Displays live video with real-time annotations for face, eyes, and drowsiness status.

### Tech Stack

Python (OpenCV, NumPy, Keras, TensorFlow)
**Deep Learning:** Convolutional Neural Networks (CNN)
**Audio Handling:** Pygame Mixer
**Image Preprocessing:** Grayscale conversion, normalization, and resizing

### How It Works

**Model Training:**
The model.py script trains a CNN on images of open and closed eyes.
It uses image augmentation and rescaling for better generalization.
The final model is saved as cnnCat2.h5.

**Real-Time Detection:**
drowsiness_detection.py captures live video from the webcam.
Detects the driver’s face and eyes using Haar Cascade classifiers.
Classifies eye states (open or closed) with the trained CNN.
Tracks drowsiness score and plays an alarm if eyes remain closed for too long.

### Future Improvements:

Add head pose estimation for more accurate drowsiness detection.
Integrate with IoT devices for car automation.
Use a more complex CNN or transfer learning for better accuracy.

### Acknowledgments

Haar Cascade Classifiers (OpenCV)
Keras & TensorFlow for deep learning
