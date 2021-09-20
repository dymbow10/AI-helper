import os
import webbrowser #for web access
from time import sleep
from datetime import *
import winsound #for voices
import speech_recognition as sr #speech to text

r = sr.Recognizer()

def open_file():
    #the AI will try to open the name files
    try:
        arq=open("names.txt","r")
    except: #if never used, the name files will be created and their respective names will be saved
        arq=open("names.txt","w")
        print("Hello, it seems this is the first time you are using this AI")
        print("please input a name you would like to be called and a name for the AI")
        name=input("Input your name: ")
        ainame=input("Input a name for the AI: ")
        arq.write(name+"\n")
        arq.write(ainame+"\n")
        arq.close()
        print("First time configuration finished, the program will now close")
        os.system("PAUSE")
        exit()
    return arq

def get_time():#fuction to get the local time from user's PC
    now=datetime.now()
    time=now.strftime("%H:%M:%S")
    return time

def treatment(arq):#name treatment
    text=arq.readlines()
    temp = text[0]
    name=""
    ai_name=""
    for i in range(len(temp)):#removing residual \n from user name
        if temp[i] != "\n":
            name += temp[i]
    temp = text[1]
    for i in range(len(temp)):#removing residual \n from IA name
        if temp[i] != "\n":
            ai_name+=temp[i]
    arq.close()
    return name, ai_name

def greeting(name, ai_name,time):
    greeting=""
    time=str(time).split(":")
    hour = int(time[0])
    if hour >= 6 and hour < 12:
        greeting = "Good Morning"
        winsound.PlaySound("sounds/greeting1.wav", winsound.SND_ASYNC)
    elif hour >= 12 and hour < 18:
        greeting = "Good Afternoon"
        winsound.PlaySound("sounds/greeting2.wav", winsound.SND_ASYNC)
    else:
        greeting =  "Good Evening"
        winsound.PlaySound("sounds/greeting3.wav", winsound.SND_ASYNC)
    print("{:1s}, {:1s} this is {:1s} your AI helper".format(greeting,name,ai_name))
    return

def voice_input():
    with sr.Microphone() as source:
        while True:
            try:
                print("Say something: ")
                audio = r.listen(source)
                text = r.recognize_google(audio).lower()
            except:
                continue
            
            if "jarvis" in text:
                return text
            elif "exit" or "quit" in text:
                winsound.PlaySound("sounds/goodbye.wav", winsound.SND_ASYNC)
                print("Goodbye")
                os.system("PAUSE")
                os._exit(0)
                
def google():
    winsound.PlaySound("sounds/google.wav", winsound.SND_ASYNC)
    string=input("Input your seach: ").replace(" ","+")#proper url formatting
    webbrowser.open_new_tab("www.google.com/search?q={:1s}".format(string))
    voice_input()
    return

def youtube():
    winsound.PlaySound("sounds/youtube.wav", winsound.SND_ASYNC)
    string=input("Input your seach: ").replace(" ","+")#proper url formatting
    webbrowser.open_new_tab("www.youtube.com/search?q={:1s}".format(string))
    voice_input()
    return

def instagram():
    winsound.PlaySound("sounds/instagram.wav", winsound.SND_ASYNC)
    webbrowser.open_new_tab("www.instagram.com")
    voice_input()
    return

def facebook():
    winsound.PlaySound("sounds/facebook.wav", winsound.SND_ASYNC)
    webbrowser.open_new_tab("www.facebook.com")
    voice_input()
    return

def whatsapp():
    winsound.PlaySound("sounds/whatsapp.wav", winsound.SND_ASYNC)
    webbrowser.open_new_tab("https://web.whatsapp.com")
    voice_input()
    return

def manual():
    file = open("docs.txt","r")
    text=file.readlines()
    print(text)
    file.close()
    voice_input()
    return

def tools(name,text):
    while True:
        winsound.PlaySound("sounds/options2.wav", winsound.SND_ASYNC)
        print("How can I help you {:1s} ?".format(name))
        with sr.Microphone() as source:
               try:
                   print("How can I help you {:1s} ?".format(name))
                   audio = r.listen(source)
                   choice=r.recognize_google(audio).lower()
                   print(choice)
               except:
                   continue
        '''if "exit" or "quit" in choice:
            winsound.PlaySound("sounds/goodbye.wav", winsound.SND_ASYNC)
            print("Goodbye, {:1s}".format(name))
            os.system("PAUSE")
            return'''
        if "google" in choice:
            google()
        elif "youtube" in choice:
            youtube()
        elif "instagram" in choice:
            instagram()
        elif "facebook" in choice:
            facebook()
        elif "message" in choice:
            whatsapp()
        elif "help" or "manual" in choice:
            manual()
        else:
            winsound.PlaySound("sounds/error.wav", winsound.SND_ASYNC)
            print("Use 'Help' or 'Manual' for JARVIS' documentation!")
            sleep(3)

def main():
    arq=open_file()
    time=get_time()
    name,ai_name=treatment(arq)
    greeting(name,ai_name,time)
    text=voice_input()
    tools(name,text)
    return

main()
