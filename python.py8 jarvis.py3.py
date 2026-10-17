import datetime
import os
import webbrowser
import random
import speech_recognition as sr  # type: ignore
import pyttsx3 # type: ignore
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def greet():
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if hour < 10:
        speak("Good morning!")
    elif 1 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, I couldn't reach the speech recognition service.")
        return ""

def execute_command(command):
    if "open" in command: 
        open_website(command)
    elif "time" in command:
        tell_time()
    elif "hello jarvis" in command or "hi jarvis" in command:
        greet("")
    elif "random number" in command:
        generate_random_number()
    elif "exit" in command or "bye" in command:
        exit_jarvis()
    else:
        speak("I'm sorry, I can't perform that task.")

def open_website(command):
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "stackoverflow": "https://stackoverflow.com",
    }

    for key in websites:
        if key in command:
            webbrowser.open(websites[key])
            break
    else:
        speak("I'm sorry, I don't know how to open that website.")

def tell_time():
    current_time = datetime.datetime.now()
    time_str = current_time.strftime("%H:%M:%S")
    speak("The current time is: " + time_str)

def generate_random_number():
    number = random.randint(1, 100)
    speak("Random number: " + str(number))

def exit_jarvis():
    speak("Goodbye!")
    exit()

if __name__ == "__main__":
    greet()

    while True:
        speak("How can I assist you?")
        command = listen()
        execute_command(command)
