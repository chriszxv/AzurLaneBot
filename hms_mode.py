import pyautogui
import cv2
import sys

from enum import Enum

pyautogui.FAILSAFE = True

class GameState(Enum):
    Other = 'other'
    HMS = 'hms'
    InCombat = 'incombat'

def localeImage(image, confidence = 0.7):
    return pyautogui.locateOnScreen(image + '.png', confidence = confidence, grayscale = True)

def clickImage(targetImage, confidence = 0.7):
    location = localeImage(targetImage, confidence = confidence)
    if location is not None:
        x, y = pyautogui.center(location)
        pyautogui.click(x, y)
        pyautogui.PAUSE = 1.0
    return 

def clickImageUntilSuccess(targetImage, confidence = 0.7):
    location = None
    while location is None:
        print('...')
        location = localeImage(targetImage, confidence = confidence)
    x, y = pyautogui.center(location)
    pyautogui.click(x, y)
    pyautogui.PAUSE = 1.0
    return 


def checkGameState():
    location = localeImage('.\\images\\hms\\exercise_reward', confidence = 0.9)
    if location is not None:
        return GameState.HMS

    location = localeImage('.\\images\\incombat\\button_pause', confidence = 0.7)
    if location is not None:
        return GameState.InCombat

    return GameState.Other

def handleOtherState():
    pressSkip()
    return

def pressSkip():
    print('press C to skip...')
    pyautogui.keyDown('C')
    pyautogui.keyUp('C')
    pyautogui.PAUSE = 1.0
    return

def handleStrikeState():
    print('click hms belfast...')
    clickImageUntilSuccess('.\\images\\hms\\belfast')
    return

def handleInCombatState():
    print('click auto off if exists...')
    location = localeImage('.\\images\\incombat\\auto_off', confidence = 0.9)
    if location is not None:
        clickImageUntilSuccess('.\\images\\incombat\\auto_off')

    print('press M to call submarine...')
    pyautogui.keyDown('M')
    pyautogui.keyUp('M')
    pyautogui.PAUSE = 1.0

    pressSkip()
    return

def main():
    scriptName = sys.argv[0]
    print('Start runnng: ' + scriptName)
    print('Press Ctrl-C to quit.')
    
    while True:
        print('...')
        currentGameState = checkGameState()
        print('======================================')
        print('Current Game State: ' + currentGameState.name)

        if currentGameState == GameState.Other:
            handleOtherState()

        elif currentGameState == GameState.HMS:
            handleStrikeState()

        elif currentGameState == GameState.InCombat:
            handleInCombatState()

        # ==================================================================
        # DEBUG
        # print(checkCurrentMainChapter())
        # location = localeImage('.\\images\\subchapter\\ship_carrier_4')
        # if location is not None:
        #     x, y = pyautogui.center(location)
        #     print(location) 

        # location = pyautogui.locateOnScreen('.\\images\\ship_normal_destroyer', grayscale = True)
        # if location is not None:
        #     x, y = pyautogui.center(location)
        #     pyautogui.click(x, y) 
        # ==================================================================
    return

if __name__ == '__main__':
    main()

