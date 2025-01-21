import pyautogui
import schedule
import time
import json

class ClickAction:
    def init(self, x, y, button="left", delay=0.5):
        self.x = x
        self.y = y
        self.button = button
        self.delay = delay

    def execute(self):
        pyautogui.click(x=self.x, y=self.y, button=self.button)
        time.sleep(self.delay)

    def modify_delay(self, new_delay):
        self.delay = new_delay

    def __repr__(self):
        return f"ClickAction(x={self.x}, y={self.y}, button='{self.button}', delay={self.delay})"