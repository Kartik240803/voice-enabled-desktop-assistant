import pyjokes
import pyttsx3
import webbrowser
import datetime
import wikipedia
import speech_recognition as sr
import os
import smtplib
import requests
from bs4 import BeautifulSoup
from wikipedia.wikipedia import search
import pywhatkit
import time
import keyboard
import pyautogui
from PyDictionary import PyDictionary as dic
import chatbot
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(f":{audio}")
    print("")
    engine.runAndWait()

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.login('patelkartik625@gmail.com', 'kartik240803')
    server.sendmail('patelkartik625@gmail.com', to, content)
    server.close()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("i am Jarvis sir. Please tell me how may I help you")

def takecommand():
    '''
    it takes microphone input from the user and return string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language='en-in')
        print(f"You said: {query}")
        
    except Exception as e:
         print("Say that again")
         return "None"
    return query  

def whatsapp(num):
    speak("What should i tell?")
    mess = takecommand()
    hour = int(datetime.datetime.now().strftime("%H"))
    min = int(datetime.datetime.now().strftime("%M"))
    min = min + 2
    pywhatkit.sendwhatmsg(num,mess,hour,min,30)
    speak("Message has been sent!")

def dict():
    speak("Activated dictionary boss!")
    speak("tell me the problem")
    prob=takecommand()
    if 'meaning' in prob:
        prob =prob.replace("meaning","")
        prob =prob.replace("jarvis","")
        prob =prob.replace(" ","")
        prob =prob.replace("what is the","")
        prob =prob.replace("of","")
        result = dic.meaning(prob)
        speak(f"the Meaning for {prob} is {result}")

    elif 'synonym' in prob:
        prob =prob.replace("synonym","")
        prob =prob.replace("jarvis","")
        prob =prob.replace(" ","")
        prob =prob.replace("what is the","")
        prob =prob.replace("of","")
        result = dic.synonym(prob)
        speak(f"the Synonym for {prob} is {result}")

    elif 'antonym' in prob:
        prob =prob.replace("antonym","")
        prob =prob.replace("jarvis","")
        prob =prob.replace(" ","")
        prob =prob.replace("what is the","")
        prob =prob.replace("of","")
        result = dic.synonym(prob)
        speak(f"the Antonym for {prob} is {result}")

    
        

        

def Task_Gui():
    wishme()
    while(True):
        query = takecommand().lower()
        # logic for do task
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace('wikipedia', "")
            query = query.replace('jarvis', "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)
        

        
        elif 'about you' in query:
            speak("I am fine!")

        elif 'open chrome' in query:
            chromepath ="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
            os.startfile(chromepath)
            speak("ya sure!")
            
        elif 'open youtube' in query:
            webbrowser.open('http://youtube.com')
            speak("Opening youtube")
        
        elif 'open google' in query:
            webbrowser.open('http://google.com')
            speak("Opening google")
        
        elif 'open stack overflow' in query:
            webbrowser.open('http://stackoverflow.com')
            speak("Opening stackoverflow")
        
        elif 'open github' in query:
            webbrowser.open('http://github.com')
            speak("Opening github")
        
        elif 'open portfolio' in query:
            webbrowser.open('https://groww.in/dashboard/explore/stocks')
            speak("Opening your portfolio sir.")
        
        elif 'meeting' in query:
            webbrowser.open('https://meet.google.com//ttu-ukxr-owx')
            speak("Starting meeting very soon")
   
        elif 'the time ' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("%H")
            
            # if int(strTime) > 12:00:00 :
            #     print("")
                

            speak(f"Sir ,the time is {strTime}")
        
        elif 'open code' in query:
            codepath = "C:\\Users\\patel kartik\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak("Opening Visual Studio Code")
        
        elif 'vs code' in query:
            codepath = "C:\\Users\\patel kartik\\AppData\\Local\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak("Opening Visual Studio Code")
        
        elif 'email to kartik' in query:
            try:
                speak("What should i Say?")
                content = takecommand()
                to = "patelkartik625@gmail.com"
                sendemail(to, content)
                speak("Email has been sent!")

            except Exception as e:

                speak("Sorry  kartik i am not able to send email right noe ")
        
        elif 'break' in query:
            speak("Ok boss , call me any time when you need!")
            break
        
        elif 'buy' in query:
            speak("Ok boss , call me any time when you need!")
            break
    
        elif 'maths' in query:
            webbrowser.open('https://meet.google.com/nca-wqse-vxg')
            speak("joining Urvi mam's Lecture sir")
        
        elif 'youtube search' in query:
            query = query.replace("youtube" ,"")
            query = query.replace("search" , "")
            query = query.replace("jarvis" ,"")
            speak(f"Searching {query} on youtube")
            webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
            pywhatkit.playonyt(query)
            speak("This may also help you ,sir")
        
        elif 'google search' in query:
            query = query.replace("google", "")
            query = query.replace("search" , "")
            query = query.replace("jarvis","")
            speak("Thish is what i found for your search sir!")
            pywhatkit.search(query)
            speak("Search done")
        
        elif 'website' in query:

            if query.startswith("launch") :
                query = query.replace("search" , "")
                query = query.replace("jarvis","")
                query = query.replace("website" , "")
                query = query.replace("open" , "")
                query = query.replace("launch" , "")
                speak("Sir , tell me the name of the website.")
                web = takecommand()
                web = web.replace("open" , "")
                web = web.replace(" " , "")
                web = web.replace("  " , "")
                web = web.replace("   " , "")
                webbrowser.open(f'https://{web}.com')
                speak("Website Launched!")

            else:
                speak("Ok sir , launching..")
                query = query.replace("search" , "")
                query = query.replace("jarvis","")
                query = query.replace("website" , "")
                query = query.replace("open" , "")
                query = query.replace(" " , "")
                query = query.replace("  " , "")
                query = query.replace("   " , "")
                a = 'https://www.' + query + '.com'
                webbrowser.open(a)
                speak("Website Launched!")
        
        elif 'facebook' in query :
            webbrowser.open('https://www.facebook.com/')
            speak("Opening Facebook")
        
        elif 'instagram' in query :
            webbrowser.open('https://www.instagram.com')
            speak("opening instagram")
        
        elif 'play music' in query : 
            speak("tell me The Name of the song !")
            result=takecommand()
            result= result.replace("play","")
            result= result.replace("music","")
            result= result.replace("jarvis" , "")
            result =result.replace(" ","")
            pywhatkit.playonyt(result)
            speak("Your Song has been Started!")
        
        elif 'whatsapp message' in query :
            query = query.replace("whatsapp message","")
            query = query.replace("to","")
            query = query.replace("send","")
            query = query.replace(" ","")
            if 'kunal' in query:
                num = '+916353985903'
                whatsapp(num)
            elif 'mummy' in query:
                num ='+919824602588'
                whatsapp(num)
            elif 'ammu' in query :
                num = '+918097093076'
                whatsapp(num)
            elif 'vishvam' in query :
                num = '+917383936339'
                whatsapp(num)
            elif 'prachi' in query :
                num = '+917698391669'
                whatsapp(num)
            elif 'ruchika' in query :
                num = '+916358030244'
                whatsapp(num)
        
        elif  'screenshot' in query :
           speak("ok boss , what should I name that file?")
           pathname  = takecommand()
           pathname = pathname.replace("jarvis" , "")
           pathname = pathname.replace("ok" , "")
           pathname = pathname.replace("save" , "")
           pathname = pathname.replace("that" , "")
           pathname = pathname.replace(" " , "")
           ss =  pyautogui.screenshot()
           path = f"D:\\screenshot\\{pathname}.png"
           ss.save(path)
           speak("Boss ,Screenshot has been saved successfully!")
        
        elif  'close youtube' in query :
            speak("Ok boss , Wait a second")
            os.system("TASKKILL /F /im chrome.exe")
            speak("Boss ,App closed successfully!")

        elif  'close code' in query :
            speak("Ok boss , Wait a second")
            os.system("TASKKILL /F /im code.exe")
            speak("Boss ,App closed successfully!")
             
        elif  'close whatsapp' in query :
            speak("Ok boss , Wait a second")
            os.system("TASKKILL /F /im whatsapp.exe")
            speak("Boss ,App closed successfully!")
             
        elif 'stop' in query :
            keyboard.press('k')
            keyboard.release('k')
            speak("Ok boss!")

        elif 'mute' in query :
            keyboard.press('m')
            keyboard.release('m')
            speak("Ok boss!")

        elif 'restart' in query :
            keyboard.press('0')
            keyboard.release('0')
            speak("Ok boss!")

        elif 'skip' in query :
            keyboard.press('l')
            keyboard.release('l')
            speak("Ok boss!")

        elif 'back' in query :
            keyboard.press('j')
            keyboard.release('j')
            speak("Ok boss!")

        elif 'full screen' in query :
            keyboard.press('f')
            keyboard.release('f')
            speak("Ok boss!")

        elif 'film mode' in query :
            keyboard.press('t')
            keyboard.release('t')
            speak("Ok boss!")

        elif 'new tab' in query :
            keyboard.press('ctrl+t')
            keyboard.release('ctrl+t')
            speak("Ok boss!")
            
        elif  'window' in query :
            keyboard.press('ctrl+n')
            keyboard.release('ctrl+n')
            speak("Ok boss!")

        elif 'close the tab' in query :
            keyboard.press('ctrl+w')
            keyboard.release('ctrl+w')
            speak("Ok boss!")

        elif 'close the chrome' in query :
            os.system("TASKKILL /F /im chrome.exe")
            speak("Ok boss!")
        
        elif 'first tab' in query:
            keyboard.press('ctrl+1')
            keyboard.release('ctrl+1')
            speak("Ok boss!")

        elif 'secomd tab' in query:
            keyboard.press('ctrl+2')
            keyboard.release('ctrl+2')
            speak("Ok boss!")

        elif 'third tab' in query:
            keyboard.press('ctrl+3')
            keyboard.release('ctrl+3')
            speak("Ok boss!")

        elif 'fourth tab' in query:
            keyboard.press('ctrl+4')
            keyboard.release('ctrl+4')
            speak("Ok boss!")

        elif 'fifth tab' in query:
            keyboard.press('ctrl+5')
            keyboard.release('ctrl+5')
            speak("Ok boss!")

        elif 'sixth tab' in query:
            keyboard.press('ctrl+6')
            keyboard.release('ctrl+6')
            speak("Ok boss!")

        elif 'seventh tab' in query:
            keyboard.press('ctrl+7')
            keyboard.release('ctrl+7')
            speak("Ok boss!")

        elif 'incognito' in query:
            keyboard.press('ctrl+shift+n')
            keyboard.release('ctrl+shift+n')
            speak("Ok boss!")
               
        elif 'history' in query:
            keyboard.press('ctrl+h')
            keyboard.release('ctrl+h')
            speak("Ok Boss!")
        
        elif 'view download' in query:
            keyboard.press('ctrl+d')
            keyboard.release('ctrl+d')
            speak("Ok Boss!")

        elif 'zoom the screen' in query:
            keyboard.press('ctrl+plus')
            keyboard.release('ctrl+plus')
            speak("Ok Boss!")

        elif 'zoom out the screen' in query:
            keyboard.press('ctrl+-')
            keyboard.release('ctrl+-')
            speak("Ok Boss!")
            
        elif 'joke' in query:
            jk = pyjokes.get_joke()
            speak("Ok Boss!")
            speak(jk)

        elif 'my location' in query:
            webbrowser.open('https://www.google.com/maps/@22.3226706,72.6197367,52m/data=!3m1!1e3')
            speak("Opening your Location!")


        elif 'dictionary' in query:
            dict()

        elif 'open cam' in query:
            keyboard.press('ctrl+e')
            keyboard.release('ctrl+e')
            speak("Ok boss!")

        elif 'close cam' in query:
            keyboard.press('ctrl+e')
            keyboard.release('ctrl+e')
            speak("Ok boss!")
        
        elif 'open microphone' in query:
            keyboard.press('ctrl+d')
            keyboard.release('ctrl+d')
            speak("ok boss!")

        elif 'close microphone' in query:
            keyboard.press('ctrl+d')
            keyboard.release('ctrl+d')
            speak("ok boss!")

        elif 'change the tab' in query:
            keyboard.press('alt+tab')
            keyboard.release('alt+tab')
            
        else:
            reply = chatbot.ChatterBot(query)
            reply =str(reply)
            reply =reply.replace("None" , "")
            speak(reply)
             
        
            
# Task_Gui()           

            
            
                 
            
            
            
        
            
                    

        


              
            
            
             
            
    


            
             
                

            
            
        
              