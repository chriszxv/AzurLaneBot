# AzurLaneBot

Python bot for lazy people to play [AzurLane](https://azurlane.yo-star.com/)

## Requirement

- Use Windows 10
- Support Python 3.X.X
- Support PyAutoGUI

## Installation

1. Setup Android Emulator

  - Download free Android emulator from [NoxPlayer](https://www.bignox.com/)
  - Install in to your Windows
  - Enable [virtualization](https://support.bluestacks.com/hc/en-us/articles/115003174386-How-can-I-enable-virtualization-VT-on-my-PC-)
  - Follow the settings:

    ![](images/readme/setting_1.png)

    ![](images/readme/setting_2.png)

    ![](images/readme/setting_3.png)

    ![](images/readme/setting_4.png)

2. Download Azur Lane

  - Download [QooApp](https://apps.qoo-app.com/en) in NoxPlayer
  - Install AzurLane via QooApp

3. Setup keyboard config for AzurLane

  - Copy `keyboard_control\com.YoStarJP.AzurLane` to the following folder:

    ```
    C:\Users\USER_NAME\AppData\Local\Nox\keyboardConfig
    ```

  - The result should be like this:

    ![](images/readme/keyboard_control.png)

## Mode

Start bot by typing following commands in this current directory

### Crossing Waves `new`

Run Crossing Waves Bot for `Ex n times`, `Hard n times`, `Normal n times`, `Easy n times`

1. Go to event screen:

  ![](images/readme/crossing_waves.png)

2. Enter command (Example: run each difficulties for 15 times)

  ```
  $ py .\crossing_waves.py 15 15 15 15
  ```

⚠️ **WARNING** ⚠️ : Make sure that you have enough `Special Pass` tokens for extra rounds. The bot will use up all the tokens based on how many running times you type for each difficulties.

--------------------------------------------------------------------------------

### Rescue Mode

1. Go to weigh anchor screen:

  ![](images/readme/weigh_anchor.png)

2. Enter command in terminal

  ```
  $ py .\rescue_mode.py
  ```

⚠️ **WARNING** ⚠️ :Make sure that you scanned rescue signals. The bot will go through all the rescue signals in the signal list only.

## To-Do

- Fix normal mode for `3-4`, `6-4` etc
- Support PvP Bot
- Support Daily Task Bot
