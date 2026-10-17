# JARVIS – Python Voice Assistant

A Python-based voice-controlled virtual assistant inspired by JARVIS. It listens to voice commands and responds using speech synthesis to perform simple tasks.

## Features
- **Voice Recognition:** Recognizes spoken commands using SpeechRecognition.
- **Voice Responses:** Speaks responses using pyttsx3.
- **Website Launcher:** Opens supported websites such as Google, YouTube, and Stack Overflow.
- **Time Announcement:** Announces the current time.
- **Random Number Generator:** Generates a random number between 1 and 100.
- **Voice Greetings:** Provides greetings based on the time of day.
- **Exit Command:** Stops the assistant when you say "exit" or "bye".

## Technologies Used
- Python
- SpeechRecognition
- PyAudio (microphone input dependency, if required by your setup)
- pyttsx3
- datetime, webbrowser, random

## Installation

Install the required Python libraries:

```bash
pip install SpeechRecognition pyttsx3 pyaudio
```

## Run the Project

```bash
python jarvis.py
```

Use your microphone to speak commands such as:
- "Open Google"
- "Open YouTube"
- "What is the time?"
- "Generate random number"
- "Bye"

## Learning Objectives
This project demonstrates Python functions, conditional statements, loops, speech recognition, text-to-speech, and basic task automation.

## Future Improvements
- Add more voice commands and website support.
- Integrate an AI-powered conversational interface.
- Add application launching and system controls.
- Improve error handling and command recognition.

## Disclaimer
This is a beginner-level virtual assistant project. Its capabilities are limited to the commands implemented in the source code.
