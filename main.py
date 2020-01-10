import speech_recognition as sr1
import speech_recognition as sr2
import re
import time
import webbrowser
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests
import urllib.request
import urllib.parse
import os
import pyttsx3
from os import path
import winreg
from datetime import datetime
from datetime import date

terminate = ['bye','shutdown', 'exit', 'quit', 'go to sleep', 'good bye']
chrome = ['chrome browser','google chrome','browser','google']
regedit = ['registry editor', 'editor', 'registry']
brave =['brave browser']




def talk(audio):
    print(audio)
    vc_id='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine=pyttsx3.init(driverName='sapi5')
    engine.setProperty('rate', 150)    # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1
    engine.setProperty('voice',vc_id)
    engine.say(audio)  
    engine.runAndWait()

def myCommand():
    r2 = sr2.Recognizer()
    with sr2.Microphone() as source:
        r2.pause_threshold = 1
        r2.adjust_for_ambient_noise(source, duration=1)
        audio = r2.listen(source)
        print('analyzing')
    try:
        command=r2.recognize_google(audio, language = "en-US").lower()
        print('You said: ' + command + '\n')
        time.sleep(2)
    except sr2.RequestError:
        print('\nNo Internet Connection\n')
    except sr2.UnknownValueError:
        print('\nYour last command could Not Understood\n')
        #command = myCommand();
    else:
        return command

def nemo(command):
    errors=[
        "I don't know what you mean",
        "Did you mean astronaut?",
        "Can you repeat it please?",
    ]
    
    # Search on Google
    if 'search' in command:
        if 'youtube' in command:
            youtube(command)
        elif 'wikipedia' in command: 
            talk("Opening Wikipedia") 
            indx = command.split().index('wikipedia') 
            query = command[indx + 1:] 
            driver = webdriver.Chrome(executable_path='chromedriver.exe')
            driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query)) 
            return
        else:
            reg_ex = re.search('open google and search (.*)', command)
            search_for = command.split("search",1)[1] 
            print('Searching: ', search_for)
            url = 'https://www.google.com/'
            if reg_ex:
                subgoogle = reg_ex.group(1)
                url = url + 'r/' + subgoogle
            talk('Okay!')
            driver = webdriver.Chrome(executable_path='chromedriver.exe')
            driver.get('http://www.google.com')
            search = driver.find_element_by_name('q')
            search.send_keys(str(search_for))
            search.send_keys(Keys.RETURN) # hit return after you enter search text
            #os.system("pause")
    elif 'open' in command:
        open(command)
        return        
    elif 'close'  in command:
        close(command)
        return        
    elif command in ('hello','who are you','what are you','do i know you'):
        talk('Hello! I am Nemo the Virtual Assistant. How can I help you?')
    elif command in ["who made you","created you",'developer']: 
        talk("I have been created by Panchal Saurabh & Nitish.")
        return
    elif 'time' in command:
        tt=time.localtime(time.time())
        d = datetime.strptime( str(tt[3])+":"+str(tt[4]) , "%H:%M")
        talk('Today\'s Time is')
        talk(d.strftime("%I:%M %p"))
        return        
    elif 'date' in command:
        today = date.today()	
        d2 = today.strftime("%B %d, %Y")
        talk('Today\'s Date is')
        talk(d2)
        return
    elif 'youtube' in command:
        youtube(command)
        pass
    elif 'extra' in command:
        talk('You will find out soon')
        return        
    elif 'pause' in command:
        os.system("pause")
        return
    else:
        error = random.choice(errors)
        talk(error)

def open(command):
    prcs = command.split("open ",1)[1]
    #print(prcs)
    if prcs in chrome:
        prcs='chrome'
    elif prcs in regedit:
        prcs='regedit'
    elif prcs in brave:
        prcs='brave'
    elif 'youtube' in command:
            youtube(command)
            return
    print(prcs)
    try:
        handle = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
        r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\App Paths\\"+prcs+".exe")
        pth = str(r""+winreg.QueryValue(handle,None)).replace("\\","\\\\")
        talk('Opening '+prcs)
        os.startfile(pth)
        #os.system("pause")
    except:
        talk('Application not Installed')


def close(command):
    prcs = command.split("close ",1)[1] 
    if prcs in chrome:
        prcs='chrome'
    elif prcs in regedit:
        prcs='regedit'
    elif prcs in brave:
        prcs='brave'
    try:
        ps=os.system("taskkill /f /im "+prcs+".exe")
        if ps==0:
            talk(prcs+" Closed")
        elif ps==1:
            talk('Access Denied')
        else:
            talk(prcs+' is not open')
    except:
        talk(prcs+' Not open or Access Denied')

def youtube(command):
    talk('Ok!')
    reg_ex = re.search('youtube (.+)', command)
    if reg_ex:
        domain = command.split("youtube",1)[1] 
        query_string = urllib.parse.urlencode({"search_query" : domain})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        #print("http://www.youtube.com/watch?v=" + search_results[0])
        try:
            webbrowser.open("http://www.youtube.com/watch?v={}".format(search_results[0]))
        except:
            print('Too many results')
        #os.system("pause")
    return



#loop to continue executing multiple commands
#def activate():


if __name__ == '__main__':
        while 1:
            txt1 = myCommand()
            if txt1 == 0:
                continue
            if txt1 in ['activate','hey nemo','wake up','hey google','ok google']:
                talk('Nemo Ready')
                print('Listening!')
                txt2 = myCommand()
                if txt2 == 0:
                    continue
                if txt2 in terminate:
                    talk('Bye Bye!!')
                    #talk('Tataa')
                    continue
                    #print(txt,'\n')
                if txt2 is None:
                    continue
                nemo(txt2)
            elif str(txt1) in ['shutdown','quit','exit','shutup']:
                break


    