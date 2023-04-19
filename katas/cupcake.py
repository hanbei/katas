from abc import abstractmethod, ABC


class Cake(ABC):
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def price(self) -> float:
        pass


class Cupcake(Cake):

    def name(self) -> str:
        return "🧁"

    def price(self) -> float:
        return 1


class Cookie(Cake):

    def name(self) -> str:
        return "🍪"

    def price(self) -> float:
        return 2


class Chocolate(Cake):

    def __init__(self, cake: Cake):
        self._cake = cake

    def name(self) -> str:
        return f"{self._cake.name()} with chocolate"

    def price(self) -> float:
        return self._cake.price() + 0.1


class Nuts(Cake):

    def __init__(self, cake: Cake):
        self._cake = cake

    def name(self) -> str:
        return f"{self._cake.name()} with nuts"

    def price(self) -> float:
        return self._cake.price() + 0.2


class Sugar(Cake):

    def __init__(self, cake: Cake):
        self._cake = cake

    def name(self) -> str:
        return f"{self._cake.name()} with sugar"

    def price(self) -> float:
        return self._cake.price() + 0.1


class Bundle(Cake):

    def __init__(self, cakes: list[Cake]):
        self._cakes = cakes

    def name(self) -> str:
        return f"({','.join(map(lambda x: x.name(), self._cakes))})"

    def price(self) -> float:
        return sum(map(lambda x: x.price(), self._cakes)) * 0.9
