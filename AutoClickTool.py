import pyautogui
import schedule
import time
import json
from ActionSequence import ActionSequence
from ClickAction import ClickAction


class AutoClickTool:
    def init(self):
        self.sequence = ActionSequence()

    def sample_point(self):
        x, y = pyautogui.position()
        print(f"Current mouse position: ({x}, {y})")

    def record_sequence(self):
        print("Recording started. Press Ctrl+C to stop.")
        try:
            while True:
                x, y = pyautogui.position()
                button = "left"
                delay = 0.5
                self.sequence.add_action(ClickAction(x, y, button, delay))
                time.sleep(0.5)
        except KeyboardInterrupt:
            print("Recording stopped.")

    def save_sequence(self, filename):
        self.sequence.save_to_file(filename)
        print(f"Sequence saved to {filename}.")

    def load_sequence(self, filename):
        self.sequence.load_from_file(filename)
        print(f"Sequence loaded from {filename}.")

    def play_sequence(self):
        print("Playing sequence...")
        self.sequence.execute_all()

    def schedule_playback(self, filename, time_string):
        self.load_sequence(filename)
        schedule.every().day.at(time_string).do(self.play_sequence)
        print(f"Scheduled playback at {time_string}.")
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == "main":
    tool = AutoClickTool()

    while True:
        print("\nSelect an option:")
        print("1. Sample current point")
        print("2. Record sequence")
        print("3. Save sequence to file")
        print("4. Load sequence from file")
        print("5. Play sequence")
        print("6. Schedule sequence playback")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            tool.sample_point()
        elif choice == "2":
            tool.record_sequence()
        elif choice == "3":
            filename = input("Enter filename to save: ")
            tool.save_sequence(filename)
        elif choice == "4":
            filename = input("Enter filename to load: ")
            tool.load_sequence(filename)
        elif choice == "5":
            tool.play_sequence()
        elif choice == "6":
            filename = input("Enter filename to load: ")
            time_string = input("Enter time for playback (HH:MM): ")
            tool.schedule_playback(filename, time_string)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")