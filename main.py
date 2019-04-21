# Inheriting stuff

import speech_recognition as sr
import os
import webbrowser
import subprocess



# Making r meaningful

r = sr.Recognizer()

# Getting the microphone and printing "Say Something" after getting it

with sr.Microphone() as source:
    print("Say Something")
    # Making audio the thing we said (in sound)
    audio = r.listen(source)

# Making said the thing we said (in text)

said = r.recognize_google(audio)
said = said.lower()

# What happens if the user said something:
print("You have said " + said)


# Voice commands
constantsaid = said 
if "open computer" in said or "open this pc" in said or "open my computer" in said:     # Opens computer
    print("Open Computer command executed")
    os.system("explorer ::{20D04FE0-3AEA-1069-A2D8-08002B30309D}")
    

if "open documents" in said or "open document" in said or "open my document" in said or "open my documents" in said:     # Opens documents folder
    print("Open Documents command executed")
    os.system("explorer shell:document")  

if "open download" in said or "open downloads" in said or "open my download" in said or "open my downloads" in said:    # Opens downloads folder
    print("Open Downloads command executed")
    os.system("explorer shell:downloads")

if "open desktop" in said:      # Opens Desktop
    print("Open Desktop command executed")
    os.system("explorer shell:Desktop")

if "open music" in said or "open my music" in said:     # Opens music folder
    print("Open Music command executed")
    os.system("explorer shell:Music")

if "open video" in said or "open my video" in said or "open videos" in said or "open my videos" in said:    # Opens video folder
    print("Open Video command executed")
    os.system("explorer shell:Video")

if "open chrome" in said or "open google chrome" in said:       # Opens Chrome browser
    print("Open Google Chrome command executed")
    os.system("start chrome")

if "open firefox" in said or "open mozilla firefox" in said:    # Opens Firefox browser
    print("Open Mozilla Firefox command executed")
    os.system("start firefox")

if "open control panel" in said:        # Opens Windows control panel
    print("Open Control Panel command executed")
    os.system("")

if "open" in said:

    said = said.replace("open", "")
    if "and" in said:
        said = said.split("and")
        print(said)
        
    else:
        said = [said, "empty"]
    i = 0
    while i < len(said):
        if "chrome" in said[i]:
            said[i] = said[i].replace("chrome", "")
            said[i] = said[i].replace("in", "")
            said[i] = said[i].replace("browser", "")
            said[i] = said[i].replace(" ", "")
            said[i] = "www." + said[i] + ".com"
            said[i] = "start chrome " + said[i]
            os.system(said[i])
            
        if "firefox" in said[i]:
            said[i] = said[i].replace("firefox", "")
            said[i] = said[i].replace("in", "")
            said[i] = said[i].replace("browser", "")
            said[i] = said[i].replace(" ", "")
            said[i] = "www." + said[i] + ".com"
            said[i] = "start firefox " + said[i]
            os.system(said[i])
        i = i + 1

# Except (exit)
print("Program exited sucessfully")
