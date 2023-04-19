import pytest

from katas.cupcake import Cupcake, Cookie, Chocolate, Nuts, Sugar, Bundle


def test_cupcake():
    cupkake = Cupcake()

    assert cupkake.name() == "🧁"
    assert cupkake.price() == 1


def test_cookie():
    cookie = Cookie()

    assert cookie.name() == "🍪"
    assert cookie.price() == 2


def test_chocolate_cookie():
    chccolateCookie = Chocolate(Cookie())

    assert chccolateCookie.name() == "🍪 with chocolate"
    assert chccolateCookie.price() == pytest.approx(2.1)


def test_chocolate_cookie_with_nuts():
    chccolateCookie = Nuts(Chocolate(Cookie()))

    assert chccolateCookie.name() == "🍪 with chocolate with nuts"
    assert chccolateCookie.price() == pytest.approx(2.3)


def test_cupcake_with_all():
    chccolateCookie = Nuts(Sugar(Chocolate(Cupcake())))

    assert chccolateCookie.name() == "🧁 with chocolate with sugar with nuts"
    assert chccolateCookie.price() == pytest.approx(1.4)


def test_bundle():
    bundle = Bundle([Cupcake(), Cookie()])

    assert bundle.name() == "(🧁,🍪)"
    assert bundle.price() == pytest.approx(3 * 0.9)
