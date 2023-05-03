from katas.rpg.character import Character


def test_character_health_cant_raise_above_1000():
    character = Character()
    character.health = 500
    character.heal(1000)
    assert character.health == 1000


def test_dead_character_cant_be_healed():
    character = Character()
    character.health = 0
    assert character.is_dead()

    character.heal(100)
    assert character.is_dead()


def test_character_health_cant_fall_below_zero():
    character = Character()
    character.health = 500
    character.take_damage(1000)
    assert character.health == 0


def test_deal_damage():
    character = Character()
    opponent = Character()

    character.deal_damage(opponent, 100)
    assert opponent.health == 900


def test_cant_deal_damage_to_self():
    character = Character()

    character.deal_damage(character, 100)
    assert character.health == 1000


def test_damage_increases_to_lower_level():
    character = Character()
    character.level = 10

    opponent = Character()

    character.deal_damage(opponent, 100)
    assert opponent.health == 800


def test_damage_decreases_to_higher_level():
    character = Character()

    opponent = Character()
    opponent.level = 10

    character.deal_damage(opponent, 100)
    assert opponent.health == 950
