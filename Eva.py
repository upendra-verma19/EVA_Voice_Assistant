import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
import time
import json
import pyjokes





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)
voicerate = 193
engine.setProperty('rate', voicerate)


def speak(audio):

    engine.say(audio)
    engine.runAndWait()


def wishMe():

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir ! , how can i help you")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir ! , how can i help you")

    else:
        speak("Good Evening sir ! , how can i help  you")


def takecommand():
    #it takes microphone input from the user and returns strings output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening....")
        audio = r.listen(source, timeout=5)
        r.pause_threshold = 1

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        #print(e)

        print("Say that again please.....")

        return "None"

    return query


if __name__ == "__main__":
    wishMe()
    crpath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s" #Location for chrome

    while True:

        #If you want your results to persist in your commandline then remove thesr 2 lines of code
        clear = lambda: os.system('cls') 
        clear()


        query = takecommand().lower()



        # Surfing the net
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

            
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.get(crpath).open("http://youtube.com")
        

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.get(crpath).open("http://google.com")

        elif 'search' in query or 'google' in query:
            query = query.replace("search", "")
            query = query.replace("google", "")
            url = "https://www.google.co.in/search?q=" + (str(query)) + "&oq="+(str(query))+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
            webbrowser.get(crpath).open(url)
            


        #File Dir
        elif 'open disk c' in query:
            Cpath = "C:\\"
            os.startfile(Cpath)

        elif 'open disk d' in query:
            Dpath = 'D:\\'  
            os.startfile(Dpath)

        elif 'open disk e' in query:
            Epath = "E:\\"
            os.startfile(Epath)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'Telegram Desktop' in query or 'open telegram' in query:
            Telegrampath = "C:\\Telegram Desktop\\Telegram.exe"
            os.startfile(Telegrampath)



        # Casual talks
        elif "can you die" in query or " you die" in query:
             speak("may be, if my creator wants to ")

        elif "when do you sleep" in query or "do you sleep" in query :
             speak("sleep is not my kind of thing, sir!")

        elif "good moring" in query or " good morning" in query :
             speak ("good morning sir !")

        elif "good evening" in query or "good evening" in query:
             speak("good evening sir !")

        elif " good afternoon" in query or " good afternoon" in query:
             speak (" good afternoon sir !") 

        elif "good night" in query:
             speak("good night sir , have a good sleep !")
             exit()

        elif "tell me your name" in query:
            print("I am Eva. Your deskstop Assistant")
            speak("I am Eva. Your deskstop Assistant")



        # Commanding to do something
        elif 'play music' in query or "play song" in query:
            speak("Here you go with songs")
            music_dir = 'D:\\Songs'                              #Change the directory
            songs = os.listdir(music_dir)
            random = os.startfile(os.path.join(music_dir, songs[1]))
        
        elif "shutdown the computer" in query or "switch off the computer" in query or "shutdown" in query:
            speak("Do you want to shutdown your computer sir ?")
            while True:
                command = takecommand()
                if "no" in command:
                    speak("thak u sir i will not shutdown the system ")
                    break

                if "yes" in command:
                    command.speak("shutting the computer")
                    os.system("shutdown /s /t 30")
                    speak("ok sir ! i shutdown the computer")
                    break


        elif 'joke' in query:
            speak(pyjokes.get_joke())


        elif "write a note" in query:
            speak("What should i write, sir")
            note = takecommand()
            file = open('notes.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)


        elif "show note" in query:
            speak("Showing Notes")
            file = open("notes.txt", "r") 
            print(file.read())
            speak(file.read(6))
            

        # this will exit and terminate the program
        elif "bye" in query or "eva bye" in query or " talk to u later " in query or "offline" in query:
            speak("See you soon again ")
            exit()

        time.sleep(3)
