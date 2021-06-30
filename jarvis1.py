import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib  

import wolframalpha 

try:
    app = wolframalpha.Client("ELR5X6-EKJUUX6QX6")
except Exception:
    print("Internet issue")


engine = pyttsx3.init()



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good morning sir")
    
    elif hour >=12 and hour <17 :
        speak("good afternoon sir")

    else: 
        speak("good evening")

    speak(" I am Arun kumar bakshi, how may I help you ")
    







def takecommand():
    #take microphone as a input and gives the string as output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        
        audio = r.listen(source)
        

    try: 
        print("Recognizing...")
        query = r.recognize_google(audio, language =  'en-in')
        print(f"User said: {query}\n")


    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query


  


if __name__ == "__main__":
    wishme()   
    
    

    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query, sentences = 2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open gmail' in query:
            webbrowser.open("www.gmail.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open sahara ' in query:
            webbrowser.open("www.robotics-ral.com")

        elif ' what is temperature ' in query:
            res = app.query(query)
            speak(next(res.results).text)


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak("sir, the time is" + strTime)

        elif "date" in query:
            strDate = datetime.datetime.now().date()
            speak(strDate)

        elif 'my birthday' in query:
            speak("sir, your birthday is on march 19")


        elif 'email to lakshmi' in query:
            try:
                speak("what should i say")
                content = takecommand()
                to = "vmahalakshmi@gmail.com"
                sendEmail(to, content)
                speak("Email is sent")

            except:
                speak("internert is slow")

        elif 'calculate' in query:
            try:
                #speak("what should i calculate")
                res = app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)

            except:
                print("error")

        elif ' temperature' in query:
            try:
                res = app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("error")

            
        elif 'tell me a joke' in query:
            try:
                res = app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)

            except:
                print("error")


        


       

        

        

   
     


