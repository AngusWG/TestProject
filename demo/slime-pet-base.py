import random


class SlimePet:
    def __init__(self):
        self._init_ui()
        super().__init__()

    def _init_ui(self):
        ...

    def run_forever(self):
        events = {
            "move_by_roll": self._move_by_roll,
            "move_by_jump": self._move_by_jump,
        }
        event = random.choice(list(events.keys()))
        func = events[event]
        func()
        ...

    def _move(self, x, y):
        ...

    def _move_by_roll(self):
        ...

    def _move_by_jump(self):
        ...


if __name__ == "__main__":
    SlimePet().run_forever()
