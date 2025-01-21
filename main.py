import pyautogui
import time
import json
import schedule
from threading import Thread

class AutoClicker:
    def __init__(self):
        self.sequence = []
        self.is_recording = False

    def sample_point(self):
        """Get the current mouse position."""
        x, y = pyautogui.position()
        print(f"Sampled Point: ({x}, {y})")
        return x, y

    def record_sequence(self):
        """Record a sequence of mouse clicks."""
        print("Recording sequence. Press Ctrl+C to stop.")
        self.sequence = []
        self.is_recording = True
        try:
            while self.is_recording:
                x, y = pyautogui.position()
                button = 'left'  # Assuming left-click for simplicity
                time.sleep(0.5)  # Sampling interval
                print(f"Recorded: ({x}, {y}, {button})")
                self.sequence.append({"x": x, "y": y, "button": button, "delay": 0.5})
        except KeyboardInterrupt:
            print("Recording stopped.")
            self.is_recording = False

    def save_sequence(self, filename):
        """Save the recorded sequence to a file."""
        with open(filename, 'w') as file:
            json.dump(self.sequence, file)
        print(f"Sequence saved to {filename}")

    def load_sequence(self, filename):
        """Load a click sequence from a file."""
        with open(filename, 'r') as file:
            self.sequence = json.load(file)
        print(f"Sequence loaded from {filename}")

    def play_sequence(self):
        """Play the loaded sequence."""
        if not self.sequence:
            print("No sequence loaded.")
            return
        print("Playing sequence...")
        for action in self.sequence:
            x, y, button, delay = action["x"], action["y"], action["button"], action["delay"]
            pyautogui.click(x=x, y=y, button=button)
            time.sleep(delay)
        print("Sequence playback complete.")

    def schedule_playback(self, filename, time_str):
        """Schedule playback of a sequence at a specified time."""
        self.load_sequence(filename)
        schedule.every().day.at(time_str).do(self.play_sequence)
        print(f"Scheduled playback at {time_str}")
        
        def run_schedule():
            while True:
                schedule.run_pending()
                time.sleep(1)
        Thread(target=run_schedule).start()

if __name__ == "__main__":
    clicker = AutoClicker()
    while True:
        print("\nOptions:")
        print("1. Sample Point")
        print("2. Record Sequence")
        print("3. Save Sequence")
        print("4. Load Sequence")
        print("5. Play Sequence")
        print("6. Schedule Playback")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            clicker.sample_point()
        elif choice == "2":
            clicker.record_sequence()
        elif choice == "3":
            filename = input("Enter filename to save sequence: ")
            clicker.save_sequence(filename)
        elif choice == "4":
            filename = input("Enter filename to load sequence: ")
            clicker.load_sequence(filename)
        elif choice == "5":
            clicker.play_sequence()
        elif choice == "6":
            filename = input("Enter filename to load sequence: ")
            time_str = input("Enter time for playback (HH:MM): ")
            clicker.schedule_playback(filename, time_str)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
