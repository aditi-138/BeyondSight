# test_speech.py
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty("rate", 150)  # Speed of speech
engine.setProperty("volume", 1.0)  # Volume (0.0 to 1.0)

def speak(text):
    """Convert text to speech and play the audio"""
    engine.say(text)
    engine.runAndWait()

# Test the speak function
speak("Hello, this is a test of the speech system.")

