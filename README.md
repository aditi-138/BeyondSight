# Beyond Sight

An AI-powered assistive application for visually impaired individuals

## 📌 Overview
Beyond Sight is an AI-led application designed to assist visually impaired individuals with daily activities through voice-guided navigation, object detection, facial recognition, and auditive assistance. The application integrates machine learning models for real-time object detection, facial and expression recognition, and text-to-speech conversion using Google Cloud TTS.

## ✨ Features
Voice-Guided Navigation: Provides real-time audio guidance for movement.

Object Detection: Identifies objects in the environment and describes them to the user.

Facial Recognition: Detects and recognizes faces from a stored database.

Text-to-Speech (TTS) Integration: Converts on-screen text to speech for accessibility.

CSV Database for Face Recognition: Stores names, contact numbers, and images for personalized interactions.

## 🛠️ Installation
Prerequisites
Ensure you have the following installed:

Python 3.12

OpenCV (cv2)

TensorFlow & Keras

Google Cloud Text-to-Speech API

Flask (if using a web interface)

## Setup
Clone the repository:

git clone https://github.com/your-username/BeyondSight.git
cd BeyondSight
Install dependencies:

pip install -r requirements.txt
Set up Google Cloud Text-to-Speech:

Create a Google Cloud account and enable TTS API.

Download the service account JSON key and set the environment variable:

export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-file.json"
Run the application:

python main_webcam.py
## 🚀 Usage
Launch the application and follow the voice commands.

Hold the camera in front of objects or faces to get real-time descriptions.

Use voice input for interaction.


## 🤝 Contributing
Contributions are welcome! Follow these steps:

Fork the repository.

Create a new branch: git checkout -b feature-branch

Commit your changes: git commit -m "Add new feature"

Push to the branch: git push origin feature-branch

Open a Pull Request.

## 📜 License
This project is licensed under the MIT License.

📧 Contact
For any queries, reach out at: aditighosh138@gmail.com

