import pyautogui
import keyboard
import time
import os

def cr():
    pyautogui.alert(text='Please go to roblox in order to work. You have 5 seconds once you click "OK" ', title='Auto briefer', button='OK')
    time.sleep(5)
    pyautogui.press('/')
    pyautogui.write('You are now under the authority of the Security Department.')
    print('You are now under the authority of the Security Department.')
    keyboard.press('enter')
    time.sleep(4)
    pyautogui.press('/')
    pyautogui.write('Failure to comply with any order or this brief will result in dismissal from this test, criminal charges, and possibly a termination.')
    print('Failure to comply with any order or this brief will result in dismissal from this test, criminal charges, and possibly a termination.')
    keyboard.press('enter')    
    time.sleep(4)
    pyautogui.press('/')
    pyautogui.write('You are to enter through the scanner at my command one by one. You are to declare if you are armed one by one.')
    print('You are to enter through the scanner at my command one by one. You are to declare if you are armed one by one.')
    keyboard.press('enter')
    time.sleep(4)
    pyautogui.press('/')
    pyautogui.write('Is that understood?')
    print('Is that understood?')
    keyboard.press('enter')
    print('Said brief!')
    time.sleep(3)
    pyautogui.alert(text='Typed brief!', title='Auto briefer', button='OK')

def escort():
    pyautogui.alert(text='Please go to roblox in order to work. You have 5 seconds once you click "OK" ', title='Auto briefer', button='OK')
    print('Please go to roblox in order to work. You have 5 seconds once you click "OK" ')
    time.sleep(5)
    pyautogui.press('/')
    pyautogui.write('Class-D. These are the rules you are expected to follow at all times.')
    print('Class-D. These are the rules you are expected to follow at all times.')
    keyboard.press('enter')
    time.sleep(4)
    pyautogui.press('/')
    pyautogui.write('Do not attempt to escape this test or breach any SCPs.')
    print('Do not attempt to escape this test or breach any SCPs.')
    keyboard.press('enter')
    time.sleep(4)
    pyautogui.press('/')
    pyautogui.write('Obey all orders given to you and do not speak unless spoken to.')
    print('Obey all orders given to you and do not speak unless spoken to.')
    keyboard.press('enter')
    time.sleep(4)
    pyautogui.press('/')
    pyautogui.write('You are to immediately follow all orders. Resisting will result in immediate termination.')
    print('You are to immediately follow all orders. Resisting will result in immediate termination.')
    keyboard.press('enter')
    time.sleep(4)
    pyautogui.press('/')
    pyautogui.write('Am I understood?')
    print('Am I understood?')
    keyboard.press('enter')
    print('Said brief!')
    time.sleep(3)
    pyautogui.alert(text='Typed brief!', title='Auto briefer', button='OK')

got = input('AUTO BRIEFER. \n There is only cr and esc command. \n cr: CR brief. \n esc: escort brief. \n Please choose brief:\n')

if got == 'cr' or got == 'CR':
    cr()
elif got == 'esc' or got == 'ESC':
    escort()
else:
    print('There is only cr and esc command. cr: CR brief. esc: escort brief. Please re open the bat file.')
