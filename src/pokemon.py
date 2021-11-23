import random
from enum import Enum, auto


class TypePokeBall(Enum):
    """Type of poke balls throw to pokemon"""

    MASTER_BALL = auto()
    POKE_BALL = auto()
    GREAT_BALL = auto()
    ULTRA_BALL = auto()


class StatusPokemon(Enum):
    """Possible status for the pokemon in anytime"""
    ASLEEP = auto()
    FROZEN = auto()
    PARALYZED = auto()
    BURNED = auto()
    POISONED = auto()


class PokeBall:
    """Basic representation of an Poke Ball"""

    def __init__(self, type_poke_ball: TypePokeBall) -> None:
        self.type = type_poke_ball
        self.rand_number = None

        if self.type.POKE_BALL:
            self.rand_number = random.randint(0, 255)
        if self.type.GREAT_BALL:
            self.rand_number = random.randint(0, 200)
        if self.type.ULTRA_BALL:
            self.rand_number = random.randint(0, 150)

    def __str__(self) -> str:
        return f"Type: {self.type.name} - Associate Random Number: {self.rand_number}"


class Pokemon:
    """Class that represents a Pokemon"""

    THRESHOLD_25 = 25
    THRESHOLD_12 = 12

    def __init__(self, name, catch_rate):
        self.is_caught = False
        self.status = None
        self.name = name
        self.catch_rate = catch_rate

    def set_catch_rate(self, poke_ball: PokeBall) -> None:
        self.catch_rate = self.catch_rate + (
                self.THRESHOLD_25 / poke_ball.rand_number)

    def set_status(self, status: StatusPokemon) -> None:
        self.status = status

    def catch_attempt(self, poke_ball: PokeBall) -> None:
        if poke_ball.type == TypePokeBall.MASTER_BALL:
            self.is_caught = True
        elif poke_ball.rand_number < self.THRESHOLD_25 and (
                self.status == StatusPokemon.ASLEEP or
                self.status == StatusPokemon.FROZEN):
            self.is_caught = True
        elif poke_ball.rand_number < self.THRESHOLD_12 and (
                self.status == StatusPokemon.PARALYZED or
                self.status == StatusPokemon.BURNED or
                self.status == StatusPokemon.POISONED):
            self.is_caught = True
        else:
            self.is_caught = False
            self.set_catch_rate(poke_ball)

    def __str__(self) -> str:
        return f"Name: {self.name} - Status: {self.status.name}"

