import pyttsx3 
import speech_recognition as sr 
import datetime
import webbrowser
import calendar 
import os
import pyjokes
import operator
import wikipedia 
import requests  
import pywhatkit as kt
from bs4 import BeautifulSoup 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()  

def calculate(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        'X' : operator.mul,
        'divided' : operator.__truediv__,
        'mod' : operator.mod,
        '^': operator.xor, 
    } [op] 

def evaluate(op1,op2,op3):
    op1,op3 = int(op1),int(op3)
    return calculate(op2)(op1,op3) 


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!") 
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!") 
        speak("Good Afternoon!")   

    else:
        print("Good Evening!") 
        speak("Good Evening!")  

    print("I am your Virtual Assistant. Please tell me how can I help you ? ") 
    speak("I am your Virtual Assistant. Please tell me how can I help you ? ")   


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please")  
        speak("Say that again please") 
        return "None"

    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'open youtube' in query:
            speak("opening Youtube")
            webbrowser.open("youtube.com")
            input("Press Enter to ccontinue...") 
        
        elif 'exit' in query:
            exit()

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
            input("Press Enter to continue...") 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(f"Sir, the time is {strTime}")    
            speak(f"Sir, the time is {strTime}")
            input("Press Enter to continue...") 

        elif 'open code' in query:
            speak("opening VS Code")
            codePath = "D:\Microsoft VS Code"
            os.startfile(codePath) 
            input("Press Enter to continue...") 
        
        elif 'tell me a joke' in query:
            joke  = pyjokes.get_joke()
            print(joke)  
            speak(joke) 
            input("Press Enter to continue...") 

        elif 'wikipedia' in query :
            speak("searching wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 3) 
            speak("According to wikipedia")
            print(results) 
            speak(results) 
            input("Press Enter to continue...") 

        elif 'calculate' in query :
            try:
                print("What will I calculate") 
                speak("What will I calculate") 
                cal = takeCommand()
                print(f'{cal} = ')
                print(evaluate(*(cal.split())))
                speak(f'{cal} is ')
                speak(evaluate(*(cal.split()))) 

            except Exception as e:
                print("I am not sure I understand")
                speak("I am not sure I understand")  

            input("Press Enter to continue...")     
        
        elif 'search google' in query:
            print("What do I search") 
            speak("What do I search") 
            try:
                question = takeCommand() 
                speak("Searching google") 
                kt.search(question) 
            except Exception as e:
                print("I am not sure I understand") 
                speak("I am not sure I understand") 
            
            input("Press Enter to continue...") 

        elif 'tell me weather' in query :
            print("tell me the name of the city") 
            speak("tell me the name of the city")
            city = takeCommand()
            API_KEY = "350bffaa04018e6a5fd55fce3220d8a4" 
            API_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}" 
            response = requests.get(API_URL) 
            x = response.json() 
            if x["cod"] != "404" :
                y = x["main"]
                cur_temp = y["temp"]
                cur_pre = y["pressure"] 
                cur_hum = y["humidity"] 
                z = x["weather"] 
                weather_description = z[0]["description"] 
                print(f"The temperature is {str(cur_temp)} and pressure is {str(cur_pre)} and humidity is {str(cur_hum)} and the weather is {str(weather_description)}") 
                speak(f"The temperature is {str(cur_temp)} and pressure is {str(cur_pre)} and humidity is {str(cur_hum)} and the weather is {str(weather_description)}") 
            else:
                print("city not found")
                speak("city not found") 
            
            input("Press Enter to continue...") 

        elif 'news headlines' in query :
            URL = "https://timesofindia.indiatimes.com/india/timestopten.cms" 
            page = requests.get(URL) 

            soup = BeautifulSoup(page.text,"lxml")  
            news = soup.find_all('a',class_="news_title")   

            for i in news:
                print(i.text) 
                speak(i.text)     
            
            input("Press Enter to continue...") 

        elif 'take notes' in query:
            speak("Go ahead")
            note = takeCommand() 
            with open ("file.txt","a") as fp:
                fp.write(note) 
            
            input("Press Enter to continue...") 
        
        elif 'show notes' in query:
            with open("file.txt","r") as fp:
                data = fp.read() 
                print(data)
                speak(data) 
            
            input("Press Enter to continue...") 

        elif 'play music' in query:
            music_folder = r"C:\Users\Lenovo\OneDrive\Desktop\song"
            songs = os.listdir(music_folder)
            play = os.startfile(os.path.join(music_folder, songs[2])) 
            input("Press Enter to continue...") 
         
        elif 'date today' in query:
            now_date = datetime.datetime.now()
            date = now_date.strftime("%A %d %B %y") 
            print(f"Today's date is {date}") 
            speak(f"Today's date is {date}") 
            input("Press Enter to continue...") 

        elif 'open notepad' in query:
            speak("opening notepad") 
            os.startfile("Notepad")  
            input("Press Enter to continue...")     

        elif 'show calendar' in query:
            now = datetime.datetime.now() 
            mont = now.strftime("%m")
            mon = int(mont) 
            print(calendar.month(2022,mon)) 
            input("Press Enter to continue...")    

        