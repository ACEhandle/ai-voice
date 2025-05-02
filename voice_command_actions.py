import pyautogui
import subprocess
import time

def handle_command(text):
    """
    Perform actions based on recognized voice command text.
    Supports: click, double click, move to top left, click by image, open program, switch window.
    """
    t = text.lower()
    if "double click" in t:
        pyautogui.doubleClick()
        print("Mouse double-clicked!")
    elif "click by image" in t:
        # Example: "click by image ok_button.png"
        parts = t.split()
        for i, part in enumerate(parts):
            if part == "image" and i+1 < len(parts):
                image_file = parts[i+1]
                print(f"Looking for image: {image_file}")
                location = pyautogui.locateCenterOnScreen(image_file, confidence=0.8)
                if location:
                    pyautogui.click(location)
                    print(f"Clicked on {image_file} at {location}")
                else:
                    print(f"Image {image_file} not found on screen.")
                return
        pyautogui.click()
        print("Mouse clicked!")
    elif "click" in t:
        pyautogui.click()
        print("Mouse clicked!")
    elif "top left" in t:
        pyautogui.moveTo(0, 0)
        print("Mouse moved to top left!")
    elif "switch window" in t or "alt tab" in t:
        pyautogui.hotkey('alt', 'tab')
        print("Switched window (alt+tab)")
    elif "open" in t:
        # Example: "open notepad" or "open chrome"
        app = t.split("open",1)[1].strip()
        if app:
            try:
                subprocess.Popen(app)
                print(f"Opened program: {app}")
            except Exception as e:
                print(f"Failed to open {app}: {e}")
        else:
            print("No program specified to open.")
    # Add more commands as needed
