import pytest

# Pytest 使用 pytest.fixture() 定义固件，下面是最简单的固件，只返回北京邮编：
@pytest.fixture()
def postcode():
    return '010'


def test_postcode(postcode):
    assert postcode == '010'

# 固件可以直接定义在各测试脚本中，就像上面的例子。更多时候，我们希望一个固件可以在更大程度上复用，这就需要对固件进行集中管理。Pytest 使用文件 conftest.py 集中管理固件。
