import speech_recognition as sr
import datetime
import os
import shutil
import pyttsx3
import pyaudio
import wikipedia
import webbrowser

# Initialize pyttsx3 for text-to-speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set voice to female voice

# Function to make Jarvis speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to wish the user based on the time of day
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("Hello, I am Jarvis. How may I help you?")

# Function to display and speak username
def username():
    uname = "Sahil Namdeo"
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    print("################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("################".center(columns))
    speak("How can I help you, Sir?")

# Function to take voice input from the microphone
def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Could you repeat?")
        return "None"
    return query

# Main function
if __name__ == "__main__":
    wishme()
    username()

    while True:
        query = takeCommand().lower()

        # Logic for different commands

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")

        elif 'open whatsapp' in query:
            speak("Opening whatsapp")
            webbrowser.open("whatsapp.com")


        elif 'open website' in query:
            speak("Opening website")
            webbrowser.open(" https://pehchan-patra.s3.amazonaws.com/portfolio/portfolio.html")


        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'quit' in query or 'exit' in query:
            speak("Goodbye Sir, have a nice day!")
            break

        # You can add more commands as needed
