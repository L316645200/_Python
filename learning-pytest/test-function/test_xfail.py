import pytest


@pytest.mark.xfail(1 < 2,
                   reason='not supported until v0.2.0')
def test_api():
    id_1 = 1
    id_2 = 2
    assert id_1 != id_2
