class Character(object):

    def __init__(self):
        self.health = 1000
        self.level = 1

    def deal_damage(self, opponent: 'Character', damage: int):
        opponent.take_damage(damage)

    def take_damage(self, damage: int):
        self.health = max(0, self.health - damage)

    def heal(self, other_character: 'Character', hp: int):
        if other_character.is_alive():
            other_character.heal_by(hp)

    def heal_by(self, hp: int):
        if self.is_alive():
            self.health = min(1000, self.health + hp)

    def is_alive(self) -> bool:
        return not self.is_dead()

    def is_dead(self) -> bool:
        return self.health <= 0
