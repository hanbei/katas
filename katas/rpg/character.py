class Character(object):

    def __init__(self):
        self.health = 1000
        self.level = 1

    def deal_damage(self, opponent: 'Character', damage: int):
        real_damage = damage
        if opponent == self:
            real_damage = 0
        if opponent.level >= self.level + 5:
            real_damage = damage / 2
        if opponent.level <= self.level - 5:
            real_damage = damage * 2

        opponent.take_damage(real_damage)

    def take_damage(self, damage: int):
        self.health = max(0, self.health - damage)

    def heal(self, hp: int):
        if self.is_alive():
            self.health = min(1000, self.health + hp)

    def is_alive(self) -> bool:
        return not self.is_dead()

    def is_dead(self) -> bool:
        return self.health <= 0
