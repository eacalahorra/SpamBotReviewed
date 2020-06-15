import random
import pyautogui
import sys
import time
import win32api, win32com

SpamText = ['This', 'is', 'for', 'rachel', 'you', 'big', 'fat', 'white', 'nasty', 'smelling', 'fat', 'bitch', 'why', 'you', 'took', 'me', 'off', 'the', 'motherfucking', 'schedule', 
            'with', 'your', 'trifflin', 'dirty', 'white', 'racist', 'ass', 'you', 'big', 'fat', 'oompa loompa', 'ass', 'bitch', 'i’m', 'coming', 'up', 'there', 'and', 'i’m', 'going', 'to', 'beat' 
            'the', 'fuck', 'out', 'of', 'you', 'bitch', 'and', 'don’t', 'even', 'call', 'the', 'police', 'today', 'cause', 'ima', 'come', 'up', 'there', 'unexpected', 'and', 'wait', 'on', 'your', 
            'motherfucking', 'ass', 'bitch']
mposy = 0
#print(mposx)
#print(mposy)

def spam(): #random spam function
    endcount = eval(input('Enter the amount of messages you would like to spam: '))#user inputs amount of times for spamming
    print("Click when you are ready to begin.")
    state_left = win32api.GetKeyState(0x01) #Determine State Left Mouse is in
    mousePressed = False #Declare Variable for if Mouse is Pressed
    while mousePressed == False:
        a = win32api.GetKeyState(0x01) #Variable for Determining if there is a difference between previous and current state
        if a != state_left: #Compare Previous and Current States
            mousePressed = True
            mposx, mposy = pyautogui.position() #grab mouse position
        time.sleep(.01) #Limit amount of times while loop runs
    count = 1
    while count <= endcount:
        state_esc = win32api.GetKeyState(0x1B) #Determines if Esc Is Pressed
        if state_esc > 0: #Breaks if Esc Is Pressed
            break
        pyautogui.click(mposx, mposy)#get position of chatbox
        pyautogui.typewrite(random.choice(SpamText), interval=0.01)#type random string, set interval time for typing each character
        pyautogui.hotkey('enter')#pressing of enter button
        count += 1  

def singleSpam(userPhrase):#single phrase spam function
    endcount = eval(input('Enter the amount of messages you would like to spam: '))#user inputs amount of times for spamming
    print("Click when you are ready to begin.")
    state_left = win32api.GetKeyState(0x01) #Determine State Left Mouse is in
    mousePressed = False #Declare Variable for if Mouse is Pressed
    while mousePressed == False:
        a = win32api.GetKeyState(0x01) #Variable for Determining if there is a difference between previous and current state
        if a != state_left: #Compare Previous and Current States
            mousePressed = True
            mposx, mposy = pyautogui.position() #grab mouse position
        time.sleep(.01) #Limit amount of times while loop runs
    count = 1
    while count <= endcount:
        state_esc = win32api.GetKeyState(0x1B) #Determines if Esc Is Pressed
        if state_esc > 0: #Breaks if Esc Is Pressed
            break
        pyautogui.click(mposx, mposy)#get position of chatbox
        pyautogui.typewrite(userPhrase, interval=0.01)#type user selected string, set interval time for typing each character
        pyautogui.hotkey('enter')#pressing of enter button
        count += 1
        
def gather(): #main function
    sPhrase = eval(input('Enter 1 for a Single Phrase, or 2 for a random set of phrases: '))#determines if user wants to spam a single phrase or a prebuilt set of random phrases
    if sPhrase == 1:
        userPhrase = input('Please Enter the Phrase you would like to spam: ')#changes SpamText to user designated phrase
        singleSpam(userPhrase)
        print('User Phrase Spamming')#console output to verify which sPhrase choice is running
    elif sPhrase == 2: #runs preselected spam phrases
        spam()
        print('Pre-Selected Phrases Spamming')#console output to verify which sPhrase choice is running
    else:
        print('Slection invalid. Please try again.')
        gather()

#spam()
gather()
