from dataclasses import dataclass


@dataclass(frozen=True)
class Roll(object):
    value: int

    def strike(self):
        return self.value == 10


@dataclass(frozen=True)
class NoRoll(Roll):
    value: int = 0


@dataclass
class Frame():
    first_roll: Roll
    second_roll: Roll = NoRoll()

    def score(self) -> int:
        return self.first_roll.value + self.second_roll.value

    def spare_bonus(self) -> int:
        return self.first_roll.value

    def strike_bonus(self) -> int:
        return self.first_roll.value + self.second_roll.value

    def strike(self) -> bool:
        return self.first_roll.strike()

    def spare(self) -> bool:
        return not self.first_roll.strike() and self.score() == 10


class Game():

    def __init__(self):
        self._frames = []

    def add_frame(self, frame: Frame):
        self._frames.append(frame)

    def score(self) -> int:
        score = 0
        for i in range(0, 10):
            score += self._score_frame(i)

        return score

    def _score_frame(self, index):
        score = self._frames[index].score()

        score += self._score_spare(index)
        score += self._score_strike(index)

        return score

    def _score_strike(self, i):
        score = 0
        if self._frames[i].strike():
            next_frame = self._frames[i + 1]
            score += next_frame.strike_bonus()
            if next_frame.strike():
                score += self._frames[i + 2].strike_bonus()
        return score

    def _score_spare(self, i):
        if self._frames[i].spare():
            return self._frames[i + 1].spare_bonus()

        return 0


def parse_game(line: str) -> Game:
    game = Game()
    split = line.split(' ')
    parse_frames(game, split)
    return game


def parse_frames(game, split):
    for f in split:
        if strike(f):
            _parse_strike(game)
        elif spare(f):
            _parse_spare(f, game)
        elif miss(f):
            _parse_frame_with_miss(f, game)
        else:
            _parse_frame(f, game)


def _parse_frame(f, game):
    x = int(f[0])
    y = int(f[1])
    frame = Frame(Roll(x), Roll(y))
    game.add_frame(frame)


def _parse_frame_with_miss(f, game):
    x = int(f[0]) if not miss(f[0]) else 0
    frame = Frame(Roll(x), Roll(0))
    game.add_frame(frame)


def _parse_strike(game):
    frame = Frame(Roll(10))
    game.add_frame(frame)


def _parse_spare(f, game):
    x = int(f[0])
    frame = Frame(Roll(x), Roll(10 - x))
    game.add_frame(frame)
    if has_bonus_roll(f):
        x = int(f[2]) if not strike(f[2]) else 10
        frame = Frame(Roll(x))
        game.add_frame(frame)


def has_bonus_roll(f):
    return len(f) == 3


def strike(x: str) -> bool:
    return x == 'X'


def spare(x: str) -> bool:
    return "/" in x


def miss(x: str) -> bool:
    return '-' in x
