import pyttsx3
import datetime
import webbrowser
import wikipedia
import speech_recognition as sr
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")  

    speak("I am Jarvis, You're welcome to my computer, How can I help you ?")   


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source) 

    try:    
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as query:
        print("Say it again Please.....")
        return "None"
    return query

if __name__=="__main__" :
    wishMe()
    
    while True:
        query = takeCommand().lower() 


        if 'wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("wikipedia", "") 
            abc = wikipedia.summary(query,sentences = 3)
            speak("Acording to Wikipedia")
            print(abc)
            speak(abc)


        elif 'open youtube' in query:
            speak("Okay")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Okay")
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            speak("Okay")
            webbrowser.open("gmail.com")           

        elif 'open whatsapp' in query:
            speak("Okay")
            webbrowser.open("web.whatsapp.com")       

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open vs code' in query:
            codepath = "C:\\Users\\Indu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Okay")
            os.startfile(codepath)

        elif 'open brave' in query:
            path = "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            speak("Okay")
            os.startfile(path) 


        elif 'open minecraft' in query:
            path = "C:\\Users\\Indu\\Desktop\\Nonu and Shona\\Minecraft\\.minecraft\\Launcher.exe"
            speak("Okay")
            os.startfile(path)   