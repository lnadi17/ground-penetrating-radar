from pyautogui import *
from time import sleep
import configparser
import threading
import keyboard

INTERRUPT_PRESSED = False
PAUSE_PRESSED = False

# All global variables are loaded from config.ini, with configure function
FAILSAFE = None
INITIAL_WAIT_TIME = None
ANIM_TIME = None
CURRENT_NAME = None
STOP_NAME = None
NAME_LENGTH = None
USE_RESTART_SWEEP = None
INTERRUPT_KEY = None
PAUSE_KEY = None
SLEEP_TIME = None

EXPORT_X=None
EXPORT_Y=None

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
			
		# click 'data to new mem' button
		for _ in range(100):
			data_to_mem()
			sleep(SLEEP_TIME)
			
		# click 'trace data'
		trace_data()
		
        # click 'export to matlab' button
        export()
		
		# enter new name for data file
        enter_text()
		
        # click 'save' button
        save()
		
		# sleep because VNA couldn't keep up
        sleep(SLEEP_TIME * 5)
		
		# click 'all mem all data'
		all_mem_all_data()
		
		# click 'delete all mem'
		delete_all_mem()
		
		# click 'mem math'
		mem_math()

        # increase current name number
        increase_current_name()
        
    bye()

def data_to_mem():
	moveTo(DATA_TO_MEM_X, DATA_TO_MEM_Y, ANIM_TIME, easeOutQuad)
    click()
	
def trace_data():
	moveTo(TRACE_DATA_X, TRACE_DATA_Y, ANIM_TIME, easeOutQuad)
    click()
	
def all_mem_all_data():
	moveTo(ALL_MEM_ALL_DATA_X, ALL_MEM_ALL_DATA_Y, ANIM_TIME, easeOutQuad)
    click()
	
def delete_all_mem():
	moveTo(DELETE_ALL_MEM_X, DELETE_ALL_MEM_Y, ANIM_TIME, easeOutQuad)
    click()
	
def mem_math():
	moveTo(MEM_MATH_X, MEM_MATH_Y, ANIM_TIME, easeOutQuad)
    click()

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

def enter_text():
    write(CURRENT_NAME, interval=ANIM_TIME/len(CURRENT_NAME))

def save():
    press('enter')
    
def increase_current_name():
    global CURRENT_NAME
    CURRENT_NAME = str(int(CURRENT_NAME) + 1).zfill(NAME_LENGTH)

def configure():
    global FAILSAFE, INITIAL_WAIT_TIME, ANIM_TIME, CURRENT_NAME, STOP_NAME, NAME_LENGTH, USE_RESTART_SWEEP, INTERRUPT_KEY, PAUSE_KEY, SLEEP_TIME
    global RESTART_SWEEP_X, RESTART_SWEEP_Y, EXPORT_X, EXPORT_Y, DATA_TO_MEM_X, DATA_TO_MEM_Y, TRACE_DATA_X, TRACE_DATA_Y, ALL_MEM_ALL_DATA_X, ALL_MEM_ALL_DATA_Y, DELETE_ALL_MEM_X, DELETE_ALL_MEM_Y, MEM_MATH_X, MEM_MATH_Y

    Config = configparser.ConfigParser()
    Config.read("config.ini")
    config_section = Config.get('Main', 'ACTIVE_CONFIG')

    INITIAL_WAIT_TIME = int(Config.get(config_section, 'INITIAL_WAIT_TIME'))
    FAILSAFE = bool(Config.get(config_section, 'FAILSAFE'))
    ANIM_TIME = float(Config.get(config_section, 'ANIM_TIME'))
    CURRENT_NAME = str(Config.get(config_section, 'START_NAME'))
    STOP_NAME = str(Config.get(config_section, 'STOP_NAME'))
    NAME_LENGTH = int(Config.get(config_section, 'NAME_LENGTH'))
    USE_RESTART_SWEEP = bool(Config.get(config_section, 'USE_RESTART_SWEEP'))
    INTERRUPT_KEY = str(Config.get(config_section, 'INTERRUPT_KEY'))
    PAUSE_KEY = str(Config.get(config_section, 'PAUSE_KEY'))
	SLEEP_TIME = float(Config.get(config_section, 'SLEEP_TIME'))
	
	DATA_TO_MEM_X = int(Config.get('Locations', 'DATA_TO_MEM_X'))
    DATA_TO_MEM_Y = int(Config.get('Locations', 'DATA_TO_MEM_Y'))
	TRACE_DATA_X = int(Config.get('Locations', 'TRACE_DATA_X'))
    TRACE_DATA_Y = int(Config.get('Locations', 'TRACE_DATA_Y'))
	ALL_MEM_ALL_DATA_X = int(Config.get('Locations', 'ALL_MEM_ALL_DATA_X'))
    ALL_MEM_ALL_DATA_Y = int(Config.get('Locations', 'ALL_MEM_ALL_DATA_Y'))
	DELETE_ALL_MEM_X = int(Config.get('Locations', 'DELETE_ALL_MEM_X'))
    DELETE_ALL_MEM_Y = int(Config.get('Locations', 'DELETE_ALL_MEM_Y'))
	MEM_MATH_X = int(Config.get('Locations', 'MEM_MATH_X'))
    MEM_MATH_Y = int(Config.get('Locations', 'MEM_MATH_Y'))
    RESTART_SWEEP_X = int(Config.get('Locations', 'RESTART_SWEEP_X'))
    RESTART_SWEEP_Y = int(Config.get('Locations', 'RESTART_SWEEP_Y'))
    EXPORT_X = int(Config.get('Locations', 'EXPORT_X'))
    EXPORT_Y = int(Config.get('Locations', 'EXPORT_Y'))

if __name__ == "__main__":
    main()
