import pyttsx3
import speech_recognition as sr
import jarvis
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
while(1):
    query = takecommand().lower()
    if 'wake up' in query: 
        jarvis.Task_Gui()
        

    








    
