import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import wikipedia
import webbrowser
import random
import subprocess
import google.generativeai as genai
import google.generativeai as genai


#Logging Configuration
Log_Dir = "logs"
Log_Dir_Name = "application3.log"

os.makedirs(Log_Dir, exist_ok=True)
Log_path = os.path.join(Log_Dir,Log_Dir_Name)

logging.basicConfig(filename=Log_path,
                    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
                    level= logging.INFO)

# Activate voice system
# engin = pyttsx3.init("nsss")
# voices = engin.getProperty("voices")
# engin.setProperty('rate',170)
# engin.setProperty('voice',voices[0])

# This is speak function
def speak(text):
    """  this is function convert text to voice 
    Args: 
        test
        returns: voic """
    engin = pyttsx3.init("nsss")
    voices = engin.getProperty("voices")
    engin.setProperty('rate',170)
    engin.setProperty('voice',voices[0])  
    
    engin.say(text)
    engin.runAndWait() # after done cloase 

#speak("hello my name is jubayer")

# This function recognize the speech and convert it to text 

def takeCommand():
    """ This function 
    return : text  as query"""
     
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ....")
        r.pause_threshold = 1
        audio = r.listen(source)
# down laod handling
# now try to write logic
    try:
        print("Recognizig ....")
        query = r.recognize_google(audio, language = "en-in")
        print(f"User said : {query}\n")

    except Exception as e:
        logging.info(e)
        print("Say that again please ")
        return "None"
    
    return query
# ---- 

def greeting():
    hour = (datetime.datetime.now()).hour

    if hour >= 0 and hour <= 12:
        speak("Good Morning sir ! How are you doing")
    elif hour >=12 and hour <=18:
        speak("GOOd Afternoon Sir ! How are you doing ")
    else:
        speak(" Good Evening sir ! How are you doing ?")
    
    speak('I am Jarvis . please tell me how may i help you today')

## Generative Ai added 
def gemini_model_response(user_input):
    GEMINI_API_KEY = "AIzaSyDk05Hp2sS5Dq4MPMqnm4Rjw0aJoW7QAYQ"
    genai.configure(api_key=GEMINI_API_KEY)

# 2. Fixed spelling (GenerativeModel) and model version (1.5-flash)
#model = genai.GenerativeModel("gemini-1.5-flash")
    model = genai.GenerativeModel("gemini-2.5-flash")
    #user_input = "what is python"

    prompt = f"Answar the provied question in short, Question : {user_input}"

    respon = model.generate_content(prompt)
    result = respon.text

    return result


# music  function will be add later

def play_music():
    musi_dir ="/Volumes/study/A_data-science/Python/Python_Mac/M_project/music"





greeting()

while True:# for continue run
    query = takeCommand().lower()
    print(query)
    
    if "your name" in query:
        speak("My name is jarvis")
        logging.info("User asked for assistant's name. ")

    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        logging.info("user asked for current time")
        speak(f"sir the time is {strTime}")
   
    elif "saima" in query:
        speak("Sayema Hussain Johura is her full name")
    
    elif "jiha" in query:
        speak(" Jihan arafath is his full name ")

    elif "dubair" in query:
        speak(" Jubayer hussain is his full name ")
    
    elif "samsun" in query:
        speak(" Samsun nahar is his full name ")

   
# Small talk 
    elif "how are you" in query:
        speak(" I am functioning a full capacity sir !")
    
    elif "where are your from?" in query:
        speak(" I am from usa")

    elif "who made you" in query:
        speak( " i was created by Bappy sir , a brillant mind !")

    elif "thank you" in query:
        speak("It is my pleasure sir. Always happy to help . ")
        
    elif "House" in query:
        speak("My House number : 27654")
    
    elif "open google " in query:
        speak("Ok sir. Please type here what do you want to read")
        webbrowser.open("https://www.google.com")
        logging.info("Google browser is open")
    #calculaor
    elif "open calculator" in query or "calcuator" in query:
        speak("opeing calculator")
        subprocess.Popen(["open", "-a", "Calculator"])
    
    #Notepad
    elif "open notepade" in query:
        speak("Opening Notepad")
        subprocess.Popen(["open", "-a","TextEdit"])
    
    # commod prompt
    elif "open terminal " in query or "open cmd " in query:
        speak("opening command prompt terminal ")
        subprocess.Popen("cmd.exe")
    
    #terminal
    elif "open terminal" in query:
        subprocess.Popen(["open", "-a", "Terminal"])

    elif "open calendar" in query:
        webbrowser.open("https://calendar.google.com")

    elif "youtube" in query:
        txt = query.replace("youtube", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={txt}")
    
    # Open Facebook
    elif "open facebook" in query:
        webbrowser.open("https://facebook.com")

    # exit()
    elif "exit" in query:
        speak("Thank you for your time sir. Have a great day ahead!")
        logging.info("User exited the program.")
        exit()
    elif "open wikipedia" in query:
            pass
    
    # open github
    elif "open github" in query:
        webbrowser.open("https://github.com")

    # Joke 
    # elif "Joke" or "jokes" in query:
    #     jokes = [
    #         "Why don't programmers like nature? Too many bugs.",
    #         "I told my computer I needed a break. It said no problem, it will go to sleep.",
    #         "Why do Java developers wear glasses? Because they don't C sharp."
    #     ]
    #     speak(random.choice(jokes))
    #     logging.info("user request a joke")
    
    # wikipedia
    elif "wikipedia" in query:
        speak("Searching wikipedia ----")
        result = wikipedia.summary(query.replace("wikipedia", ""), sentences=2)
        speak("Accoording to wikipedia")
        speak(result)
        logging.info("user requested information fro wikipedia")
    
    #open vs code 
    elif "open vs code " in query:
         os.system("code")
    
    #music
    else:
        response = gemini_model_response(query)
        speak(response)
       # for manual # speak("I am sorry, I can't help you with that.")
        #logging.info("User asked for an unsupported command.")
        logging.info("user ask for other quesetion by LLm")