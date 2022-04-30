"""
Firstly install some file.....
       1. pip install SpeechRecognition
       2. pip install pyttsx3
       3. pip install PyAudio  [install problem but pyaudio wheel file download and install]
                        link :  https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
                        download : PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl    [For Python v-3.9.2]
                                        then
            1. pip install pipwin  [Firstly]
            2. pipwin install pyAudio [Seceondly]

       4. pip install pywhatkit
       5. pip install flask
       6. pip install pywikipedia
       7. pip install pyjokes
"""
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import os

listener = sr.Recognizer()
Shereyase = pyttsx3.init('sapi5')
voices = Shereyase.getProperty('voices')
Shereyase.setProperty('voice', voices[1].id)


def speak(audio):
    Shereyase.say(audio)
    print(audio)
    Shereyase.runAndWait()

def talkCommand():
    r = sr.Recognizer()
    with sr.Microphone() as  source:
        print("Listening.................")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=10,phrase_time_limit=10)
        try:
            print("Recognizer...........")
            query = r.recognize_google(audio,language='en-in')
            print(f"User Said : {query}\n")
        except Exception as e:
            #speak("Unable to recognize your voice.......")
            return "None"
        return query


def username():
    speak("What Should i call you sir ?")
    uname = talkCommand()
    speak("Welcome Mister " + uname)
    speak("How Can I Help You Sir ?")



def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evenning Sir")
    speak("I am your Partner Sereyase")


if __name__ == "__main__":
    wishme()
    username()
    while True:
        order = talkCommand().lower()

        if "how are you" in order:
            speak("i am fine sir Thank you.")
            speak("how are you sir?")

        elif "I am fine" in order or "good" in order or "best" in order:
            speak("It is good to know that you are fine")

        elif "no fine" in order or "not fine" in order:
            speak("What happened to you sir?")

        elif "many problem" in order:
            speak("oh. Thats Sir...")
            speak("Sir can I know your problem")

        elif "who i am" in order:
            speak("If you can talk then surely you are a human")

        elif "i love you" in order:
            speak("Sir ! you are a funny man")

        elif "will you merry me" in order or 'will you marry me' in order or 'merry me' in order or 'marry me' in order:
            speak("Sorry sir . i am engaged with prothes")

        elif "love" in order:
            speak("It is the 7th sense that destroy all other senses")

        elif "who are you" in order:
            speak("I am partner of prothes")

        elif "what is your name" in order:
            speak("my name is shereyase madhu shampa")

        elif "what class are you read in" in order or "what class are you reading" in order:
            speak("Sir i read in BSE in CSE")
            speak("Sir what do you do?")

        elif "i am doing" in order or "i do" in order or "i was doing" in order:
            speak("Good sir.")

        elif "tell me about" in order or 'about' in order:
            look_for = order.replace("tell me about",'')
            info = wikipedia.summary(look_for,10)
            speak(info)

        elif "joke" in order or 'tell me jokes' in order:
            speak(pyjokes.get_joke())


        elif ''  or 'peyara' in order:
            speak("")


        elif "play" in order or "playing" in order:
            song = order.replace("play",'')
            speak('play' + song)
            pywhatkit.playonyt(song)


        elif "open notepad" in order:
            npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
            os.startfile(npath)



        elif "kutta" in order or 'dog' in order:
            speak('Sir You are big cow')

        elif 'bokachoda' in order:
            speak('Sorry sir ! You are very Bad')

        elif 'may khabar deyh nah' in order or "maay khabar dena" in order or "my khabar dena" in order:
            speak("sir apni onnek Olos Tai Khabar Deyh nah")

        elif "Thank you" in order or 'no thanks' in order or 'thank' in order:
            speak("wellcome sir")

        else:
            speak("sir i do not understand your speak")
            speak('sir please tell me again')
            speak("please sir kisu bolen...")

speak("sir thank you")