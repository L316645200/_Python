from sqlite3 import connect

import pytest


def test_raises():
    with pytest.raises(TypeError) as e:
        connect('localhost', '6379')
    exec_msg = e.value.args[0]
    print(exec_msg)
    assert exec_msg == 'must be real number, not str'
