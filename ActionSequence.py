import json
from ClickAction import ClickAction


class ActionSequence:
    def init(self):
        self.actions = []


    def add_action(self, action):
        self.actions.append(action)

    def remove_action(self, index):
        if 0 <= index < len(self.actions):
            del self.actions[index]

    def execute_all(self):
        for action in self.actions:
            action.execute()

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump([action.__dict__ for action in self.actions], file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.actions = [ClickAction(**action) for action in data]

    def __repr__(self):
        return f"ActionSequence(actions={self.actions})"