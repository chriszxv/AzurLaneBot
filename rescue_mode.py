import time
import pyautogui
import cv2
import sys

from enum import Enum

pyautogui.FAILSAFE = True


class GameState(Enum):
    Other = 'other'
    PreCombat = 'precombat'
    SubChapter = 'subchapter'
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
    location = localeImage(
        '.\\images\\precombat\\rescue_signal_1', confidence=0.7)
    if location is not None:
        return GameState.PreCombat
    location = localeImage(
        '.\\images\\precombat\\rescue_signal_2', confidence=0.7)
    if location is not None:
        return GameState.PreCombat

    location = localeImage('.\\images\\subchapter\\offensive', confidence=0.7)
    if location is not None:
        return GameState.SubChapter

    location = localeImage(
        '.\\images\\formation\\auto_fight_off', confidence=0.7)
    if location is not None:
        return GameState.Formation
    location = localeImage(
        '.\\images\\formation\\auto_fight_on', confidence=0.7)
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
    print('handle rescue chapter:')
    handleRescueChapter()

    print('handle sub chapter:')
    handleSubChapter()
    return


def handleRescueChapter():
    print('click rescue signal...')
    clickImage('.\\images\\precombat\\rescue_signal_1')
    clickImage('.\\images\\precombat\\rescue_signal_2')

    print('click rescue...')
    clickImageUntilSuccess('.\\images\\precombat\\rescue')
    return


def handleSubChapter():
    print('click sub chapter...')
    clickImage('.\\images\\precombat\\sub_chapter_X_5', confidence=0.7)

    print('click strike button 1...')
    clickImage('.\\images\\precombat\\strike', confidence=0.7)

    print('click strike button 2...')
    clickImage('.\\images\\precombat\\strike', confidence=0.7)

    print('wait animation...')
    time.sleep(4.0)
    print('Reset panel postion...')
    pressKey('A', 4)
    pressKey('S', 1)

    return


def handleSubChapterState():
    print('wait animation...')
    time.sleep(3.0)

    findShipBoss()
    findShipBattleship()

    findShipBoss()
    findShipDestroyer()

    findShipBoss()
    findShipCarrier()
    return


def findShipBoss():
    print('click ship boss...')
    clickImage('.\\images\\subchapter\\ship_boss_1', confidence=0.7)
    clickImage('.\\images\\subchapter\\ship_boss_2', confidence=0.7)
    # clickImage('.\\images\\subchapter\\ship_boss_3', confidence = 0.7)
    # clickImage('.\\images\\subchapter\\ship_boss_4', confidence = 0.7)
    # clickImage('.\\images\\subchapter\\ship_boss_5', confidence = 0.7)
    # clickImage('.\\images\\subchapter\\ship_boss_6', confidence = 0.7)
    clickImage('.\\images\\subchapter\\ship_boss_7', confidence=0.7)
    return


def findShipBattleship():
    print('click ship battleship...')
    clickImage('.\\images\\subchapter\\ship_battleship_1', confidence=0.7)
    clickImage('.\\images\\subchapter\\ship_battleship_2', confidence=0.7)
    clickImage('.\\images\\subchapter\\ship_battleship_3', confidence=0.7)
    clickImage('.\\images\\subchapter\\ship_battleship_4', confidence=0.7)
    clickImage('.\\images\\subchapter\\ship_battleship_5', confidence=0.7)
    clickImage('.\\images\\subchapter\\ship_battleship_6', confidence=0.7)
    clickImage('.\\images\\subchapter\\ship_battleship_7', confidence=0.7)
    return


def findShipDestroyer():
    print('click ship destroyer...')
    clickImage('.\\images\\subchapter\\ship_destroyer_1', confidence=0.7)
    clickImage('.\\images\\subchapter\\ship_destroyer_2', confidence=0.7)
    clickImage('.\\images\\subchapter\\ship_destroyer_3', confidence=0.7)
    clickImage('.\\images\\subchapter\\ship_destroyer_4', confidence=0.7)
    clickImage('.\\images\\subchapter\\ship_destroyer_5', confidence=0.7)
    clickImage('.\\images\\subchapter\\ship_destroyer_6', confidence=0.7)
    clickImage('.\\images\\subchapter\\ship_destroyer_7', confidence=0.7)
    return


def findShipCarrier():
    print('click ship carrier...')
    clickImage('.\\images\\subchapter\\ship_carrier_1', confidence=0.7)
    clickImage('.\\images\\subchapter\\ship_carrier_2', confidence=0.7)
    clickImage('.\\images\\subchapter\\ship_carrier_3', confidence=0.7)
    clickImage('.\\images\\subchapter\\ship_carrier_4', confidence=0.7)
    clickImage('.\\images\\subchapter\\ship_carrier_5', confidence=0.7)
    clickImage('.\\images\\subchapter\\ship_carrier_6', confidence=0.7)
    # clickImage('.\\images\\subchapter\\ship_carrier_7', confidence = 0.7)
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
    scriptName = sys.argv[0]
    print('Start runnng: ' + scriptName)
    print('Press Ctrl-C to quit.')

    while True:
        print('...')
        currentGameState = checkGameState()
        print(
            '============================================================================')
        print('Current Game State: ' + currentGameState.name)

        if currentGameState == GameState.Other:
            handleOtherState()

        elif currentGameState == GameState.PreCombat:
            handlePreCombatState()

        elif currentGameState == GameState.SubChapter:
            handleSubChapterState()

        elif currentGameState == GameState.Formation:
            handleFormationState()

        elif currentGameState == GameState.Complete:
            handleInCompleteState()
    return


if __name__ == '__main__':
    main()
