from pyautogui import *
from time import sleep
import configparser
import threading
import keyboard

INTERRUPT_PRESSED = False
PAUSE_PRESSED = False

# All global variables are loaded from config.ini, with configure function
PAUSE = None
FAILSAFE = None
INITIAL_WAIT_TIME = None
ANIM_TIME = None
CURRENT_NAME = None
STOP_NAME = None
NAME_LENGTH = None
USE_RESTART_SWEEP = None
USE_TEXTFIELD = None
INTERRUPT_KEY = None
PAUSE_KEY = None

RESTART_SWEEP_X=None
RESTART_SWEEP_Y=None
EXPORT_X=None
EXPORT_Y=None
TEXTFIELD_X=None
TEXTFIELD_Y=None
SAVE_X=None
SAVE_Y=None

def main():
    configure()
    greet()
    wait_for_setup()
    run_interrupt_thread()
    run_pause_thread()
    sleep(INITIAL_WAIT_TIME)

    while True:
        if PAUSE_PRESSED:
            pause()
        if should_stop():
            break
        # click 'restart sweep' button (optional)
        if USE_RESTART_SWEEP:
            restart_sweep()
        # click 'export to matlab' button
        export()
        # click textfield to activate it (optional)
        if USE_TEXTFIELD:
            textfield()
        # enter new name for data file
        enter_text()
        # click 'save' button
        save()
        # sleep for 500ms because VNA couldn't keep up
        sleep(0.5)
        # increase current name number
        increase_current_name()
        
    bye()

def run_interrupt_thread():
    thread = threading.Thread(target=interrupt_thread, daemon=True)
    thread.start()

def run_pause_thread():
    thread = threading.Thread(target=pause_thread, daemon=True)
    thread.start()
def pause_thread():
    global PAUSE_PRESSED
    while True:
        if keyboard.is_pressed(PAUSE_KEY):
            PAUSE_PRESSED = True

def pause():
    global PAUSE_PRESSED
    alert(title='Information',
    text='Program has been paused. It will continue {} seconds after pressing OK.\n\nPress OK to continue.'.format(INITIAL_WAIT_TIME))
    PAUSE_PRESSED = False
    sleep(INITIAL_WAIT_TIME)

def interrupt_thread():
    global INTERRUPT_PRESSED
    while True:
        if keyboard.is_pressed(INTERRUPT_KEY):
            INTERRUPT_PRESSED = True
            break

def greet():
    alert(title='Information',
    text='This program executes multiple sweeps on VNA and saves them automatically.\n\nPress OK to continue.')

def bye():
    alert(title='Information',
    text='Program has stopped working without errors.\n\nPress Ok to end current session.')

def wait_for_setup():
    alert(title='Information',
    text='Program will start executing after {} seconds when you click OK.\n\nPress OK when ready.'.format(INITIAL_WAIT_TIME))
    
def should_stop():
    if (int(CURRENT_NAME) >= int(STOP_NAME)) or INTERRUPT_PRESSED:
        print("Stopping program.")
        return True

def restart_sweep():
    moveTo(RESTART_SWEEP_X, RESTART_SWEEP_Y, ANIM_TIME, easeOutQuad)
    click()

def export():
    moveTo(EXPORT_X, EXPORT_Y, ANIM_TIME, easeOutQuad)
    click()

def textfield():
    moveTo(TEXTFIELD_X, TEXTFIELD_Y, ANIM_TIME, easeOutQuad)
    click()

def enter_text():
    write(CURRENT_NAME, interval=ANIM_TIME/len(CURRENT_NAME))

def save():
    moveTo(SAVE_X, SAVE_Y, ANIM_TIME, easeOutQuad)
    mouseDown()
    mouseUp()
    mouseDown()
    mouseUp()
    mouseDown()
    mouseUp()
    
def increase_current_name():
    global CURRENT_NAME
    CURRENT_NAME = str(int(CURRENT_NAME) + 1).zfill(NAME_LENGTH)

def configure():
    global FAILSAFE, PAUSE, INITIAL_WAIT_TIME, ANIM_TIME, CURRENT_NAME, STOP_NAME, NAME_LENGTH, USE_RESTART_SWEEP, USE_TEXTFIELD, INTERRUPT_KEY, PAUSE_KEY
    global RESTART_SWEEP_X, RESTART_SWEEP_Y, EXPORT_X, EXPORT_Y, TEXTFIELD_X, TEXTFIELD_Y, SAVE_X, SAVE_Y

    Config = configparser.ConfigParser()
    Config.read("config.ini")
    config_section = Config.get('Main', 'ACTIVE_CONFIG')

    INITIAL_WAIT_TIME = int(Config.get(config_section, 'INITIAL_WAIT_TIME'))
    PAUSE = float(Config.get(config_section, 'PAUSE_TIME'))
    FAILSAFE = bool(Config.get(config_section, 'FAILSAFE'))
    ANIM_TIME = float(Config.get(config_section, 'ANIM_TIME'))
    CURRENT_NAME = str(Config.get(config_section, 'START_NAME'))
    STOP_NAME = str(Config.get(config_section, 'STOP_NAME'))
    NAME_LENGTH = int(Config.get(config_section, 'NAME_LENGTH'))
    USE_RESTART_SWEEP = bool(Config.get(config_section, 'USE_RESTART_SWEEP'))
    USE_TEXTFIELD = bool(Config.get(config_section, 'USE_TEXTFIELD'))
    INTERRUPT_KEY = str(Config.get(config_section, 'INTERRUPT_KEY'))
    PAUSE_KEY = str(Config.get(config_section, 'PAUSE_KEY'))

    RESTART_SWEEP_X = int(Config.get('Locations', 'RESTART_SWEEP_X'))
    RESTART_SWEEP_Y = int(Config.get('Locations', 'RESTART_SWEEP_Y'))
    EXPORT_X = int(Config.get('Locations', 'EXPORT_X'))
    EXPORT_Y = int(Config.get('Locations', 'EXPORT_Y'))
    TEXTFIELD_X = int(Config.get('Locations', 'TEXTFIELD_X'))
    TEXTFIELD_Y = int(Config.get('Locations', 'TEXTFIELD_Y'))
    SAVE_X = int(Config.get('Locations', 'SAVE_X'))
    SAVE_Y = int(Config.get('Locations', 'SAVE_Y'))

if __name__ == "__main__":
    main()
