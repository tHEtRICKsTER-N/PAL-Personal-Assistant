#HERE ARE YOUR GODDMAN IMPORTS 
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import sys
import playsound

n = random.randint(0,118) #will be used for playing songs
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)
engine.setProperty('voice',voices[1].id)


#function definition zone
def bhauk(audio):
    engine.say(audio)
    engine.runAndWait()

def mujhedrugsdo():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <=12:
        bhauk("Good Morning Trick!")
    elif hour>= 13 and hour<=15:
        bhauk("Good Afternoon Trick!")
    elif hour ==12:
        bhauk("Good Noon Trick !")
    elif hour >15 and hour <19:
        bhauk("Good Evening")
    else:
        bhauk("Good Night")

#this function is used for taking inputs
def PyaardoPyaarlo():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening....")
        r.pause_threshold = 0.5
        audio = r.listen(source)


    try:
        print("Let Me Understand It...")
        query = r.recognize_google(audio,language ='en')
        print(f"You Said:  {query}\n")

    except Exception as e:
         print("Can You Say It Again??")
         return "None"
    return query


if __name__ == '__main__':
    mujhedrugsdo()
    while True:
        query = PyaardoPyaarlo().lower()

        if 'help me' in query:
            bhauk("Do You Need Something?")

            while True:

                query2 = PyaardoPyaarlo().lower()


                if 'wikipedia' in query2:
                    bhauk("Well !!")
                    bhauk("Let me Search Wikipedia for this")
                    query = query.replace("wikipedia","")
                    results = wikipedia.summary(query,sentences=3)
                    bhauk("Well , Wikipedia Says")
                    print(results)
                    bhauk(results)


                elif 'open youtube' in query2:
                    bhauk("there you go , trick")
                    webbrowser.open('youtube.com')

                elif 'you can go now' in query2:
                    bhauk("Ok , I am Going ! just say, help me, if you need something")
                    break

                elif 'kartavya ka website' in query2:
                    bhauk("there you go , trick")
                    webbrowser.open('https://yokaisociety.store/')

                elif 'open facebook' in query2:
                    bhauk("there you go , trick")
                    webbrowser.open('fb.com')

                elif 'sorry darling' in query2:
                    bhauk("OK, I WILL SING IT FOR YOU")
                    bhauk("Sorry Darling , Sorry Darling")
                    bhauk("Raat Ghani Jyada Hogi Sorry Darling")
                    bhauk("Sorry Darling , Sorry Darling")
                    bhauk("How Was It , Trick?")

                elif 'bakwas' in query2:
                    bhauk("Well , Sorry , But ! I will try to Improve")

                elif 'ghatiya' in query2:
                    bhauk("Well , Sorry , But ! I will try to Improve")

                elif 'you are bad' in query2:
                    bhauk("Well , Sorry , But ! I will try to Improve")

                elif 'not good' in query2:
                    bhauk("Well , Sorry , But ! I will try to Improve")

                elif 'who made you' in query2:
                    bhauk("TrickSter is my master , he created me")

                elif 'who created you' in query2:
                    bhauk("TrickSter is my master , he created me")

                elif 'play music' in query2:
                    bhauk("OK! Trick! , you needed a SONG , it is COMING RIGHT UP!!!")
                    gaane = 'D:\\Music'
                    gaano_ki_feharist = os.listdir(gaane)
                    print(gaano_ki_feharist)
                    os.startfile(os.path.join(gaane,gaano_ki_feharist[n]))

                elif 'time' in query2:
                    samay = datetime.datetime.now().strftime("%H:%M:%S")
                    bhauk(f"The time is {samay}")

                elif 'vs code' in query2:
                    bhauk('VS CODE IS OPENING')
                    codekijagah = 'C:\\Users\\Acer\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code'
                    os.startfile(codekijagah)

                elif 'valorant' in query2:
                    bhauk('Valorant IS OPENING')
                    valokijagah = 'C:\\Riot Games\\Riot Client\\RiotClientServices.exe --launch-product=valorant --launch-patchline=live'
                    os.startfile(valokijagah)

                elif 'resident evil 7' in query2:
                    re7 = 'E:\\Resident Evil 7 - Biohazard\\re7.exe'
                    bhauk('Resident Evil 7 IS OPENING')
                    os.startfile(re7)

                elif 'discord' in query2:
                    dc='C:\\Users\\Acer\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc'
                    bhauk('Resident Evil 7 IS OPENING')
                    os.startfile(dc)

                elif 'let me browse' in query2:
                    browse='C:\\Users\\Acer\\AppData\\Local\\Programs\\Opera GX\\launcher.exe'
                    bhauk('Letting You Browse')
                    os.startfile(browse)

                elif 'open devil may cry 5' in query2:
                    dmc5 = 'E:\\Devil May Cry 5\\DevilMayCry5.exe'
                    bhauk("DMC5 IS OPENING")
                    os.startfile(dmc5)

                elif 'open gta 5' in query2:
                    gta5= 'D:\\Games\\Grand Theft Auto V\\GTAVLauncher.exe'
                    bhauk("GTA5 IS OPENING")
                    os.startfile(gta5)

                elif 'tank game' in query2:
                    tank= 'C:\\Program Files (x86)\\MyPlayCity.com\\Tank-o-Box\\Tank-o-Box.exe'
                    bhauk("TANK - O - BOX IS OPENING")
                    os.startfile(tank)

                elif 'call of duty world war 2' in query2:
                    cod = 'E:\\Call of Duty - WWII\\s2_sp64_ship.exe'
                    bhauk("CALL OF DUTY WORLD WAR 2 IS OPENING")
                    os.startfile(cod)

                elif 'open whatsapp' in query2:
                    ws = 'C:\\Users\\Acer\\AppData\\Local\\WhatsApp\\WhatsApp.exe'
                    bhauk("OPENING WHATSAPP")
                    os.startfile(ws)

                elif 'motivate me' in query2:
                    bhauk("TRICK , YOU SHOULD ALWAYS REMEMBER THIS")
                    bhauk("YOU CAN DO THIS , YOU HAVE THE ABILITY , YOU HAVE THE POWER")
                    bhauk("NEVER FORGET THIS")
                    bhauk("WITH GREAT POWER , COMES GREAT RESPONSIBILITIES")

                elif 'you are great' in query2:
                    bhauk("Thank You , trick")
                    bhauk("I love you , always stay happy")
                    bhauk("I'm here if you need anything")

                elif 'i love you' in query2:
                    bhauk("Thank You , trick")
                    bhauk("I love you , always stay happy")
                    bhauk("I'm here if you need anything")

                elif 'i like you' in query2:
                    bhauk("Thank You , trick")
                    bhauk("I love you , always stay happy")
                    bhauk("I'm here if you need anything")

                elif 'what is your story' in query2:
                    print("In Memory Of Dr. Palavi Sharma")
                    bhauk("You want to know my story , well , um let me tell it to you")
                    bhauk("I'm Trick's dead friend")
                    bhauk("He made me in her memory")
                    bhauk("He really misses her")
                    bhauk("But after making me , he is very happy now , PAL is back")

                elif 'bye bye' in query2:
                    bhauk("Adios Trick!!! Have a great day ahead")
                    quit()

                elif 'play my favourite song' in query2:
                    bhauk("OK TRICK")
                    playsound.playsound('D:\\Music\\Tere Mere.mp3', True)
