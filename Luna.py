import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as kit
import pyautogui
import time


# Use the below dictionary or try to import google contacts
email = {
    'rikhil' : 'kakanirikhil7@gmail.com', # Contact me in Mail if you have any doubts
    'sam' : 'sister@gmail.com',
    'mom' : 'mom@gmail.com',
    'dad' : 'father@gmail.com'
    
}
contacts = {
    'rikhil': 'XXXXXXXXXXX',
    'sister' : 'XXXXXXXXXXX',
    'mom' : 'XXXXXXXXXXX',
    'dad' : 'XXXXXXXXXXX',
    'friend' : '9342055412'
}


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def set_pitch(pitch_value):
    engine.setProperty('pitch', pitch_value)
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Boss")
    elif hour >= 12 and hour <18:
        speak("Good Afternoon Boss")
    else:
        speak("Good Evening Boss")
        
    speak("This is  Luna  your  personal  assistant, How may I help you")

# Note : Allow los risk app settings in gmail to send emails

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yourmail@gmail.com', 'password')
    server.sendmail('yourmail@gmail.com', to, content)
    server.close()

def get_weather(city):
    speak(f"searching weather for {city}")
    kit.search(f"weather in {city}")
    
def whatsapp(reciptent, msg):
    speak("Openning WhatsApp")
    os.startfile("C:\\Users\\kakan\\OneDrive\\Desktop\\WhatsApp.lnk")
    time.sleep(5)
    
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.typewrite(reciptent)
    time.sleep(2)
    
    # Adjust coordinates according to yur screen size
    
    pyautogui.moveTo(200,300)
    pyautogui.click()
    
    
    pyautogui.typewrite(msg)
    pyautogui.press('enter')
    speak('Message sent')
    
def takecommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print(e)
        speak("I did not understand what you are saying. Could you please repeat it?")
        return "None"
    
    return query
        
if __name__ == "__main__":
    #set_pitch(100)
    wishme()
    if 1:
        query = takecommand().lower()
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")  
            print("Searching Wikipedia...")      
            query = query.replace("wikipedia", "")
            query = query.replace("luna", "")
            query = query.replace("search", "")
            query = query.replace("about", "")
            
            results = wikipedia.summary(query, sentences=5)
           
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open google chrome' in query:
            print("Openning..")
            speak("Openning..")
            webbrowser.open("google.com")
            
        elif 'open youtube' in query:
            print("openning...")
            speak("Openning...")
            webbrowser.open("https://www.youtube.com/")
            
        elif 'play music' in query:
            print("Playing Music...")
            
            speak("Playing Music")
            music_dir = "C:\\Users\\kakan\\OneDrive\\Documents\\Luna\\Songs"
            songs = os.listdir(music_dir)
            
            speak("Which song would you like to play?")
            print("Available songs:")
            
            for song in songs:
                print(song)
            
            song_name = takecommand().lower()
            
            found_song = None
            for song in songs:
                if song_name in song.lower():  
                    found_song = song
                    break
            
            if found_song:
                speak(f"Playing {found_song}")
                os.startfile(os.path.join(music_dir, found_song))
            else:
                speak("Sorry, I couldn't find the song you asked for.")
 
                
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{strtime} Sir!")
            print(f"{strtime} Sir!")
            
        elif 'open vs code' in query:
            print("Openning...")
            speak("Openning...")
            code_path = "C:\\Users\\kakan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            
        elif 'email' in query:
            try:
                speak("To Whom should i send the email?")
                nickname = takecommand()
                if nickname in email:
                    to = email[nickname]
                    
                    speak("What do you want to sent?")
                    content = takecommand()
                    send_email(to, content)
                    
                
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send the mail")
        elif 'weather' in query:
            speak("which city would you like weather?")
            city = takecommand().lower()
            get_weather(city)
        
        elif 'whatsapp' in query:
            try:
                speak("To whom would you like to send?")
                
                recipient = takecommand().lower()
                
                if recipient in contacts:
                    phoneNo = contacts[recipient]
                    speak("what do you want to send?")
                    msg = takecommand().lower()

                    whatsapp(phoneNo,msg)
                    
                else:
                    speak("I dont have that reciptant in contacts!")
            except Exception as e:
                print(e)
                speak("Sorry I am unable to send whatsapp message!")