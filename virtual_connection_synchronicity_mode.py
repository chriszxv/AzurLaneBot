import pyautogui
import cv2
import sys

from enum import Enum

pyautogui.FAILSAFE = True


class GameState(Enum):
    Other = 'other'
    PreCombat = 'precombat'
    SubChapter = 'subchapter'
    Combat = 'combat'


def localeImage(image, confidence=0.7):
    return pyautogui.locateOnScreen(image + '.png', confidence=confidence, grayscale=True)


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


def checkGameState():
    location = localeImage(
        '.\\images\\virtual_connection_synchronicity\\event_bonus', confidence=0.9)
    if location is not None:
        return GameState.PreCombat

    location = localeImage(
        '.\\images\\subchapter\\offensive', confidence=0.7)
    if location is not None:
        return GameState.SubChapter

    location = localeImage('.\\images\\combat\\button_pause', confidence=0.7)
    if location is not None:
        return GameState.Combat

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


def handlePreCombatState():
    print('handle sub chapter:')
    handleSubChapter()
    return


def handleSubChapter():
    print('click sp 4...')
    clickImage('.\\images\\virtual_connection_synchronicity\\sp_4',
               confidence=0.9)

    print('click strike button 1...')
    clickImage('.\\images\\precombat\\strike', confidence=0.7)

    print('click strike button 2...')
    clickImage('.\\images\\precombat\\strike', confidence=0.7)
    return


def handleSubChapterState():

    findShipBoss()
    findShipGirl()

    findShipBoss()
    findShipBattleship()

    findShipBoss()
    findShipDestroyer()

    findShipBoss()
    findShipCarrier()

    return


def findShipBoss():
    print('click ship boss...')
    clickImage(
        '.\\images\\virtual_connection_synchronicity\\ship_boss_2', confidence=0.7)
    return


def findShipGirl():
    print('click ship girl...')
    clickImage(
        '.\\images\\virtual_connection_synchronicity\\ship_fortune_1', confidence=0.7)
    clickImage(
        '.\\images\\virtual_connection_synchronicity\\ship_fortune_4', confidence=0.7)
    clickImage(
        '.\\images\\virtual_connection_synchronicity\\ship_prinz_eugen_1', confidence=0.7)
    clickImage(
        '.\\images\\virtual_connection_synchronicity\\ship_prinz_eugen_4', confidence=0.7)
    clickImage(
        '.\\images\\virtual_connection_synchronicity\\ship_shokaku_1', confidence=0.7)
    clickImage(
        '.\\images\\virtual_connection_synchronicity\\ship_takao_4', confidence=0.7)
    return


def findShipBattleship():
    print('click ship battleship...')
    clickImage(
        '.\\images\\virtual_connection_synchronicity\\ship_battleship_3', confidence=0.7)
    clickImage(
        '.\\images\\virtual_connection_synchronicity\\ship_battleship_4', confidence=0.7)
    clickImage(
        '.\\images\\virtual_connection_synchronicity\\ship_battleship_5', confidence=0.7)
    return


def findShipDestroyer():
    print('click ship destroyer...')
    clickImage(
        '.\\images\\virtual_connection_synchronicity\\ship_destroyer_5', confidence=0.7)
    clickImage(
        '.\\images\\virtual_connection_synchronicity\\ship_destroyer_6', confidence=0.7)
    clickImage(
        '.\\images\\virtual_connection_synchronicity\\ship_destroyer_7', confidence=0.7)
    return


def findShipCarrier():
    print('click ship carrier...')
    clickImage(
        '.\\images\\virtual_connection_synchronicity\\ship_carrier_4', confidence=0.7)
    clickImage(
        '.\\images\\virtual_connection_synchronicity\\ship_carrier_6', confidence=0.7)
    clickImage(
        '.\\images\\virtual_connection_synchronicity\\ship_carrier_7', confidence=0.7)
    return


def handleCombatState():
    print('click auto off if exists...')
    location = localeImage('.\\images\\combat\\auto_off', confidence=0.9)
    if location is not None:
        clickImageUntilSuccess('.\\images\\combat\\auto_off')

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
        print('============================================================================')
        print('Current Game State: ' + currentGameState.name)

        if currentGameState == GameState.Other:
            handleOtherState()

        elif currentGameState == GameState.PreCombat:
            handlePreCombatState()

        elif currentGameState == GameState.SubChapter:
            handleSubChapterState()

        elif currentGameState == GameState.Combat:
            handleCombatState()
    return


if __name__ == '__main__':
    main()
