import os
import  random as rand
import webbrowser as wb
import speech_recognition as sr
import  pyaudio
import  pyttsx3
from neuralnetwork import speak
quarry='just'
start_message=""" ***************************************************************************
                  ***************************************************************************
                  **         THIS IS COPY CAT OF COMMAND PROMPT OF WINDOWS                 **
                  **                        CREATED  BY                                    **
                  **                       ~~~~~~~~~~~~~                                   **
                  **                       PRABHAT KUMAR                                   **
                  **                       ~~~~~~~~~~~~~                                   **
                  ***************************************************************************
                  ***************************************************************************
 Hint:  write sumethin ... for anythinng..............         
"""
smily=''' 
                                *                              *
                               ***                            ***
                              *****                          *****
                               ***                            ***
                                *                              * 





                       *****                                      *****
                         ****                                    ****
                           ****                                ****
                            ****                              ****
                               ****                         ****
                                  ****                   **** 
                                    *******           ******
                                      ********************
                                        **************** 
                                              ***   
'''
helps=''' This is same like command prompt 
          you like simple string like
          make file for create file 
          open google 
          serch on stack over flow
          open application by name
          .
          .
          .
'''
print(start_message)
while True:
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            quarry=r.recognize_google(audio,language='en-in')
        except:
            speak("can you say it again please...")

    if 'run dragon center' in quarry:
        path = "C:\\Program Files (x86)\\MSI\\Dragon Center\\Dragon Center.exe"
        os.startfile(path)
    elif 'sublime' in quarry:
        path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
        os.startfile(path)
    elif 'camera' in quarry:
        path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
        os.startfile(path)
    elif 'python' in quarry:
    	path='C:\\Users\\prabh\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe'
    	os.startfile(path)
    elif 'song' in quarry:
        music_dir="D:\\songs\\Video"
        songs=os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,songs[rand.randint(0,len(songs))]))
    elif 'node js' in quarry:
        path="C:\\Program Files\\nodejs\\node.exe"
        os.startfile(path)
    elif 'create file'in quarry:
        path="D:\\automation\\makefile.bat"
        os.startfile(path)
    elif 'ok google' in quarry:
        wb.open('google.com')
    elif 'yotube' in quarry:
        wb.open('youtube.com')
    elif 'facebook' in quarry:
        wb.open('facebook.com')
    elif 'twitter' in quarry:
        wb.open('twitter.com')
    elif 'stack over flow' in quarry:
        wb.open('stackoverflow.com')
    elif 'help' in quarry:
        print(helps)
    elif 'bol bum' in quarry:
        music_dir="D:\\songs\\bol bum song"
        songs=os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,songs[rand.randint(0,len(songs))]))
    elif 'hello' in quarry:
        speak('hello sir how may i help you')






##############END STATEMENT ######################
    elif 'quit' or 'exit' in quarry:
        quit()