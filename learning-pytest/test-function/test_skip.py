import pytest


@pytest.mark.skip(reason='out-of-date api')
def test_connect():
    pass


@pytest.mark.skipif(1 < 2, reason='1 < 2')  # 判断是否跳过
def test_api():
    pass
