import pyautogui
import cv2
import sys

from enum import Enum

pyautogui.FAILSAFE = True

class GameState(Enum):
    Other = 'other'
    PreCombat = 'precombat'
    Formation = 'formation'
    Complete = 'complete'

def localeImage(image, confidence=0.7, grayscale=True):
    return pyautogui.locateOnScreen(image + '.png', confidence=confidence, grayscale=grayscale)


def clickImage(targetImage, confidence=0.7):
    location = localeImage(targetImage, confidence=confidence)
    if location is not None:
        x, y = pyautogui.center(location)
        pyautogui.click(x, y)
        pyautogui.PAUSE = 1.0
    return


def clickImageUntilSuccess(targetImage, confidence=0.7):
    location = None
    while location is None:
        print('...')
        location = localeImage(targetImage, confidence=confidence)
    x, y = pyautogui.center(location)
    pyautogui.click(x, y)
    pyautogui.PAUSE = 1.0
    return


def pressKey(key, count=1):
    print('press ' + str(key) + ' ' + str(count) + ' time(s)...')
    while(count > 0):
        pyautogui.keyDown(key)
        pyautogui.keyUp(key)
        pyautogui.PAUSE = 0.3
        count = count - 1
    return


def checkGameState():
    location = localeImage('.\\images\\crossing_waves\\suruga', confidence=0.7)
    if location is not None:
        return GameState.PreCombat

    location = localeImage('.\\images\\formation\\auto_fight_off', confidence=0.7)
    if location is not None:
        return GameState.Formation
    location = localeImage('.\\images\\formation\\auto_fight_on', confidence=0.7)
    if location is not None:
        return GameState.Formation

    location = localeImage('.\\images\\complete\\confirm', confidence=0.7)
    if location is not None:
        return GameState.Complete

    return GameState.Other


def handleOtherState():
    pressKey('C')
    return


def handlePreCombatState():
    global maximum_ex_count
    global maximum_hard_count
    global maximum_normal_count
    global maximum_easy_count
    
    global current_ex_count
    global current_hard_count
    global current_normal_count
    global current_easy_count

    print('Current EX: ' + str(current_ex_count) + '/' + str(maximum_ex_count) + ' time(s)')
    print('Current Hard: ' + str(current_hard_count) + '/' + str(maximum_hard_count) + ' time(s)')
    print('Current Normal: ' + str(current_normal_count) + '/' + str(maximum_normal_count) + ' time(s)')
    print('Current Easy: ' + str(current_easy_count) + '/' + str(maximum_easy_count) + ' time(s)')


    if current_ex_count < maximum_ex_count:
        print('handle ex chapter:')
        current_ex_count = current_ex_count + 1
        clickImage('.\\images\\crossing_waves\\ex', confidence=0.7)

    elif current_hard_count < maximum_hard_count:
        print('handle hard chapter:')
        current_hard_count = current_hard_count + 1
        clickImage('.\\images\\crossing_waves\\hard', confidence=0.7)

    elif current_normal_count < maximum_normal_count:
        print('handle normal chapter:')
        current_normal_count = current_normal_count + 1
        clickImage('.\\images\\crossing_waves\\normal', confidence=0.7)

    elif current_easy_count < maximum_easy_count:
        print('handle easy chapter:')
        current_easy_count = current_easy_count + 1
        clickImage('.\\images\\crossing_waves\\easy', confidence=0.7)

    print('click strike button...')
    clickImage('.\\images\\precombat\\strike', confidence=0.7)
    return

def handleFormationState():
    print('click auto off if exists...')
    location = localeImage(
        '.\\images\\formation\\auto_fight_off', confidence=0.9, grayscale=False)
    if location is not None:
        clickImageUntilSuccess('.\\images\\formation\\auto_fight_off')
        print('wait animation...')
        time.sleep(2.0)

    print('click auto submarine support off if exists...')
    location = localeImage(
        '.\\images\\formation\\auto_submarine_support_off', confidence=0.9, grayscale=False)
    if location is not None:
        clickImageUntilSuccess(
            '.\\images\\formation\\auto_submarine_support_off')

    print('click weigh anchor')
    clickImage('.\\images\\formation\\weigh_anchor', confidence=0.7)

    return


def handleInCompleteState():
    clickImage('.\\images\\complete\\confirm', confidence=0.7)
    return


def main():

    global maximum_ex_count
    global maximum_hard_count
    global maximum_normal_count
    global maximum_easy_count

    global current_ex_count
    global current_hard_count
    global current_normal_count
    global current_easy_count

    maximum_ex_count = 0
    maximum_hard_count = 0
    maximum_normal_count = 0
    maximum_easy_count = 0

    current_ex_count = 0
    current_hard_count = 0
    current_normal_count = 0
    current_easy_count = 0

    scriptName = sys.argv[0]
    maximum_ex_count = int(sys.argv[1])
    maximum_hard_count = int(sys.argv[2])
    maximum_normal_count = int(sys.argv[3])
    maximum_easy_count = int(sys.argv[4])
    
    print('Start runnng: ' + scriptName)
    print('Run EX: ' + str(maximum_ex_count) + ' time(s)')
    print('Run Hard: ' + str(maximum_hard_count) + ' time(s)')
    print('Run Normal: ' + str(maximum_normal_count) + ' time(s)')
    print('Run Easy: ' + str(maximum_easy_count) + ' time(s)')
    print('Press Ctrl-C to quit.')

    while current_ex_count < maximum_ex_count or current_hard_count < maximum_hard_count or current_normal_count < maximum_normal_count or current_easy_count < maximum_easy_count:
        print('...')
        currentGameState = checkGameState()
        print(
            '============================================================================')
        print('Current Game State: ' + currentGameState.name)

        if currentGameState == GameState.Other:
            handleOtherState()

        elif currentGameState == GameState.PreCombat:
            handlePreCombatState()

        elif currentGameState == GameState.Formation:
            handleFormationState()

        elif currentGameState == GameState.Complete:
            handleInCompleteState()
    
    print('Current EX: ' + str(current_ex_count) + '/' + str(maximum_ex_count) + ' time(s)')
    print('Current Hard: ' + str(current_hard_count) + '/' + str(maximum_hard_count) + ' time(s)')
    print('Current Normal: ' + str(current_normal_count) + '/' + str(maximum_normal_count) + ' time(s)')
    print('Current Easy: ' + str(current_easy_count) + '/' + str(maximum_easy_count) + ' time(s)')
    print('Done')
    return

if __name__ == '__main__':
    main()
