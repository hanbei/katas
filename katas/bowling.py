class Game(object):

    def __init__(self):
        self.frames = []
        self.current_frame = None
        self.last_frame = None

    def roll(self, pins: int) -> None:
        if len(self.frames) == 10:
            return

        if not self.current_frame:
            self.current_frame = Frame().first_roll(pins)

            if self.last_frame is not None:
                if self.last_frame.is_spare() or self.last_frame.is_strike():
                    self.last_frame.add_bonus(pins)
        else:
            self.current_frame.second_roll(pins)
            if self.last_frame is not None:
                if self.last_frame.is_strike():
                    self.last_frame.add_bonus(pins)

        if self.current_frame.ended():
            self.frames.append(self.current_frame)
            self.last_frame = self.current_frame
            self.current_frame = None

    def score(self) -> int:
        return sum(map(lambda f: f.score(), self.frames))


class Frame(object):

    def __init__(self):
        self._first_roll = 0
        self._first_rolled = False
        self._second_roll = 0
        self._second_rolled = False
        self._bonus = 0

    def first_roll(self, pins: int) -> 'Frame':
        self._first_roll = pins
        self._first_rolled = True
        return self

    def second_roll(self, pins: int) -> 'Frame':
        if self._first_roll != 10:
            self._second_roll = pins
            self._second_rolled = True
        return self

    def is_strike(self) -> bool:
        return self._first_roll == 10

    def is_spare(self) -> bool:
        return self._first_roll != 10 and (self._first_roll + self._second_roll) == 10

    def score(self):
        return self._first_roll + self._second_roll + self._bonus

    def add_bonus(self, pins: int) -> 'Frame':
        self._bonus += pins
        return self

    def ended(self) -> bool:
        return (self._first_rolled and self._first_roll == 10) or (self._first_rolled and self._second_rolled)
